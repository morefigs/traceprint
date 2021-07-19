from typing import Optional, List
from sys import stdout
import builtins
from inspect import getframeinfo, stack, Traceback


class Options:
    limit = 0
    right_align = 30
    flatten_recurring_outputs = True


class State:
    frame_infos_previous: List[Traceback] = []


def set_options(limit: Optional[int] = None,
                right_align: Optional[int] = None,
                flatten_recurring_outputs: Optional[bool] = None):
    """
    Set printstack options.
    :param limit: print up to limit stack entries, if limit is above zero.
    :param right_align: number of characters to offset the link text to the right by.
    :param flatten_recurring_outputs: display recurring outputs (e.g. from a loop) inline instead of multiline.
    """
    if limit is not None:
        Options.limit = limit

    if right_align is not None:
        Options.right_align = right_align

    if flatten_recurring_outputs is not None:
        Options.flatten_recurring_outputs = flatten_recurring_outputs


def _build_print_str(*objects, sep: str, end: str) -> str:
    """
    Build the regular print string manually, removing (at most) one newline end for better formatting.
    """
    print_str = sep.join((str(e) for e in objects)) + end
    if print_str.endswith('\n'):
        print_str = print_str[:-1]
    return print_str


def _build_padding_str(print_str: str) -> str:
    """
    Build right justify padding, accounting for possible new lines.
    """
    if len(print_str) == 0 or print_str.endswith('\n') or print_str.endswith('\r'):
        width = 0
    else:
        width = len(print_str.splitlines()[-1])
    return ' ' * (Options.right_align - width)


def _build_link_str(frame_info: Traceback) -> str:
    """
    Build the clickable link string for a frame info object.
    """
    return f'File "{frame_info.filename}", line {frame_info.lineno}, in {frame_info.function}'


def _build_full_str(*objects, sep: str, end: str, frame_infos: List[Traceback]) -> str:
    """
    Build the entire string to output.
    """
    print_str = _build_print_str(*objects, sep=sep, end=end)

    # Print on a single line if limit/depth is 1
    if len(frame_infos) == 1:
        padding_str = _build_padding_str(print_str)
        link_str = _build_link_str(frame_infos[-1])
        return f'{print_str}{padding_str}{link_str}'

    # Else print in reverse similar to exception traceback with multiple lines
    link_str = '\n'.join(f'  {_build_link_str(frame_info)}' for frame_info in reversed(frame_infos))
    return f'\n{link_str}\n{print_str}'


print_orig = print


def _print_stack(*objects, sep=' ', end='\n', file=stdout, flush=False) -> None:
    stack_ = stack()

    frame_infos = []
    # Offset by 1 to hide this function call
    for i in range(1, len(stack_)):
        frame_infos.append(getframeinfo(stack_[i][0]))

    if Options.flatten_recurring_outputs and frame_infos == State.frame_infos_previous:
        limit = 1
    elif Options.limit:
        limit = min(Options.limit, len(stack_))
    else:
        limit = 0

    State.frame_infos_previous = frame_infos

    # Optionally trim the stack
    if limit:
        frame_infos = frame_infos[:limit]

    print_orig(_build_full_str(*objects, sep=sep, end=end, frame_infos=frame_infos), file=file, flush=flush)


def _print_suppress(*objects, sep=' ', end='\n', file=stdout, flush=False) -> None:
    pass


def enable() -> None:
    """
    Adds filename and line number to the builtin print function.
    """
    builtins.print = _print_stack


def disable():
    """
    Resets the print function to have its original behavior.
    """
    builtins.print = print_orig


def suppress() -> None:
    """
    Completely suppresses all print function calls.
    """
    builtins.print = _print_suppress

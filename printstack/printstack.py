from typing import Optional, List
import sys
import builtins
from inspect import getframeinfo, stack, Traceback
print_orig = print


LIMIT = 0
RIGHT_ALIGN = 30


def set_options(limit: Optional[int] = None, right_align: Optional[int] = None):
    """
    Set printstack options.
    """
    if limit is not None:
        global LIMIT
        LIMIT = limit

    if right_align is not None:
        global RIGHT_ALIGN
        RIGHT_ALIGN = right_align


def _build_link_str(frame_infos: List[Traceback]) -> str:
    return '\n'.join(f'  File "{info.filename}", line {info.lineno}, in {info.function}'
                     for info in frame_infos)


def _build_print_str(*objects, sep: str, end: str) -> str:
    # Manually build the regular print string, removing (one) newline end for better formatting
    print_str = sep.join((str(e) for e in objects)) + end
    if print_str.endswith('\n'):
        print_str = print_str[:-1]
    return print_str


def _build_padding_str(print_str: str) -> str:
    # Calculate right justify padding, accounting for possible new lines
    if len(print_str) == 0 or print_str.endswith('\n') or print_str.endswith('\r'):
        width = 0
    else:
        width = len(print_str.splitlines()[-1])
    return ' ' * (RIGHT_ALIGN - width - 2)


def _build_full_str(*objects, sep: str, end: str, frame_infos: List[Traceback]) -> str:
    link_str = _build_link_str(frame_infos)
    print_str = _build_print_str(*objects, sep=sep, end=end)

    # Print on a single line if depth is 1
    if len(frame_infos) == 1:
        padding_str = _build_padding_str(print_str)
        return f'{print_str}{padding_str}{link_str}'

    # Else prints similar to exception traceback for multiple lines
    return f'\n{link_str}\n{print_str}'


def enable() -> None:
    """
    Adds filename and line number to the builtin print function.
    """
    def _printstack(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
        # Subtract 1 to hide this function call
        limit = len(stack()) - 1
        if LIMIT:
            limit = min(limit, LIMIT)

        # Get the stack trace in reverse, similar to a traceback
        frame_infos = []
        for i in range(limit, 0, -1):
            frame_infos.append(getframeinfo(stack()[i][0]))

        print_orig(_build_full_str(*objects, sep=sep, end=end, frame_infos=frame_infos), file=file, flush=flush)

    builtins.print = _printstack


def disable():
    """
    Resets the print function to have its original behavior.
    """
    builtins.print = print_orig


def suppress() -> None:
    """
    Completely suppresses all print function calls.
    """
    def _printnull(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
        pass

    builtins.print = _printnull

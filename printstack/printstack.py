from typing import Optional
import sys
import builtins
from inspect import getframeinfo, stack
print_orig = print


STACK_DEPTH = 0
PADDING = 30


def set_options(stack_depth: Optional[int] = None, padding: Optional[int] = None):
    if stack_depth is not None:
        global STACK_DEPTH
        STACK_DEPTH = stack_depth

    if padding is not None:
        global PADDING
        PADDING = padding


def _link_str(info) -> str:
    return f'File "{info.filename}", line {info.lineno}, in {info.function}'


def enable() -> None:
    """
    Adds filename and line number to the builtin print function.
    """
    def _printstack(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
        # Overrides `end` to preserve formatting
        end = '\n'

        # Subtract 1 to hide this function call
        stack_depth = len(stack()) - 1
        if STACK_DEPTH:
            stack_depth = min(stack_depth, STACK_DEPTH)

        # Get the stack trace (without list comprehension, which adds to the stack)
        stack_infos = []
        for i in range(stack_depth, 0, -1):
            stack_infos.append(getframeinfo(stack()[i][0]))

        # Prints similar to exception traceback for multiple lines
        if stack_depth > 1:
            print_orig()
            for info in stack_infos:
                print_orig(f'  {_link_str(info)}')
            print_orig(*objects, sep=sep, end=end, file=file, flush=flush)

        # Prints on a single line if depth is 1
        else:
            padding = " " * (PAD_WIDTH - len(sep.join((f'{e}' for e in objects))))
            print_orig(*objects, padding, _link_str(stack_infos[0]), sep=sep, end=end, file=file, flush=flush)

    builtins.print = _printstack


def disable():
    builtins.print = print_orig


def _suppress() -> None:
    """
    Completely suppresses all print function calls.
    """
    def _printnull(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
        pass

    builtins.print = _printnull

from typing import Optional
import sys
import builtins
from inspect import getframeinfo, stack
print_orig = print


LIMIT = 0
RIGHT_ALIGN = 30


def set_options(limit: Optional[int] = None, right_align: Optional[int] = None):
    if limit is not None:
        global LIMIT
        LIMIT = limit

    if right_align is not None:
        global RIGHT_ALIGN
        RIGHT_ALIGN = right_align


def _link_str(info) -> str:
    return f'File "{info.filename}", line {info.lineno}, in {info.function}'


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
        stack_infos = []
        for i in range(limit, 0, -1):
            stack_infos.append(getframeinfo(stack()[i][0]))

        # Manually build the regular print string, appending end if not "empty"
        print_str = sep.join((str(e) for e in objects))
        print_str += end.strip()

        # Prints on a single line if depth is 1
        if limit == 1:

            # Calculate right justify padding, accounting for possible new lines
            if len(print_str) == 0 or print_str.endswith('\n') or print_str.endswith('\r'):
                width = 0
            else:
                width = len(print_str.splitlines()[-1])
            padding = '  ' + ' ' * (RIGHT_ALIGN - width - 2)

            complete_str = f'{print_str}{padding}{_link_str(stack_infos[0])}'

        # Prints similar to exception traceback for multiple lines
        else:
            link_strs = '\n'.join(f'  {_link_str(info)}' for info in stack_infos)
            complete_str = f'\n{link_strs}\n{print_str}'

        print_orig(complete_str, file=file, flush=flush)

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

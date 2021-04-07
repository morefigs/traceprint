import sys
import builtins
from inspect import getframeinfo, stack
from time import perf_counter


__print_orig = print
__prev_time = 0


def link() -> None:
    """
    Adds filename and line number to the builtin `print` statement.
    """
    def _link(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:

        info = getframeinfo(stack()[1][0])

        # Pad evenly up to n chars
        n = 32
        pad = (n - len(sep.join((f'{e}' for e in objects)))) * ' '

        count = perf_counter()

        global __prev_time
        diff = count - __prev_time
        __prev_time = count
        diff_str = f'+{diff:.3f}'

        # Make zeros stand out
        if diff_str == '+0.000':
            diff_str = '+0    '

        # Prepend time and append link to print output
        __print_orig(f'{count:>8.3f} {diff_str:>9}   ', *objects, f'{pad} File \"{info.filename}\", line {info.lineno}',
                     sep=sep, end=end, file=file, flush=flush)

    builtins.print = _link


def unlink():
    """
    Undoes a call to link.
    """
    builtins.print = __print_orig


def suppress() -> None:
    def _suppress(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
        pass

    builtins.print = _suppress

import sys
import builtins
from inspect import getframeinfo, stack


_print = print


def _link(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) -> None:
    """
    Like the builtin `print` but with the filename and line number appended.
    """
    info = getframeinfo(stack()[1][0])

    # Pad evenly up to n chars
    n = 24
    pad = (n - len(sep.join((f'{e}' for e in objects)))) * ' '

    _print(*objects, f'{pad} File \"{info.filename}\", line {info.lineno}', sep=sep, end=end, file=file, flush=flush)


builtins.print = _link

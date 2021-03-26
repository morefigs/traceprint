from inspect import getframeinfo, stack
    

_print = print


def _link(*values: object,
          sep: Optional[str] = ' ',
          end: Optional[str] = '\n',
          file: Optional[SupportsWrite[str]] = sys.stdout,
          flush: Optional[bool] = False) -> None:
    caller = getframeinfo(stack()[1][0])
    _print(f'{text}       \tFile \"{caller.filename}\", line {caller.lineno}')


print = _link

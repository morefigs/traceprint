_print = print


def null(*args):
    pass


def _print_link(text):
    from inspect import getframeinfo, stack
    caller = getframeinfo(stack()[1][0])
    _print(f'{text}       \tFile \"{caller.filename}\", line {caller.lineno}')


def enable():
    global print
    print = _print_link


def suppress():
    global print
    print = null

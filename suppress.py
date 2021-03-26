import builtins


_print = print


def _suppress(*args, **kwargs) -> None:
    pass


builtins.print = _suppress

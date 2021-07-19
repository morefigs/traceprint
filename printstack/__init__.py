"""
printstack is a Python package that adds stack trace links to the builtin print function, so that editors such as
PyCharm can link you to the source of the print call.
"""

from .printstack import set_options, enable, disable, suppress


enable()

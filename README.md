# traceprint

_"I never use the print statement for debugging, but when I do I use traceprint."_ - Guido van Rossum.

`traceprint` is a Python package that adds stack trace links to the builtin print function, so that editors such as PyCharm can link to the source of the `print` call.

![](examples/example.png?raw=true)

## Installation

[![Downloads](https://pepy.tech/badge/traceprint)](https://pepy.tech/project/traceprint)

    pip install traceprint

## Usage

Simply import `traceprint` to enhance the `print` function:

```python
import traceprint

print("Hello world")

# Hello world              File "/dev/traceprint/examples/example.py", line 3, in <module>
```

Some options are configurable:

```python
import traceprint
traceprint.set_options(
    limit=1,                        # Limit depth of stack entries displayed, if limit is above zero
    right_align=40,                 # Number of characters to offset the link text to the right by
    flatten_recurring_outputs=True  # Display recurring outputs (e.g. from a loop) inline instead of multiline
)
```

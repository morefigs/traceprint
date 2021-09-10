# printstack
[![pip installs](https://pepy.tech/badge/printstack)](https://pepy.tech/project/printstack)

## Description

`printstack` is a Python package that adds stack trace links to the builtin print function, so that editors such as PyCharm can link to the source of the `print` call.

![](examples/example.png?raw=true)

## Installation

    pip install printstack

## Usage

Simply import `printstack` to enhance the `print` function:

    import printstack

    print("Hello world")
    
    # Hello world              File "/dev/printstack/examples/example.py", line 3, in <module>

<br>Some options are configurable:

    import printstack; printstack.set_options(
        limit=1,                        # limit depth of stack entries displayed, if limit is above zero
        right_align=40,                 # number of characters to offset the link text to the right by
        flatten_recurring_outputs=True  # display recurring outputs (e.g. from a loop) inline instead of multiline
    )

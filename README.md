# printstack

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

    import printstack
    printstack.set_options(
        limit=1,        # limits the depth of the stack links, 0 for no limit
        right_align=40  # adjusts the right align width of the stack link
    )

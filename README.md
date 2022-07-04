# traceprint
[![pip installs](https://static.pepy.tech/personalized-badge/printstack?period=total&units=international_system&left_color=grey&right_color=blue&left_text=pip%20installs)](https://pepy.tech/project/printstack)

`traceprint` is a Python package that adds stack trace links to the builtin print function, so that editors such as PyCharm can link to the source of the `print` call.

![](examples/example.png?raw=true)

## Installation

    pip install traceprint

## Usage

Simply import `traceprint` to enhance the `print` function:

    import traceprint

    print("Hello world")
    
    # Hello world              File "/dev/traceprint/examples/example.py", line 3, in <module>

<br>Some options are configurable:

    import traceprint
    traceprint.set_options(
        limit=1,                        # Limit depth of stack entries displayed, if limit is above zero
        right_align=40,                 # Number of characters to offset the link text to the right by
        flatten_recurring_outputs=True  # Display recurring outputs (e.g. from a loop) inline instead of multiline
    )

# printstack

## Description

`printstack` adds stack trace links to the builtin print function, so that editors such as PyCharm can link you to the source of the `print` call.

![](examples/example.png?raw=true)

## Installation

    pip install printstack

## Usage

Simply import `printstack` to enhance the `print` function:

    import printstack

    print("Hello world")

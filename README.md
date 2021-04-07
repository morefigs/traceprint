# printhack

## Description

`printhack` appends a filename and line number to the output of the `print` function, so that editors such as PyCharm can link to the source of the `print` call.

![](examples/example.png?raw=true)

## Installation

Install via:

    pip install printhack

## Usage

Simply add the following code to your script to enhance your `print` statement:

    from printhack import link
    link()

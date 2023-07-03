# Clipette
Python clipboard utility that works natively on python with its inbuilt modules to exchange data with the windows clipboard. Designed specifically to be used for Blender (for [ImagePaste](https://github.com/Yeetus3141/ImagePaste)).

**-WORK IN PROGRESS-**

## Usage
Must call `open_clipboard()` before using any clipboard function which returns 0 on failure.
Should call `empty_clipboard()` before setting any data to clipboard.
Must call `close_clipboard()` at the end or other applications may not be able to access the clipboard.

Example (to get unicode text from clipboard):
```
import clipette

if clipette.open_clipboard():
    text = clipette.get_UNICODETEXT()
    print(text)
    clipette.close_clipboard()
```

# Clipette
Python clipboard utility that works natively on python to 
exchange data with the windows clipboard through the win32 API.
Is designed particularly to work properly with different image formats
(for [ImagePaste](https://github.com/Yeetus3141/ImagePaste)) 
but also works with other clipboard formats.


## Documentation
Please refer to [the docs](https://b-init.github.io/clipette/) for function descriptions and more details.

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

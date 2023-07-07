# Clipette
Python clipboard utility that works natively on python to 
exchange data with the windows clipboard through the win32 API.
Is designed particularly to work properly with different image formats
(for [ImagePaste](https://github.com/Yeetus3141/ImagePaste)) 
but also works with other clipboard formats.


## Documentation
Please refer to [the docs](https://b-init.github.io/clipette/) for function descriptions, references and more details.

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
For more examples, refer to [the docs](https://b-init.github.io/clipette/)

## Todo
- Implement [`GetLastError`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to enable easier debugging of win32 functions.
- Add support for more Image Formats like `psd` or maybe `jpeg`.

## Why?
While working on [ImagePaste](https://github.com/Yeetus3141/ImagePaste), I needed a way to quickly and 
reliably exchange image data with the clipboard which turned out to be a problem on Windows where
the clipboard image standard is kind of a mess.
I tried [Pillow](https://pypi.org/project/Pillow/) and shell scripts but neither worked fastly enough or with the required image formats
so I ended up developing this module. 


# Clipette
Python clipboard utility that works natively on python to 
exchange data with the windows clipboard through the win32 API.
Is designed particularly to work properly with different image formats
(for [ImagePaste](https://github.com/Yeetus3141/ImagePaste)) 
but also works with other clipboard formats.


## Documentation
Please refer to [the docs](https://b-init.github.io/clipette/) for function descriptions, references and more details.
Refer to the official [win32 API docs](https://learn.microsoft.com/en-us/windows/win32/dataxchg/clipboard) for documentation on win32 clipboard API.

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

## Contributing

It will be great if you have an idea and turn it into visible. Tell us how amazing they are by [suggesting a feature][link_issues], or you can make it yourself by creating [a pull request][link_pulls]. And if you encounter a problem, let us know by [opening an issue][link_issues]. But before doing anything, let's take a look at [our contributing guide](.github/CONTRIBUTING.md), it will show you how to start with all of that.

## Todo
- Implement [`GetLastError`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) to enable easier debugging of win32 functions.
- Add support for more Image Formats like `psd` or `jpeg`.
- Add tests.

## Why?
While working on [ImagePaste](https://github.com/Yeetus3141/ImagePaste), I needed a way to quickly and 
reliably exchange image data with the clipboard which turned out to be a problem on Windows where
the clipboard image standard is kind of a mess.
I tried [Pillow](https://pypi.org/project/Pillow/) and shell scripts but neither worked fastly enough or with the required image formats
so I ended up developing this module. 


[link_issues]: https://github.com/b-init/clipette/issues
[link_pulls]: https://github.com/b-init/clipette/pulls
[link_docs]: https://b-init.github.io/clipette/
[link_docs_md]: https://github.com/b-init/clipette/tree/main/docs
[link_discuss]: https://github.com/b-init/clipette/discussions
[link_references]: https://b-init.github.io/clipette/references/


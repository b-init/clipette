# Usage Examples

## set text

```py
import clipette
if clipette.open_clipboard():
    clipette.empty_cliboard()
    clipette.set_UNICODETEXT("<some text>")
    clipette.close_clipboard()
```



&nbsp;
## get PNG

```py
import clipette
if clipette.open_clipboard():
    clipette.get_PNG("<filepath to save into>", "<filename>")
    clipette.close_clipboard()
```
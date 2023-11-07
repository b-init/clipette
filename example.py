import clipette
if clipette.open_clipboard():
    clipette.empty_cliboard()
    clipette.set_UNICODETEXT("<some text>")
    clipette.close_clipboard()

# safe clipboard
with clipette.clipboard():
    clipette.empty_cliboard()
    clipette.set_UNICODETEXT("<some text>")

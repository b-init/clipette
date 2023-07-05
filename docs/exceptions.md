<a id="clipette.ClipetteWin32ClipboardError"></a>

## ClipetteWin32ClipboardError

```python
class ClipetteWin32ClipboardError(Exception)
```

Raised when the clipboard is inaccessible or clipette is unable to
exchange given data with the clipboard.

<a id="clipette.ClipetteWin32MemoryError"></a>


&nbsp;
## ClipetteWin32MemoryError

```python
class ClipetteWin32MemoryError(Exception)
```

Raised when clipette is unable to perform memory operations through
`kernel32` api.
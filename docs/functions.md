## open\_clipboard

```python
def open_clipboard() -> int
```

Opens clipboard. Must be called before any action in performed.

**^^Returns^^**:

`int`: 0 if function fails, 1 otherwise.

<a id="clipette.close_clipboard"></a>


&nbsp;
## close\_clipboard

```python
def close_clipboard() -> int
```

Closes clipboard. Must be called after all actions are performed.

**^^Returns^^**:

`int`: 0 if function fails, 1 otherwise.

<a id="clipette.empty_clipboard"></a>



&nbsp;
## empty\_clipboard

```python
def empty_clipboard() -> int
```

Empties clipboard. Should be called before any setter actions.

**^^Returns^^**:

0 if function fails, 1 otherwise.

<a id="clipette.get_UNICODETEXT"></a>


&nbsp;
## get\_UNICODETEXT

```python
def get_UNICODETEXT() -> str
```

Gets text from clipboard as a string.

**^^Returns^^**:

`str`: text grabbed from clipboard.

<a id="clipette.set_UNICODETEXT"></a>


&nbsp;
## set\_UNICODETEXT

```python
def set_UNICODETEXT(text: str) -> bool
```

Sets text to clipboard in CF_UNICODETEXT format.

**^^Arguments^^**:

- `text` (`str`): text to set to clipboard.

**^^Returns^^**:

`bool`: True if function succeeds.

<a id="clipette.get_FILEPATHS"></a>


&nbsp;
## get\_FILEPATHS

```python
def get_FILEPATHS() -> list[str]
```

Gets list of filepaths from clipboard. 

**^^Returns^^**:

`list[str]`: list of filepaths.

<a id="clipette.get_DIB"></a>


&nbsp;
## get\_DIB

```python
def get_DIB(filepath: str = '', filename: str = 'bitmap') -> str
```

Gets image from clipboard as a bitmap and saves to *filepath* as *filename.bmp*.

**^^Arguments^^**:

- `filepath` (`str`): filepath to save image into.
- `filename` (`str`): filename of the image.

**^^Returns^^**:

`str`: full filepath of the saved image.

<a id="clipette.get_DIBV5"></a>


&nbsp;
## get\_DIBV5

```python
def get_DIBV5(filepath: str = '', filename: str = 'bitmapV5') -> str
```

Gets image from clipboard as a bitmapV5 and saves to *filepath* as *filename.bmp*.

**^^Arguments^^**:

- `filepath` (`str`): filepath to save image into.
- `filename` (`str`): filename of the image.

**^^Returns^^**:

`str`: full filepath of the saved image.

<a id="clipette.get_PNG"></a>


&nbsp;
## get\_PNG

```python
def get_PNG(filepath: str = '', filename: str = 'PNG') -> str
```

Gets image in ``PNG`` or ``image/png`` format from clipboard and saves to *filepath* as *filename.png*.

**^^Arguments^^**:

- `filepath` (`str`): filepath to save image into.
- `filename` (`str`): filename of the image.

**^^Returns^^**:

`str`: full filepath of the saved image.

<a id="clipette.set_DIB"></a>


&nbsp;
## set\_DIB

```python
def set_DIB(src_bmp: str) -> bool
```

Sets given bitmap image to clipboard in ``CF_DIB`` or ``CF_DIBV5`` format according to the image.

**^^Arguments^^**:

- `src_bmp` (`str`): full filepath of source image.

**^^Returns^^**:

`bool`: True if function succeeds.

<a id="clipette.set_PNG"></a>


&nbsp;
## set\_PNG

```python
def set_PNG(src_png: str) -> bool
```

Sets source PNG image to clipboard in ``PNG`` format.

**^^Arguments^^**:

- `src_png` (`str`): full filepath of source image.

**^^Returns^^**:

`bool`: True if function succeeds.

<a id="clipette.is_format_available"></a>


&nbsp;
## is\_format\_available

```python
def is_format_available(format_id: int) -> bool
```

Checks whether specified format is currently available on the clipboard.

**^^Arguments^^**:

- `format_id` (`int`): id of format to check for.

**^^Returns^^**:

`bool`: True if specified format is available, False otherwise.

<a id="clipette.get_available_formats"></a>


&nbsp;
## get\_available\_formats

```python
def get_available_formats(buffer_size: int = 32) -> dict[int, str]
```

Gets a dict of all the currently available formats on the clipboard.

**^^Arguments^^**:

- `buffer_size` (`int`): (optional) buffer size to store name of each format in.

**^^Returns^^**:

`dict[int, str]`: a dict {format_id : format_name} of all available formats.

<a id="clipette.get_image"></a>


&nbsp;
## get\_image

```python
def get_image(filepath: str = '', filename: str = 'image') -> str
```

Gets image from clipboard in a format according to a priority list (``PNG`` > ``DIBV5`` > ``DIB``).

**^^Arguments^^**:

- `filepath` (`str`): filepath to save image into.
- `filename` (`str`): filename of the image.

**^^Returns^^**:

`str`: full filepath of the saved image.

<a id="clipette.set_image"></a>


&nbsp;
## set\_image

```python
def set_image(src_img: str) -> bool
```

(NOT FULLY IMPLEMENTED) Sets source image to clipboard in multiple formats (``PNG``, ``DIB``).

**^^Arguments^^**:

- `src_img` (`str`): full filepath of source image.

**^^Returns^^**:

`bool`: True if function succeeds.

# TPC3

**Author**: [**A102131** Oleksii Tantsura](https://www.github.com/Ol3ksii)

**Date**: 2025-03-02

## Summary

In this task (TPC3), the goal is to develop a Python program that converts Markdown syntax into HTML.

The program must process Markdown input and correctly convert the following elements:

- **Headers**: Lines starting with `#`, `##`, or `###` should be converted into `<h1>`, `<h2>`, or `<h3>` tags.
- **Bold text**: Text enclosed in `**` should be wrapped in `<b>`.
- **Italic text**: Text enclosed in `*` should be wrapped in `<i>`.
- **Numbered lists**: Recognized patterns like `1. Item` should be transformed into `<ol>` and `<li>` elements.
- **Links**: `[text](URL)` should be transformed into `<a href="URL">text</a>`.
- **Images**: `![alt text](image URL)` should be transformed into `<img src="image URL" alt="alt text"/>`.

## Results

The program is executed from the command line and expects Markdown input via standard input. Example usage:

```bash
python3 TPC3.py < example.md
```

## example.md:
```
# Example Header

This is a **bold** and *italic* text.

1. First item
2. Second item
3. Third item

Check this link: [Example](http://example.com)

![Example Image](http://example.com/image.jpg)
```

After execution, the user is presented with the output in the following order:

```bash
<h1>Example Header</h1>

This is a <b>bold</b> and <i>italic</i> text.

<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ol>

Check this link: <a href="http://example.com">Example</a>

<img src="http://example.com/image.jpg" alt="Example Image"/>
```

- **1** (Headers conversion):
    ```
    # Header 1
    ## Header 2
    ### Header 3
    ```
    Output:
    ```
    <h1>Header 1</h1>
    <h2>Header 2</h2>
    <h3>Header 3</h3>
    ```

- **2** (Bold and Italic conversion):
    ```
    This is **bold** and *italic* text.
    ```
    Output:
    ```
    This is <b>bold</b> and <i>italic</i> text.
    ```

- **3** (Numbered list conversion):
    ```
    1. First item
    2. Second item
    3. Third item
    ```
    Output:
    ```
    <ol>
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
    </ol>
    ```

- **4** (Link conversion):
    ```
    [Visit here](http://example.com)
    ```
    Output:
    ```
    <a href="http://example.com">Visit here</a>
    ```

- **5** (Image conversion):
    ```
    ![Example Image](http://example.com/image.jpg)
    ```
    Output:
    ```
    <img src="http://example.com/image.jpg" alt="Example Image"/>
    ```

## Conclusion

The Python program successfully converts Markdown syntax into HTML while following the specified constraints. 
The implementation ensures structured transformation of headers, formatting elements, lists, links, and images, providing a functional Markdown-to-HTML converter.

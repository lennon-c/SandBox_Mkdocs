
## code blocks  
Plain code block
```python
import sys 

for path in sys.path:
    print(path)
```
  

## admonition or callout

[see the documentation](https://squidfunk.github.io/mkdocs-material/reference/admonitions/#usage)


!!! note "This is the admonition title of a `note`"
    body 

```md
!!! note "This is the admonition title of a `note`"
    body 

```

!!! info "this is a `info` admonition"
    This is the admonition body

??? note "collapsable admonition - closed by defualt"
    you can close me.

???+ note "collapsable admonition - opened by defualt"
    you can close me.


## grid cards 

[see docs](https://squidfunk.github.io/mkdocs-material/reference/grids/?h=grid#using-card-grids)
cards are not displayed in editor

<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>

## linenums 
For showing line numbers in code and for highlighting code lines
[See docs](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/#adding-line-numbers)
lines colors and numbers are not rendered in editor

``` py linenums="1"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

``` py hl_lines="2 3"
def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items) - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
```

## tabbed 


[see docs](https://squidfunk.github.io/mkdocs-material/reference/content-tabs/#grouping-code-blocks)

=== "Source"

    ```python 
    from sandbox.calculations import Two_numbers

    nums = Two_numbers(4, 2)
    print(f'{nums.add()=}')
    ```

=== "Result"

    ```
    nums.add()=6.0
    ```

rendered from this markdown code:
````md
=== "Source"

    ```python 
    from sandbox.calculations import Two_numbers

    nums = Two_numbers(4, 2)
    print(f'{nums.add()=}')
    ```

=== "Result"

    ```
    nums.add()=6.0
    ```
````
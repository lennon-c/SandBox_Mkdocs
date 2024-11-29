This allows for interactive Python execution. To use it, you need to install `markdown-exec`. [See the documentation](https://pawamoy.github.io/markdown-exec/usage/pyodide/) for more information.

It is very cool, but it has several limitations:

- While it should work well for most built-in Python modules, it does not support all of them. For instance, there is no support for `tkinter`!
- You can install packages from PyPi, but only pure Python modules are supported.
- There is support for some non-pure Python packages, such as `numpy`.

```pyodide
import os, sys 
print('cwd',os.getcwd())

for path in sys.path:
    print(path)
```

which was run using: 
````md
```pyodide
import os, sys 
print('cwd',os.getcwd())

for path in sys.path:
    print(path)
```
````


## Packages of Project Hosted in GitHub

This will not work, pyodide cannot access your documentation, nor the installs at deployment.

```pyodide
from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
```

This is a not very elegant solution, but it works:

```pyodide   install="pyodide-importer"

from pyodide_importer import register_hook
register_hook("https://raw.githubusercontent.com/lennon-c/SandBox_Mkdocs/main/")

from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
 
```
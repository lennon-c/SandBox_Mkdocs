This allows for interactive python. 
It requires installing `markdown-exec`. [See the documentation](https://pawamoy.github.io/markdown-exec/usage/pyodide/)

It is very cool, but has several limitations: 

- Although it should work well for most of the python built-in modules, it does not support all of of them, for instance, there is no support for `tkinter`! 
- You can install from PyPi, but only pure python modules.
- There is support for some non pure python packages such as `numpy` 

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


## packages of project hosted in GitHub

this will not work, pyodide cannot access your documentation, nor the installs at deployment.

```pyodide
from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
```

There is a not that optimal solution: 

```pyodide   install="pyodide-importer"

from pyodide_importer import register_hook
register_hook("https://raw.githubusercontent.com/lennon-c/SandBox_Mkdocs/main/")

from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
 
```

This will work only for projects that are pure python and relies on only pure python packages! 

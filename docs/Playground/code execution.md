This can be used either for automating (just executing without showing source code) or in tutorials (executing and showing both the results and the source code).


This requires installing `markdown-exec`. [See the documentation](https://pawamoy.github.io/markdown-exec/usage/)


## Showing source code and results
###  tabbed
```python exec="true" source="tabbed-left" result="pycon"
import os, sys 
print('cwd',os.getcwd())

for path in sys.path:
    print(path)
```
which was generated by using the markdown code: 

````markdown  
```python exec="true" source="tabbed-left" result="pycon"
import os, sys 
print('cwd',os.getcwd())

for path in sys.path:
    print(path)
```
````

### source code above

```python exec="true" source="above" result="pycon"
import os
print(os.getcwd())
```

which was run by using: 
````md
```python exec="true" source="above" result="pycon"
import os
print(os.getcwd())
```
````

## running own hosted module in GitHub
Here, a python script importing a class from this project module `sandbox.calculations.Two_numbers`.

```python exec="true" source="tabbed-left" result="pycon"  
from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
```

which was run using this markdown code:

````md
```python exec="true" source="tabbed-left" result="pycon"  
from sandbox.calculations import Two_numbers

nums = Two_numbers(4, 2)
print(f'{nums.add()=}')
```
````

My first trial did only work  partially:

- It was actually working for development `mkdocs serve`, but not in production `mkdocs gh-deploy`.

Solution:

-  I modified the `ci.yml` file for GitHub workflows, so that my package can be installed at deployment. Adding this line:

```yml title="ci.yml"
    - run: pip install git+https://github.com/lennon-c/SandBox_Mkdocs.git
```

- Since it requires an install, one has to setup the source code as a package.
    - I am using poetry, so I just had to make sure to add the required documentation for packaging, but there was no need for a package wheel! 

This is really cool, one can thus use `markdown-exec` to showcase own projects that are hosted in GitHub.
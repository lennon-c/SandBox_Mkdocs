Playground for testing options, plugins, formatting of:

- mkdocs
- mkdocs-material 
- mkdocstrings-python
- markdown-exec[ansi]
- mkdocs-open-in-new-tab
- mkdocs-callouts (disabled, used to allow Obsidian syntax for callouts)

Just a set of personal tests, to see what works and what does not. 

Showcased in this project's [documentation](https://lennon-c.github.io/SandBox_Mkdocs/)



## Adding python exec in Readme

This code block is shown but not executed in README.md, while it is executed in the documentation site, where only the result is shown.

```python exec="true"  
print('I am in README.md and in the Home page')
```
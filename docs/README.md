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

I do not use an `index.md` file as the entry point for the website. Instead, I use a `README.md` file, which serves as both the homepage of the site and the documentation on GitHub, reducing boilerplate.

However, some markup features are not supported when the `README.md` file is viewed directly on GitHub.

For example, code execution does not work on GitHub:

The following code block is displayed but not executed on GitHub, whereas it is executed on the documentation site.


```python exec="true"  
print('***I am in README.md and in the Home page***')
```


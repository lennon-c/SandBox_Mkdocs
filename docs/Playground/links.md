Linking things can be tricky...


## Linking Other Pages in the Project

It is recommended to use [relative paths](https://www.mkdocs.org/user-guide/writing-your-docs/#linking-to-pages) when linking to other pages in the project. The paths should be relative to the location of the current file containing the link and should point to `.md` files.

For instance: 

Go to [Home Page](../README.md)

```md
Go to [Home Page](../README.md)
```
### Links in the `README.md` File

I do not use an `index.md` file as the entry point for the website. Instead, I use a `README.md` file, which serves both as the homepage of the site and as the documentation on GitHub, reducing boilerplate.

However, this approach has the following drawback:

- Links using relative paths will not work when the `README.md` file is accessed directly on GitHub.
    - To address this, use external links with a URL address in production.

Go to [Home Page](https://lennon-c.github.io/SandBox_Mkdocs/)

```md
Go to [Home Page](https://lennon-c.github.io/SandBox_Mkdocs/)
```

## Link to a Docstring Object:

Here, one uses square brackets and employs dot notation to link to objects within the package.

link to class `sandbox.calculations.Two_numbers`

- [link to class][sandbox.calculations.Two_numbers]

```md 
- [link to class][sandbox.calculations.Two_numbers]
```
 
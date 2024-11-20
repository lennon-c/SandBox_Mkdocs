With GitHub Actions, you can deploy the documentation site each time changes are pushed to the remote repository.

Create a file in `.github\workflows\ci.yaml` (in your local repository) with the following text, then commit and push the changes.

??? note  "ci.yaml"
    ```yaml title="ci.yaml"
    name: ci 
    on:
      push:
        branches:
          # - master 
          - main
    permissions:
      contents: write
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Configure Git Credentials
            run: |
              git config user.name github-actions[bot]
              git config user.email 41898282+github-actions[bot]@users.noreply.github.com
          - uses: actions/setup-python@v5
            with:
              python-version: 3.x
          - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
          - uses: actions/cache@v4
            with:
              key: mkdocs-material-${{ env.cache_id }}
              path: .cache
              restore-keys: |
                mkdocs-material-
          - run: pip install mkdocs-material 
          - run: pip install mkdocstrings-python
          - run: pip install markdown-exec[ansi]
          - run: pip install mkdocs-open-in-new-tab
          - run: pip install git+https://github.com/lennon-c/SandBox_Mkdocs.git
          - run: mkdocs gh-deploy --force
    ```
## With Code Execution (markdown-exec)

To execute code importing your own package, or any package hosted on GitHub, you first need to add the instruction to install it:

```yaml title="ci.yaml"
          - run: pip install git+https://github.com/user/package.git
```

For this example, I used: `run: pip install git+https://github.com/lennon-c/SandBox_Mkdocs.git`.

### Problems
- If your executed code fetches data that is not contained in the package but resides only on your computer, the code will break during deployment.
    - By contrast, if you deploy manually (e.g., using `mkdocs gh-deploy`), the code will still work.

- This could be problematic if the data is large, or if you do not want to load it or make it publicly available.
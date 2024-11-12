---
title: Some samples of formatting 
---

```python exec='1'
from pathlib import Path
path =  Path('_file_').parent

for p in (path / 'docs'/ 'Playground').iterdir():
    if  p.stem == 'index':
        continue
    print(f'- [{p.stem }]({p.stem })')
```



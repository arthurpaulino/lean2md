# lean2md

A Python package that converts Lean files into markdown.

1. Install it with `$ pip install lean2md`
2. Use it with `$ python -m lean2md <lean_src_dir> <md_tgt_dir>`

For a Lean file (inside `<lean_src_dir>`) like this:

```lean
import Mathlib.Tactic --#

namespace Sample --#

/-!
# Title

etc etc.
-/

/- Some doc -/
def one := 1

/-!
## Subtopic

* Item 1
* Item 2
-/

def two := 2

end Sample --#
```

A markdown file like this one will be created (inside `<md_tgt_dir>`):

````markdown
# Title

etc etc.

Some doc

```lean
def one := 1
```

## Subtopic

* Item 1
* Item 2

```lean
def two := 2
```
````

Note that lines ending in `--#` (without trailing white spaces) are ignored by lean2md.

# cv

Bespoke CV generator

### Setup

#### Requirements

- uv (python 3.12)
- weasyprint

#### Install dependencies

First, install the weasyprint system dependency:

```bash
$ sudo apt install weasyprint
```

Then, install Python depdencies with `uv`:

```bash
$ uv sync
```

### CV generation

Adjust values in _contents.yml_ and generate outputs:

```bash
$ python -m cv.generate
```

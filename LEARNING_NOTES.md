# Python Learning Notes

Personal log while re-exploring old university Python material in `university/`.
Newest entries at the bottom.

## 2026-09-25 — Project tooling (venv, .idea, dependency manifests)

**`venv/`** — a Python virtual environment: an isolated copy of the interpreter
reference + installed packages for one project, separate from the system Python.
Created with `python3.11 -m venv venv`, activated with `source venv/bin/activate`.
Disposable — regenerate it any time, so it's gitignored.

**`.idea/`** — PyCharm's per-project settings folder (run configs, code style,
workspace state). Machine/IDE-specific, also gitignored.

**Comparison to JS/TS tooling:**

| Python | JS/TS | Notes |
|---|---|---|
| `venv/` | `node_modules/` | `venv` also pins the interpreter, not just packages |
| `pyproject.toml` | `package.json` | modern standard (PEP 621) |
| `requirements.txt` | — | older/simpler flat dependency list, no lock/manifest split |
| `poetry.lock` / `uv.lock` / `Pipfile.lock` | `package-lock.json` | no single standard — varies by tool |

Plain `venv` does **not** read a manifest to pick/install a Python version —
you point it at whatever interpreter you already have. `requires-python` in
`pyproject.toml` is just metadata unless a smarter tool enforces it.

**`uv`** is the closest thing to `npm install` for Python: reads
`pyproject.toml` + `uv.lock`, downloads the pinned Python version if missing,
creates the venv, installs everything.

```bash
uv init myproject      # like `npm init` → creates pyproject.toml
uv add requests        # like `npm install requests` → updates pyproject.toml + uv.lock
uv sync                # ensures venv matches the manifest, like `npm install`
```

Plain pip/venv equivalent (no manifest-driven Python version):

```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**Repo hygiene while setting this repo up:** added a root `.gitignore`
(`venv/`, `__pycache__/`, `.idea/`, `.DS_Store`, `.env`), and removed two
nested `.git` folders found under `university/pythonWSEI` and
`university/projektUczenieMaszynowe2024` — they were separate repos
accidentally nested inside this one, which would have made `git add` only
track empty placeholder entries for their files instead of the real content.

## 2026-09-25 — `zad1.py` (university/pythonWSEI/pythonExercises)

```python
import time

name = input("Podaj imie: ")
age = input("Podaj wiek: ")

try:
    age = int(age)
    ...
    name_as_list = list(name)
    ...
    current_time = time.gmtime()
    current_year = current_time.tm_year
    year_of_birth = current_year - age
    ...
except ValueError:
    print('Podany wiek nie jest liczbą')
except Exception as e:
    print('Coś poszło nie tak')
```

Concepts covered:

- **`input()`** always returns a `str` — has to be explicitly converted
  (`int(age)`) before doing arithmetic on it.
- **`try` / `except`** with multiple `except` blocks: a specific exception
  (`ValueError`, raised by `int()` on a non-numeric string) is caught first,
  a generic `except Exception as e` catches anything else as a fallback.
  Python checks `except` clauses top to bottom and uses the first match.
- **`list("abc")`** on a string produces a list of its characters
  (`['a', 'b', 'c']`) — strings are iterable, so this works like any
  sequence-to-list conversion.
- **String concatenation with `+`** requires all operands to be `str`,
  hence the repeated `str(...)` wrapping around numbers.
- **`time.gmtime()`** returns a `struct_time` (UTC); `.tm_year` pulls the
  year field out of it — used here to derive an approximate birth year from
  the given age.

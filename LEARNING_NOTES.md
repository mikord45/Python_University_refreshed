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

## 2026-09-25 — `zad2.py` (university/pythonWSEI/pythonExercises)

Understood, no new concepts beyond `zad1.py`. Adds:

- **`float(money)`** — same idea as `int(age)`, converting input to a
  decimal number.
- **`if / elif / elif / else`** chain combining two conditions with `and`
  to cover all four combinations of age/money.
- **`round(value, 2)`** — rounds a float to 2 decimal places (money amounts).

## 2026-09-25 — `zad3.py` (university/pythonWSEI/pythonExercises)

```python
from enum import Enum

class Modes(Enum):
    MONTHLY = 'monthly'
    YEARLY = 'yearly'
```

New concepts:

- **`Enum`** (from the standard library `enum` module) — a base class
  designed to be subclassed for defining a fixed, closed set of named
  constants.
- **`class Modes(Enum):`** — ordinary Python inheritance (`class Child(Parent)`),
  same mechanism as any other subclass. Each `NAME = value` line inside is
  turned into a distinct singleton member (`Modes.MONTHLY`) by `Enum`'s
  metaclass, with `.name` (`'MONTHLY'`) and `.value` (`'monthly'`).
- **Why `Enum` over a plain class with class attributes:**
  - members compare by identity, not by their raw underlying value, so
    `Modes.MONTHLY == 'monthly'` is `False` — prevents accidental string
    typos/collisions matching where they shouldn't.
  - invalid lookups raise (`Modes('quarterly')` → `ValueError`) instead of
    silently doing nothing.
  - iterable/introspectable for free (`list(Modes)`, `.name`/`.value`).
  - signals intent: "this is a closed set of options," not arbitrary
    class-level storage.
- **Manually raising an exception:** `raise Exception(invalidValueMessage)`
  to reject an invalid input value, then in the generic
  `except Exception as e` handler, `str(e)` is compared against the known
  message to tell "an error I raised on purpose" apart from any other
  unexpected failure.
- **Augmented assignment (`income *= 12`)** — shorthand for
  `income = income * 12`, same idea as JS `*=`. Used here to convert a
  monthly income into a yearly one.

## 2026-09-25 — `zad4.py` (university/pythonWSEI/pythonExercises)

```python
products = products.split(",")
set_of_products = set()
for product in products:
    product_without_white_characters = product.strip()
    if(product_without_white_characters):
        set_of_products.add(product_without_white_characters)

dictionary_of_products = {}
for product in set_of_products:
    price = float(input('Podaj cenę ' + product + ": "))
    dictionary_of_products.update({product: price})

for name, price in dictionary_of_products.items():
    print(name + ":" + str(price))
```

New concepts:

- **`str.split(",")`** — splits a string into a list on a separator, like
  JS `.split(',')`.
- **`str.strip()`** — trims leading/trailing whitespace, like JS `.trim()`.
- **`set()` / `.add()`** — a set, equivalent to JS `Set()`, used here to
  dedupe product names before asking for prices.
- **`dict` (`{}`) vs JS `Map`/object:** Python's `dict` *behaves* like a JS
  `Map` (ordered key→value pairs, insertion order preserved, any hashable
  type — not just strings — can be a key) but *looks* like a JS object
  literal syntactically (`{}`, no separate `.set()`/`.get()` required,
  though `dict` does offer `.get()`/`.update()` as convenience methods).
  Key difference from `Map`: dict keys must be hashable (immutable-ish) —
  e.g. a `list` can't be a key, but a `tuple` can.
- **`dict.update({key: value})`** — merges another dict/mapping into this
  one; used here just to add a single pair (`d[key] = value` would've been
  the more idiomatic way for that specific case).
- **`dict.items()`** — iterate `(key, value)` pairs, unpacked directly into
  `name, price` in the `for` loop — like JS
  `for (const [name, price] of map.entries())`.
- **Truthiness check on a string** (`if(product_without_white_characters):`)
  — an empty string `''` is falsy, any non-empty string is truthy, so this
  reads as "if there's something left after stripping" without an explicit
  `!= ''` comparison. Same idea applies to other empty containers
  (`[]`, `{}`, `set()`) and to `0`/`None`.

## 2026-09-25 — `zad5.py` (university/pythonWSEI/pythonExercises)

```python
import math

def calculate_triangle_area(sideA, sideB, sideC):
    try:
        ...
        allSides = [sideALength, sideBLength, sideCLength]
        allSides.sort(reverse=True)
        if(allSides[0] >= allSides[1] + allSides[2]):
            return -1
        p = 0.5 * (sideALength + sideBLength + sideCLength)
        area = math.sqrt(p*((p - sideALength) * (p - sideBLength) * (p - sideCLength)))
        return float(area)
    except Exception as e:
        return -1
```

Understood, concepts:

- **`def function_name(params):`** — function definition, like JS
  `function calculate_triangle_area(sideA, sideB, sideC) {}`.
- **`import math`** — standard library module for math functions;
  `math.sqrt()` used here (Heron's formula for triangle area).
- **`list.sort(reverse=True)`** — in-place sort, descending; used to find
  the longest side to validate the triangle inequality.
- **Early `return -1`** as a sentinel/error value from inside a function,
  checked by the caller (`if triangleArea > 0`) instead of raising —
  an alternative error-handling style to the `raise`/`except` pattern seen
  in earlier exercises.
- **`except Exception as e: return -1`** — catching any error during
  parsing/calculation and converting it into the same sentinel value.

## 2026-09-25 — `zad5b.py` (university/pythonWSEI/pythonExercises)

```python
def calculate_roots_of_the_quadratic_equation(a, b, c):
    try:
        ...
        if(a_value == 0):
            return
        discriminant = b_value * b_value - (4 * a_value * c_value)
        if(discriminant < 0):
            return []
        ...
    except Exception as e:
        return
```

Understood, concepts:

- **Bare `return`** (no value) implicitly returns `None` — used here as a
  distinct sentinel ("invalid input") from `return []` ("valid input, but
  no real roots"). Two different falsy-ish results used to signal two
  different situations, distinguished by the caller via
  `if roots == None` / `elif len(roots) == 0`.
- **Returning a `list` of results** (`[first_root, second_root]`) from a
  function as a simple way to hand back a variable number of computed
  values (1 or 2 roots) without a dedicated data structure.
- Same overall shape as `zad5.py`: `try/except` wrapping parsing +
  calculation, `math.sqrt()`, results interpreted by the caller through a
  chain of `if/elif/else`.

## 2026-09-25 — `zad1.py` (university/pythonWSEI/pythonExercises2)

Script that copies `.jpg`/`.png` files from a few subfolders into one shared
`kopie` folder (renaming them to avoid clashes) and writes a `raport.txt`
listing the images found per folder. Lots of new stdlib usage:

- **`import os`** — filesystem paths/listing (`os.path.join`, `os.listdir`,
  `os.path.exists`, `os.makedirs`, `os.path.isdir`, `os.path.basename`,
  `os.path.dirname`, `os.path.abspath`, `os.path.splitext`).
- **`import shutil`** — higher-level file ops; `shutil.copy2(src, dest)`
  copies a file and preserves metadata (like timestamps).
- **`os.path.join(a, b, ...)`** — builds a path with correct separators,
  like Node's `path.join`.
- **`os.path.exists(path)` / `os.makedirs(path)`** — check for and create a
  folder (with any missing parents).
- **List comprehension with a filter:**
  `[f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.png'))]`
  — builds a filtered list in one line; equivalent to a `for` loop with an
  `if` + `.append()` inside.
- **`str.endswith((a, b))`** — accepts a tuple of options, checking
  "ends with a OR b" in one call.
- **f-strings** (`f"...{expr}..."`) — Python's template literals, like JS
  `` `...${expr}...` ``.
- **`os.path.basename(path)`** — last component of a path (folder/file
  name); **`os.path.dirname(path)`** — everything before it.
- **`enumerate(iterable)`** — loop giving both index and item
  (`for i, file in enumerate(files)`), like JS
  `.forEach((file, i) => ...)`.
- **`os.path.splitext(filename)`** — splits into `(name, extension)`, e.g.
  `('photo', '.JPG')`.
- **`with open(path, 'w') as report:`** — a **context manager**: opens the
  file and guarantees it's closed afterward, even on error. `'w'` = write
  mode (overwrites). `report.write(text)` writes without an automatic
  newline (unlike `print`).
- **`os.path.isdir(path)`** — check whether a path is a directory.
- **`value in some_list`** — membership check, like JS
  `some_list.includes(value)`.
- **`__file__`** — special variable holding the current script's path;
  combined with `os.path.abspath`/`os.path.dirname` to anchor paths to the
  script's own location regardless of the current working directory.
- **`if __name__ == "__main__":`** — standard entry-point guard.
  `__name__` is `"__main__"` when the file is run directly, but the
  module's name when it's imported elsewhere — so `main()` only runs on
  direct execution, not on import.

### Follow-up: tuples, and `__name__` on import

**Tuple** — an ordered, fixed-size collection like a list, but
**immutable** (can't be changed after creation): `t = (1, 2, 3)`;
`t[0] = 99` raises `TypeError`.

| | `list` | `tuple` |
|---|---|---|
| Syntax | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable? | Yes | No — fixed once created |
| Typical use | Grows/shrinks/changes | Fixed, often small/heterogeneous group (coords, one data row, multi-value return) |
| Hashable? | No — can't be a dict key/set member | Yes (if contents are hashable) — *can* be a dict key |

Already seen one in `zad1.py`: `f.lower().endswith(('.jpg', '.png'))` —
`('.jpg', '.png')` is a tuple of fixed options to check against.

A `dict` isn't really comparable to a tuple — a dict maps *keys* to values
(`{'name': 'Alice'}`), a tuple is just positional values with no keys
(`('Alice', 30)`). Tuple when position alone is enough; dict when you want
named fields.

**`__name__` on import** — every file gets `__name__` filled in
automatically: `"__main__"` when run directly, or the module's filename
(no `.py`) when imported.

```python
# greetings.py
print("name is:", __name__)

def hello():
    print("hello!")

if __name__ == "__main__":
    hello()
```

```bash
$ python greetings.py
name is: __main__
hello!
```

```python
# app.py
import greetings
greetings.hello()
```

```bash
$ python app.py
name is: greetings
hello!
```

The module's top-level code (the `print`) still runs once on import — but
`__name__` is `"greetings"` there, so the guarded `hello()` call inside
`if __name__ == "__main__":` does **not** auto-fire on import; `hello()`
only runs here because `app.py` called it explicitly. This is exactly why
`zad1.py` uses the guard: importing it to reuse a function like
`copy_and_rename_files()` won't also trigger the whole `main()` script.

## 2026-09-25 — `zad2.py` (university/pythonWSEI/pythonExercises2)

Reads SMTP config + a message from files and sends an email. Understood,
concepts for reference:

- **`import smtplib`** — standard library module for sending email via
  SMTP.
- **`with open(file_name, 'r') as file:`** — context manager in read mode.
- **`file.readlines()`** — reads all lines into a list of strings
  (including trailing `\n`s); combined with a list comprehension +
  `.strip()` to clean each line:
  `[line.strip() for line in lines]`.
- **`file.read()`** — reads the whole file as a single string.
- **Tuple/sequence unpacking:**
  `sender_email, password, smtp_server, smtp_port = config_data` — assigns
  each element of a 4-item list to a separate variable in one line.
- **Multi-line f-string body** built with explicit `\n` separators for an
  email's headers + content.
- **`smtplib.SMTP(...)`, `.starttls()`, `.login()`, `.sendmail()`,
  `.quit()`** — the SMTP client workflow: connect, upgrade to TLS,
  authenticate, send, close.
- **`try/except Exception as e` with `f"...{e}"`** — same error-handling
  shape as earlier exercises, formatting the caught exception into the
  message via an f-string instead of `str(e)` concatenation.

## 2026-09-25 — `zad3.py` (university/pythonWSEI/pythonExercises2)

For each month of a given year, finds the last weekday (Mon–Fri) of that
month — e.g. for a "payday is the last business day of the month" style
calculation. Understood, concepts for reference:

- **`import calendar`** / **`import datetime`** — standard library modules
  for calendar math and date objects.
- **`calendar.monthrange(year, month)`** — returns
  `(weekday of first day, number of days in month)`; `[1]` grabs the day
  count (last calendar day of the month).
- **`datetime.date(year, month, day)`** — constructs a date object.
- **`.weekday()`** — returns the day of week as an int (Monday=0 ... Sunday=6).
- **`calendar.SATURDAY` / `calendar.SUNDAY`** — named constants for those
  weekday ints (5 and 6), used instead of magic numbers.
- **`in [a, b]`** — membership check against a list of two options, same
  idea as `str.endswith((a, b))`/`value in some_list` seen earlier.
- **`while` loop decrementing a value** (`last_day -= 1`) — steps
  backward from month-end day by day until landing on a weekday.
- **`.strftime("%d.%m.%Y")`** / **`.strftime("%B")`** — formats a date
  object into a string; `%B` gives the full month name.
- **`range(1, 13)`** — loop over months 1–12 (`range` end is exclusive).
- Same `if __name__ == "__main__": main()` entry-point guard as
  `pythonExercises2/zad1.py`.

## 2026-09-25 — `zad4.py` (university/pythonWSEI/pythonExercises2)

Reads a CSV of Lego sets, counts/aggregates sets from a given year, and
opens a random matching set's image in a browser. Understood, concepts for
reference:

- **`import csv` / `random` / `webbrowser` / `statistics`** — four
  standard library modules used together here.
- **`csv.DictReader(csvfile)`** — wraps an open CSV file and, while
  iterated, turns each row into a `dict` keyed by the header row's column
  names (e.g. `row['year']`, `row['num_parts']`) instead of a plain
  positional list like `csv.reader` would give.
  - `reader` itself is a `csv.DictReader` **object** — an **iterator**,
    not a list of dicts. Each loop step reads the next line from the file
    and converts *that row* into a dict on the spot (lazy, not all loaded
    upfront).
  - Every value comes back as a `str`, even numeric columns — hence
    `int(row['year'])`, `int(row['num_parts'])`.
  - Being an iterator over an open file, it can only be consumed **once**;
    to scan the file a second time, `zad4.py` reopens it with a fresh
    `with open(...)` + a new `DictReader`.
- **`open(csv_path, newline='', encoding='utf-8')`** — `newline=''` is the
  recommended flag when reading CSVs in Python (avoids double-handling of
  line endings); `encoding='utf-8'` ensures non-ASCII characters read
  correctly.
- **Returning a tuple of two values** (`return number_of_sets,
  numbers_of_elements_per_set`) and **unpacking it** at the call site
  (`number_of_sets, numbers_of_elements_per_set = readDataFromCsV(...)`) —
  same pattern as the config unpacking in `pythonExercises2/zad2.py`.
- **Bare `except:`** (no exception type) — catches anything, even broader
  than `except Exception as e`; used here for the year-input validation.
- **Truthiness check on a list** (`if numbers_of_elements_per_set:`) —
  same idea as the string truthiness check from `pythonExercises/zad4.py`,
  here skipping the stats block if the list is empty.
- **`statistics.mean()` / `statistics.median()`** — average and median of
  a list of numbers, no manual calculation needed.
- **List comprehension with a filter, then `random.choice(...)`:**
  `random.choice([row for row in reader if int(row['year']) == year_to_search])`
  — builds a filtered list of matching rows (forcing the lazy `reader`
  into an actual list, since `random.choice` needs something indexable),
  then picks one at random.
- **`webbrowser.open(url)`** — opens a URL in the system's default web
  browser.

## 2026-09-25 — `zad1.py` (university/pythonWSEI/pythonExercises3)

Three classes (`Triangle`, `Rectangle`, `Circle`), each validating its own
inputs and exposing area/perimeter/name methods. First OOP-heavy exercise.

```python
class Triangle:
    def __init__(self, a, b, c):
        self.name = "Trójkąt"
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Niepoprawne wartości boków trójkąta")
        self.a = a
        self.b = b
        self.c = c

    def count_surface_area(self):
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
```

- **`class Name:` / `__init__(self, ...)`** — `__init__` acts as the
  constructor (like JS/Java `constructor(...)`), though Python technically
  splits object creation into `__new__` (allocates the object) and
  `__init__` (initializes it) — `__new__` is basically never touched
  directly, so `__init__` is what people call "the constructor" in
  practice.
- **`self`** — refers to the specific instance being operated on, Python's
  explicit equivalent of JS's implicit `this`. `self.a = a` creates an
  attribute `a` on that instance, later readable as `triangle.a`.
- **Validating in the constructor + `raise ValueError(...)`** — reject
  invalid construction arguments immediately, before assigning them as
  attributes, so an invalid `Triangle` can never exist half-built.
- **Instance methods** (`def count_surface_area(self):`) — always take
  `self` as the first parameter to access the instance's own attributes;
  called as `triangle.count_surface_area()` (`self` passed implicitly by
  Python).
- **Dunder ("double underscore"/magic) methods** — special methods Python
  calls automatically for operators, e.g. `__le__` backs `<=`
  (`a <= 0` → `a.__le__(0)`), `__add__` backs `+` (`a + b` → `a.__add__(b)`).
  PyCharm's inline `{__le__, __add__}` hints next to untyped parameters
  aren't code — they're the IDE inferring, from how each parameter is used
  in the function body, which dunder methods its type must support (a
  duck-typing/structural hint, purely informational, no runtime effect).
- **Three near-identical classes** (`Triangle`, `Rectangle`, `Circle`),
  each with its own `count_surface_area`, `count_perimeter`,
  `display_name` — same shape repeated per class rather than a shared
  base class (no inheritance used here, unlike the earlier `Enum` example).
- **Separate `try/except ValueError as e: print(e)` per shape** at the
  bottom — each construction attempt is isolated, so one invalid shape
  doesn't stop the others from being tried.

## 2026-09-25 — `zad2.py` (university/pythonWSEI/pythonExercises3)

```python
class Turtle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.__x = 0

    def move(self, distance):
        self.__x += distance

    def get_position(self):
        return self.__x
```

- **`self.__x` — "private" attribute via name mangling.** Python has no
  real `private`/`public` access modifiers (unlike Java/TS). Conventions
  instead:
  - `_x` (single underscore) — convention only: "internal, don't touch,"
    but nothing enforces it.
  - `__x` (double leading underscore, not a dunder) — Python automatically
    renames it internally to `_ClassName__attr` (here, `_Turtle__x`), a
    process called **name mangling**. This makes external access awkward
    (though not impossible: `john_turtle._Turtle__x` still works) and
    prevents accidental name collisions in subclasses. Plain
    `john_turtle.__x` raises `AttributeError`.
  - Net effect: Python's version of a private field with a getter —
    `__x` is only meant to be touched through the class's own methods
    (`move()` to change it, `get_position()` to read it), enforced by
    convention/mangling rather than a language keyword.
- **Methods mutating instance state:** `move()` updates `self.__x` via
  `+=` instead of returning a new value — same augmented-assignment
  operator seen in `pythonExercises/zad3.py`, applied to an instance
  attribute this time.
- Same instance-creation/method-call pattern as `zad1.py`:
  `john_turtle = Turtle("John", 5)`, then `john_turtle.move(10)`,
  `john_turtle.get_position()`.

## 2026-09-25 — `zad3.py` (university/pythonWSEI/pythonExercises3)

Three small, unrelated classes (`Employee`, `Monster`, `Refrigerator`),
each reusing the same `__init__`/instance-methods-returning-f-strings shape
as `zad1.py`/`zad2.py`. New concepts:

- **`list.append(item)`** (`self.items.append(item)`) — adds an item to
  the end of a list. (Earlier exercises used `set.add()` and list
  comprehensions, but not `list.append()` directly.)
- **`list.remove(item)`** (`self.items.remove(item)`) — removes the
  *first matching value* from a list (by value, not by index — unlike
  JS's index-based `splice`).
- **`str.join(iterable)`** (`', '.join(self.items)`) — joins a list of
  strings into one string with a separator between each item. Equivalent
  to JS `array.join(', ')`, but the separator string is the one calling
  `.join()` and the list is passed as the argument — order is flipped
  compared to JS.

## 2026-09-25 — `zad4.py` (university/pythonWSEI/pythonExercises3)

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def describe(self):
        print(f"Jestem zwierzęciem gatunku {self.species}.")

class Bird(Animal):
    def __init__(self, species, wingspan, plumage_color):
        super().__init__(species)
        self.wingspan = wingspan
        self.plumage_color = plumage_color

    def sing(self):
        print(f"{self.species} śpiewa piękną pieśń.")
```

First real (user-defined) class inheritance example — `Enum` back in
`pythonExercises/zad3.py` was inheritance too, but from a built-in base
class, not one written in the exercise. Understood, concepts for
reference:

- **`class Bird(Animal):`** — `Bird` inherits from `Animal`: it gets
  `Animal`'s methods (`describe()`) automatically, plus its own extra ones
  (`sing()`, `fly()`, `information_about_bird()`).
- **`super().__init__(species)`** — calls the parent class's `__init__`
  to set up the attributes it's responsible for (`self.species`), instead
  of duplicating that assignment in the child. The child's `__init__` then
  adds its own extra attributes (`wingspan`, `plumage_color`) on top.
  Equivalent to JS/Java `super(species)` inside a subclass constructor.
- **`my_bird.describe()`** — calling a method the subclass never
  defined itself; Python looks it up on the parent class since `Bird`
  doesn't override it.
- Second example (`Character` → `Warrior`) follows the identical pattern:
  `super().__init__(name, health)` plus one extra attribute (`strength`)
  and extra methods (`attack()`, `defend()`) added in the subclass.

## 2026-09-25 — `zad1.py` (university/pythonWSEI/pythonExercises4)

```python
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

class Elektryczny(Samochod):
    def __init__(self, zasieg_na_ladowaniu, **args):
        super(Elektryczny, self).__init__(**args)
        self.zasieg_na_ladowaniu = zasieg_na_ladowaniu

class Sportowy(Samochod):
    def __init__(self, maksymalna_predkosc, **args):
        super(Sportowy, self).__init__(**args)
        self.maksymalna_predkosc = maksymalna_predkosc

class ElektrycznySportowy(Elektryczny, Sportowy):
    def __init__(self, marka, model, zasieg_na_ladowaniu, maksymalna_predkosc):
        super(ElektrycznySportowy, self).__init__(marka=marka, model=model, zasieg_na_ladowaniu=zasieg_na_ladowaniu, maksymalna_predkosc=maksymalna_predkosc)
```

First **multiple inheritance** example — `ElektrycznySportowy(Elektryczny, Sportowy)`, where both bases ultimately inherit from `Samochod` (a "diamond" shape). New concepts:

- **`super(ClassName, self).__init__(...)`** — the explicit, two-argument
  form of `super()`. Functionally identical to the zero-arg `super()`
  shorthand from `pythonExercises3/zad4.py`; Python 3's `super()` is sugar
  that expands to exactly this explicit form. (Old-style/Python 2
  compatible, still valid, just more verbose.)
- **Multiple inheritance and MRO (Method Resolution Order):**
  `super()` does **not** call "my literal parent class" — it calls the
  *next class in the MRO of the actual instance's type*. For
  `ElektrycznySportowy`, the MRO is
  `ElektrycznySportowy → Elektryczny → Sportowy → Samochod → object`
  (inspectable via `ElektrycznySportowy.__mro__`). So when `Elektryczny`
  calls `super().__init__()`, it actually reaches `Sportowy` next, not
  `Samochod` directly — even though `class Elektryczny(Samochod)` looks
  like a direct link. MRO/C3 linearization guarantees `Samochod.__init__`
  still only runs once despite two inheritance paths leading to it.
- **Why `**kwargs` (not positional args) is required for this to work:**
  keyword-argument matching is **name-based, not order/position-based**.
  `ElektrycznySportowy.__init__` sends all four values as keyword args in
  one `super().__init__(marka=..., model=..., zasieg_na_ladowaniu=...,
  maksymalna_predkosc=...)` call. Each class down the MRO chain
  (`Elektryczny` → `Sportowy` → `Samochod`) only grabs the one named
  parameter it declares, and sweeps everything else it doesn't recognize
  into its own `**args` dict, forwarding that remainder on to whichever
  class is next in the MRO — without needing to know in advance what that
  next class even is. Traced with prints:
  ```
  Elektryczny keeps: zasieg_na_ladowaniu=500, forwards: {'marka': 'Tesla', 'model': 'Model S', 'maksymalna_predkosc': 250}
  Sportowy keeps: maksymalna_predkosc=250, forwards: {'marka': 'Tesla', 'model': 'Model S'}
  Samochod received: marka=Tesla, model=Model S
  ```
  This is a **single sequential relay chain** (`Elektryczny → Sportowy →
  Samochod`), not each base class being called independently in parallel
  by `ElektrycznySportowy`.
  - Using plain **positional** args instead breaks specifically because
    of this MRO indirection: `Elektryczny` assumes its `super().__init__()`
    call goes to `Samochod`'s `(marka, model)` signature, but it actually
    lands on `Sportowy`'s `(maksymalna_predkosc, marka, model)` signature
    — so a positional value meant for `marka` silently lands in
    `maksymalna_predkosc`'s slot instead, then errors on a missing
    argument. `**kwargs` avoids this entirely since matching is by name.
- **`**args` in a parameter list vs. in a call** — two complementary jobs:
  in a `def`, `**args` *collects* stray keyword arguments into a dict;
  in a call, `**args` *unpacks* a dict back out into individual keyword
  arguments (like JS's `...args` / `{...obj}` spread, but keyword-specific
  in Python — `*args` without the second `*` handles positional
  args/spread the same way).

## 2026-09-25 — `zad2.py` (university/pythonWSEI/pythonExercises4)

```python
class BankAccount:
    def __init__(self, account_number, currency, bank, owner, balance=0):
        ...
        self.__owner = owner
        self.__balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}\n..."

    def __len__(self):
        return self.__balance

    def __add__(self, other):
        if (isinstance(other, BankAccount) and self.bank == other.bank
                and self.currency == other.currency
                and self.__owner == other.get_owner()):
            new_balance = self.__balance + other.get_balance()
            return BankAccount(self.account_number, self.currency, self.bank, self.__owner, new_balance)
        else:
            raise ValueError("Accounts cannot be added. They are not compatible.")
```

- **`balance=0`** — a **default parameter value**: `balance` is optional
  when constructing a `BankAccount`; if omitted, it defaults to `0`.
- **Getter/setter methods** (`get_owner()`/`set_owner()`,
  `get_balance()`/`set_balance()`) — the conventional Python way to expose
  controlled read/write access to a "private" (`__`-mangled) attribute
  from outside the class, since `self.__owner` isn't reachable as
  `account.__owner` externally. (Python also has a `@property` decorator
  for a more elegant version of this, not used here.)
- **`isinstance(obj, ClassName)`** — checks whether `obj` is an instance
  of a given class (or subclass), like `instanceof` in JS/Java. Used to
  guard against adding a `BankAccount` to something that isn't one.
- **`__str__`** — dunder method controlling what `str(obj)` (and `print(obj)`)
  produces. Without it, printing an object gives an unhelpful default like
  `<BankAccount object at 0x...>`; defining `__str__` lets you return a
  custom readable string instead.
- **`__len__`** — dunder method controlling what `len(obj)` returns.
  Repurposed here to mean "account balance" (an unusual choice, since
  `len()` is normally for size/count of a collection — but demonstrates
  that any behavior can be hooked in).
- **`__add__` — operator overloading.** Defines what `+` does for
  instances of this class: `account1 + account2` is translated by Python
  into `account1.__add__(account2)` (`self` = left operand, `other` =
  right operand). This is the same dunder mechanism flagged earlier by
  PyCharm's inferred `{__add__}` type hint in `pythonExercises3/zad1.py` —
  here it's the actual implementation instead of an inferred requirement.
  - Validates `other` is a compatible `BankAccount` (same bank, currency,
    owner) before combining, `raise`ing `ValueError` otherwise.
  - Returns a **brand-new** `BankAccount` with the summed balance rather
    than mutating either existing account — mirrors how `+` behaves for
    Python's built-in types (e.g. `"a" + "b"` returns a new string, it
    doesn't mutate either operand).

## 2026-09-25 — `zad3.py` (university/pythonWSEI/pythonExercises4)

Same `BankAccount` as `zad2.py`, but `get_owner()`/`set_owner()`/
`get_balance()`/`set_balance()` are replaced with `@property`:

```python
@property
def owner(self):
    return self.__owner

@owner.setter
def owner(self, new_owner):
    self.__owner = new_owner
```

- **`@property` / `@x.setter`** — turns a pair of methods into a
  **descriptor** stored as a class attribute (`BankAccount.owner`, type
  `property`), which intercepts Python's default attribute-access
  behavior. Normally `a.owner = v` would just write `v` into
  `a.__dict__['owner']`, and `a.owner` would read it back — but a data
  descriptor defined on the class takes priority over the instance's own
  `__dict__`, so `a.owner = v` instead calls the descriptor's `__set__`
  (running the `@owner.setter` method), and `a.owner` calls its `__get__`
  (running the `@property` getter). Confirmed by inspection: `a.__dict__`
  never contains an `'owner'` key at all, only the mangled
  `_BankAccount__owner`; `BankAccount.owner` is a `property` object.
  - Net effect: lets calling code use plain attribute syntax
    (`account1.owner`, `account1.balance = 1500`) while secretly routing
    through custom getter/setter methods — same underlying idea as
    `zad2.py`'s manual `get_owner()`/`set_owner()`, just with cleaner call
    syntax (compare `other.balance` here vs. `other.get_balance()` in
    `zad2.py`, used inside `__add__`).
  - Real-world benefit beyond syntax: **future-proofing the public
    interface**. If validation logic (e.g. "balance can't go negative")
    is added later inside `balance.setter`, every existing
    `account.balance = x` call site keeps working unchanged and
    automatically gets the new validation — no call sites need to change
    to something like `set_balance(x)`. (Not actually exercised in this
    file — the setters here just assign directly, no validation added.)
- **Constructor defaults vs. property defaults — they're unrelated.**
  `balance=0` in `__init__(self, ..., balance=0)` is only a fallback for
  the constructor *parameter* if omitted at construction time; `__init__`
  still runs `self.__balance = balance` exactly once with whichever value
  was actually used. The property getter/setter have no independent
  default of their own — they just read/write that same `self.__balance`
  slot afterward. `owner` has no default at all (a required constructor
  parameter).

## 2026-09-25 — `zad4.py` (university/pythonWSEI/pythonExercises4)

```python
import random
import string

def generate_password(length, min_letters=1, min_digits=1):
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        letters_count = sum(c.isalpha() for c in password)
        digits_count = sum(c.isdigit() for c in password)
        if letters_count >= min_letters and digits_count >= min_digits:
            yield password

password_generator = generate_password(length=8, min_letters=4, min_digits=2)

for _ in range(5):
    print(next(password_generator))
```

- **`yield` → generator function.** Any function containing `yield`
  anywhere in its body becomes a **generator function** — decided by
  Python at compile time just from the presence of `yield`, regardless of
  whether that line is actually reachable at runtime (even a `yield`
  behind an `if` that's always `False` still makes it a generator; calling
  it never runs the body directly, it always just returns a generator
  object). Confirmed:
  ```python
  def looks_normal_but_isnt(flag):
      if flag:
          yield 1
      return 42

  looks_normal_but_isnt(False)   # <generator object ...> — body never ran
  ```
- **Calling a generator function doesn't run its code** — it returns a
  paused generator object. `generate_password(...)` does *not* start the
  `while True:` loop yet.
- **`next(generator)`** — resumes execution from where it last paused,
  runs until the next `yield`, returns that value, then **pauses again**
  — everything after `yield` stays frozen until the next `next()` call.
  This is how an infinite `while True:` loop doesn't hang: it only ever
  advances one step per `next()` call. Iterating a generator with a
  `for` loop does the same thing under the hood, calling `next()`
  repeatedly.
- **`string.ascii_letters`** (`'abc...XYZ'`) / **`string.digits`**
  (`'0123456789'`) — constant strings from the `string` module listing
  character sets.
- **`random.choices(population, k=n)`** — picks `n` random elements from
  `population`, **with repetition allowed** (unlike `random.sample`,
  which wouldn't repeat). Returns a list.
- **`c.isalpha()` / `c.isdigit()`** — `True`/`False` checks on a single
  character.
- **Generator expression inside `sum()`:**
  `sum(c.isalpha() for c in password)` — `(... for ... in ...)` without
  brackets is a **generator expression**, like a lazy list comprehension.
  `sum()` adds up the `True`/`False` values, which behave as `1`/`0` in
  arithmetic — so this counts how many characters are letters.
- **`_` as a loop variable** — conventional name meaning "I don't need
  this value," used when a loop only cares about *how many times* to
  repeat (`for _ in range(5):`), not the current item.

## 2026-09-25 — Concepts not yet covered, similar difficulty level

Natural next topics given everything above (functions, `try/except`,
comprehensions, file I/O, classes/inheritance/`@property`/dunders,
generators). Each links to the official Python docs.

- **Lambda functions** — small anonymous one-line functions
  (`square = lambda x: x * x`), often used as a quick throwaway function
  passed to something like `sorted(key=...)`.
  [Lambda expressions — Python docs](https://docs.python.org/3/reference/expressions.html#lambda) ·
  [How to Use Python Lambda Functions — Real Python](https://realpython.com/python-lambda/) ·
  [How the Python Lambda Function Works — freeCodeCamp](https://www.freecodecamp.org/news/python-lambda-function-explained/)
- **`*args` / `**kwargs` in ordinary functions** — you've seen `**args`
  used for cooperative `super()` calls in `pythonExercises4/zad1.py`, but
  it's a general-purpose feature for any function that needs to accept a
  variable number of positional (`*args`) or keyword (`**kwargs`)
  arguments. `args`/`kwargs` are just **conventional names, not
  keywords** — only the `*`/`**` actually matter; `def f(*vars, **options):`
  behaves identically, everyone just uses `args`/`kwargs` by convention so
  it's instantly recognizable.
  [Arbitrary argument lists — Python tutorial](https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists) ·
  [Python args and kwargs: Demystified — Real Python](https://realpython.com/python-kwargs-and-args/) ·
  [Clearing the Confusion Once and For All: args, kwargs, and Asterisks in Python — Bex T. (Medium)](https://medium.com/data-science/clearing-the-confusion-once-and-for-all-args-kwargs-and-asterisks-in-python-a905c36467a2) ·
  [Python *args and **kwargs — Will Vincent](https://wsvincent.com/python-args-kwargs/)
- **Extended iterable unpacking with `*`** — `first, *rest = [1, 2, 3, 4]`
  gives `first = 1`, `rest = [2, 3, 4]`. Same `*` used for `*args`, but
  applied to assignment. The starred variable can sit anywhere
  (`first, *middle, last = animals`), always collects into a `list`
  regardless of what's being unpacked, and only one `*` is allowed per
  assignment.
  [Assignment statements — Python docs](https://docs.python.org/3/reference/simple_stmts.html#assignment-statements) ·
  [Extended iterable unpacking — Python Morsels](https://www.pythonmorsels.com/extended-iterable-unpacking/) ·
  [Unpacking with starred assignments — Pydon't (mathspp)](https://mathspp.com/blog/pydonts/unpacking-with-starred-assignments) ·
  [PEP 3132 — Extended Iterable Unpacking](https://peps.python.org/pep-3132/)
- **Dict and set comprehensions** — same idea as the list comprehensions
  already used (`pythonExercises2/zad1.py`), extended to `{}`:
  `{k: v for k, v in pairs}`, `{x * x for x in range(5)}`.
  [Dictionaries — Python tutorial](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) ·
  [Python Dictionary Comprehensions: How and When to Use Them — Real Python](https://realpython.com/python-dictionary-comprehension/) ·
  [Python Set Comprehensions: How and When to Use Them — Real Python](https://realpython.com/python-set-comprehension/) ·
  [Comprehensions in Python — GeeksforGeeks](https://www.geeksforgeeks.org/python/comprehensions-in-python/)
- **`@staticmethod` / `@classmethod`** — sibling decorators to `@property`
  (already used in `pythonExercises4/zad3.py`). `@staticmethod` defines a
  method that doesn't need `self` at all (just namespaced under the
  class); `@classmethod` receives the class itself (`cls`) instead of an
  instance — often used for alternative constructors.
  [`staticmethod` — Python docs](https://docs.python.org/3/library/functions.html#staticmethod) ·
  [`classmethod` — Python docs](https://docs.python.org/3/library/functions.html#classmethod) ·
  [Python's Instance, Class, and Static Methods Demystified — Real Python](https://realpython.com/instance-class-and-static-methods-demystified/) ·
  [Class Method vs Static Method in Python — GeeksforGeeks](https://www.geeksforgeeks.org/python/class-method-vs-static-method-python/)
- **Custom exceptions** — defining your own exception type by subclassing
  `Exception` (`class InsufficientFundsError(Exception): pass`), so
  callers can `except InsufficientFundsError:` specifically instead of a
  generic `except Exception:`/`except ValueError:` as done throughout the
  exercises so far.
  [User-defined exceptions — Python tutorial](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions) ·
  [Defining Your Own Exceptions — Real Python](https://realpython.com/lessons/defining-your-own-exceptions/) ·
  [How to Define Custom Exceptions in Python — Programiz](https://www.programiz.com/python-programming/user-defined-exception)
- **`zip(iterable1, iterable2, ...)`** — pairs up elements from multiple
  iterables positionally, e.g. `zip(names, ages)` → pairs of
  `(name, age)`. Commonly combined with a dict comprehension:
  `{n: a for n, a in zip(names, ages)}`.
  [`zip` — Python docs](https://docs.python.org/3/library/functions.html#zip) ·
  [Using the Python zip() Function for Parallel Iteration — Real Python](https://realpython.com/python-zip-function/) ·
  [Python zip() Function — freeCodeCamp](https://www.freecodecamp.org/news/the-zip-function-in-python-explained-with-examples/)
- **`import json`** — read/write JSON, the natural sibling to the `csv`
  module already used (`pythonExercises2/zad4.py`):
  `json.load(file)` / `json.dump(data, file)`.
  [`json` — Python docs](https://docs.python.org/3/library/json.html) ·
  [Working With JSON Data in Python — Real Python](https://realpython.com/python-json/) ·
  [Python JSON: Read, Write, Parse JSON — Programiz](https://www.programiz.com/python-programming/json)
- **`pathlib`** — an object-oriented, more modern alternative to the
  `os.path` functions already used throughout
  `pythonExercises2/zad1.py`/`zad3.py` (e.g. `Path(base_dir) / 'kopie'`
  instead of `os.path.join`, `.exists()`, `.is_dir()` as methods instead
  of `os.path.exists()`/`os.path.isdir()`).
  [`pathlib` — Python docs](https://docs.python.org/3/library/pathlib.html) ·
  [Python's pathlib Module: Taming the File System — Real Python](https://realpython.com/python-pathlib/) ·
  [Pathlib Module in Python — GeeksforGeeks](https://www.geeksforgeeks.org/python/pathlib-module-in-python/)
- **f-string format specs** — beyond plain `f"{value}"`, a mini
  language after `:` controls formatting, e.g. `f"{price:.2f}"` (2
  decimal places) as a more direct alternative to the `round()` calls
  used throughout the earlier exercises.
  [Format specification mini-language — Python docs](https://docs.python.org/3/library/string.html#format-specification-mini-language) ·
  [Python's Format Mini-Language for Tidy Strings — Real Python](https://realpython.com/python-format-mini-language/) ·
  [Python's F-String for String Interpolation and Formatting — Real Python](https://realpython.com/python-f-strings/) ·
  [Python f-string — formatting strings in Python with f-string — ZetCode](https://zetcode.com/python/fstring/) ·
  [String Alignment in Python f-string — GeeksforGeeks](https://www.geeksforgeeks.org/python/string-alignment-in-python-f-string/) ·
  [Guide to String Formatting in Python Using F-strings — Built In](https://builtin.com/data-science/python-f-string)

## 2026-09-25 — Practice tasks

Self-directed exercises combining concepts from `university/pythonWSEI/`
with the additional concepts above. No solutions written down — attempt
independently, ask for a review/hints when stuck.

1. **Library system (classes, `@property`, dunders, custom exceptions).**
   Build a `Book` class (`title`, `author`, `pages`, `is_borrowed`) using
   `@property` for controlled access, `__str__` for a readable
   description, and `__len__` returning `pages`. Build a `Library` class
   holding a `dict` of books keyed by title. Define a custom
   `BookNotAvailableError(Exception)` and `raise` it from a `borrow(title)`
   method if the book is already borrowed or doesn't exist. Add a method
   returning a list of currently available books using a list
   comprehension.

2. **Fibonacci generator (generators, comprehensions, `sum`).** Write a
   generator function `fibonacci()` that `yield`s Fibonacci numbers
   forever (like the infinite `while True:` + `yield` pattern from
   `pythonExercises4/zad4.py`, but without the retry-until-valid logic).
   Then, without ever converting it to a full list, use it to compute the
   sum of all *even* Fibonacci numbers below 4,000,000 (stop pulling from
   the generator once you pass the limit).

3. **CSV/JSON report tool (file I/O, `csv`/`json`, `statistics`, custom
   context manager).** Read a CSV of records (e.g. products with a price
   column, similar shape to `pythonExercises/zad4.py`'s product/price
   pairs), compute `mean`/`median` price with the `statistics` module, and
   write the results out as a JSON file. Wrap the "start/end of
   processing" with your own context manager (a class with
   `__enter__`/`__exit__`, or `@contextlib.contextmanager`) that prints a
   timestamped start/end message — read up on context managers beyond
   `with open(...)` first, since this task needs a custom one.

4. **Mixins and multiple inheritance (MRO, `**kwargs` cooperation).**
   Write two small "mixin" classes: `LoggableMixin` (a `log(message)`
   method that prints with a timestamp) and `ComparableMixin` (implements
   `__eq__`/`__lt__` by comparing some attribute you decide on). Combine
   both into one class via multiple inheritance, alongside a base class
   with its own `__init__`, following the same cooperative `**kwargs`
   `super().__init__()` relay pattern from `pythonExercises4/zad1.py` so
   construction works correctly. Verify with `YourClass.__mro__`.

5. **Flexible aggregator function (`*args`, `**kwargs`, `zip`, lambdas).**
   Write a function `summarize(*args, **kwargs)` that accepts any number
   of numeric positional arguments and computes their sum/average, with
   optional keyword arguments like `round_to=2` (using an f-string format
   spec or `round()`) and `label="Result"` for the printed output. Then
   write a second function that takes two lists of equal length (names
   and values) and uses `zip()` + a dict comprehension to build a
   `{name: value}` mapping, sorted by value using
   `sorted(..., key=lambda ...)`.

## 2026-09-25 — Python's type system

Comparisons below are to JS/TS since that's the reference point so far.

### Dynamic typing — variables aren't typed, values are

A variable name can be rebound to any type at any time; nothing is
declared up front:
```python
x = 5
x = "now a string"   # totally legal
x = [1, 2, 3]         # legal again
```
This is like JS `let x = 5; x = "now a string";` (not like TS, which
would reject that reassignment under a static type annotation). Python
has no `let`/`const`/type keyword — just `name = value`.

### Strong typing — but no silent coercion between unrelated types

"Dynamic" is not the same as "loose." Python won't silently convert
between incompatible types the way JS does:
```python
"5" + 5      # TypeError: can only concatenate str (not "int") to str
```
vs JS: `"5" + 5` → `"55"` (silent coercion). This is exactly why
`int(age)` / `float(money)` conversions showed up constantly in the
`pythonExercises` files — Python requires you to convert explicitly
before combining `str` and numeric values, rather than doing it for you.

### The core built-in types

| Type | Example | Mutable? | Notes |
|---|---|---|---|
| `int` | `5` | — (immutable) | arbitrary precision, no overflow |
| `float` | `3.14` | — | |
| `bool` | `True`/`False` | — | subtype of `int` (`True == 1`) |
| `str` | `"abc"` | — | immutable — `s[0] = 'x'` fails |
| `NoneType` | `None` | — | Python's `null`/`undefined` equivalent |
| `list` | `[1, 2, 3]` | **yes** | `.append()`, item assignment work |
| `tuple` | `(1, 2, 3)` | — | fixed once created (covered earlier, in the `zad1.py` follow-up above) |
| `dict` | `{'a': 1}` | **yes** | keys must be hashable (immutable-ish) |
| `set` | `{1, 2, 3}` | **yes** | unordered, no duplicates |
| `frozenset` | `frozenset({1,2})` | — | immutable version of `set` |

**Mutable vs immutable matters a lot** in Python — it's why a `list`
can't be a `dict` key/`set` member but a `tuple` can (immutable →
hashable), and why reassigning `self.__x = 0` then `self.__x += distance`
in `pythonExercises3/zad2.py` actually rebinds `__x` to a *new* `int`
each time rather than mutating the old one in place (`int` is immutable).

### Checking types at runtime

- **`type(x)`** — returns the exact type object, e.g. `type(5)` → `<class 'int'>`.
- **`isinstance(x, SomeType)`** — checks if `x` is that type *or a
  subclass of it* (already used in `pythonExercises4/zad2.py`'s
  `__add__` to validate `other`). Prefer `isinstance()` over `type() ==`
  for this reason — it respects inheritance.

### Duck typing — Python cares what an object *can do*, not what it *is*

Python usually doesn't check types explicitly at all — it just tries the
operation, and if the object supports it, it works. This is exactly what
was going on with PyCharm's inferred `{__le__, __add__}` hints in
`pythonExercises3/zad1.py`: Python doesn't care that a parameter is
"officially" an `int` — it only cares that whatever's passed in supports
`<=` (has `__le__`) and `+` (has `__add__`). "If it walks like a duck and
quacks like a duck..." — any object implementing the right dunder methods
can be used, regardless of its declared type (there often isn't one).

### Type hints (optional, not enforced at runtime)

Python also supports **optional** type annotations (PEP 484) — closer to
what TypeScript gives you, but Python itself does **not** enforce them at
runtime; they're purely for humans and external tools (PyCharm, `mypy`)
to catch mistakes *before* running the code:
```python
def add(a: int, b: int) -> int:
    return a + b

add("oops", "still runs")   # runs fine at runtime, no TypeError from typing —
                             # a type checker (mypy/PyCharm) would flag it though
```
None of the exercises so far use these annotations — every function has
been written with plain, unannotated parameters — but you'll see them a
lot in larger/production Python codebases.
[`typing` module — Python docs](https://docs.python.org/3/library/typing.html) ·
[PEP 484 — Type Hints](https://peps.python.org/pep-0484/)

### Reference

[Built-in Types — Python docs](https://docs.python.org/3/library/stdtypes.html) —
full built-in types reference.

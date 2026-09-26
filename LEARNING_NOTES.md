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

## 2026-09-25 — `2-liczby.py` (university/kolokwium python 2024)

A set of commented-out numeric demo snippets (not a runnable script — each
block meant to be uncommented individually). Understood, concepts for
reference:

```python
print(int(1.9))    # 1
print(int(-1.9))   # -1

a = 0b1             # binary literal: 1
a = a << 2          # left shift: 1 << 2 = 4
print(bin(a))       # '0b100'
a <<= 1              # augmented shift assignment: a = a << 1

a = 0b100
b = 0b1000
a | b                # bitwise OR
a & b                # bitwise AND
a ^ b                # bitwise XOR

import math
math.sqrt(5)
-5 ** 0.5            # note: -(5 ** 0.5), NOT (-5) ** 0.5 — unary minus
                     # binds *after* **, so this is -2.236..., not a
                     # complex/error result
math.sqrt(-5)        # ValueError: math domain error
```

- **`int(x)` on a float truncates toward zero**, it doesn't round:
  `int(1.9) == 1`, `int(-1.9) == -1` (not `-2`) — different from `round()`.
- **`0b...` binary literals** — write an integer directly in binary,
  e.g. `0b100 == 4`. **`bin(x)`** does the reverse: converts an `int` to
  its `'0b...'` string representation.
- **Bit-shift operators `<<`/`>>`** — shift bits left/right (`x << n`
  multiplies by `2**n`). **`<<=`** is the same augmented-assignment
  pattern as `+=`/`*=` seen earlier, applied to shifting.
- **Bitwise operators `|` (OR), `&` (AND), `^` (XOR)** — operate on the
  binary representation of integers bit-by-bit. Distinct from the logical
  `or`/`and` used everywhere else in the exercises so far, which operate
  on whole truthy/falsy values, not individual bits.
- **Operator precedence gotcha: `-5 ** 0.5`** — `**` binds *tighter* than
  unary `-`, so this parses as `-(5 ** 0.5)`, not `(-5) ** 0.5`. Matters
  here because `(-5) ** 0.5` would involve a square root of a negative
  number.
- **`math.sqrt(-5)` raises `ValueError`** — the `math` module only works
  with real numbers; there's a separate `cmath` module for complex-number
  math that would return a complex result instead of erroring.

## 2026-09-25 — `2-liczby-dodatek.py` (university/kolokwium python 2024)

Demonstrates Python's alternative numeric types beyond plain `int`/`float`.
Understood, concepts for reference (actual output shown, verified by
running the script):

```python
from fractions import Fraction

Fraction(1, 3) + Fraction(4, 5)              # 17/15 — exact rational arithmetic
Fraction(2.3).limit_denominator(10 ** 14)    # 23/10 — simplifies float's messy exact binary value
                                              #         to the nearest simple fraction
```
- **`Fraction`** — exact rational numbers (numerator/denominator), no
  binary floating-point rounding error. `Fraction(2.3)` on its own would
  be a huge, ugly fraction (float `2.3` isn't exactly representable in
  binary); `.limit_denominator(n)` finds the closest "nice" fraction with
  denominator ≤ `n`. Mixing a `Fraction` with a plain `float` in `+`
  converts the result back to `float` (`Fraction(23,10) + 0.2 == 2.5`).

```python
import decimal
0.2 + 0.1                                    # 0.30000000000000004 — binary float rounding error
decimal.Decimal('0.2') + decimal.Decimal('0.1')  # 0.3 — exact
decimal.Decimal('0.1')                       # 0.1 — exact, built from the string
decimal.Decimal(0.1)                         # 0.1000000000000000055511151231257827021181583404541015625
                                              # — built from the float, exposes its true imprecise binary value
decimal.getcontext().prec = 2
decimal.Decimal(1) / decimal.Decimal(3)      # 0.33 — precision is now a global context setting
```
- **`decimal.Decimal`** — exact base-10 arithmetic, avoiding the classic
  `0.1 + 0.2 != 0.3` binary floating-point problem. **Construct from a
  string** (`Decimal('0.1')`) for an exact value; constructing **from a
  float** (`Decimal(0.1)`) instead exposes the float's actual imprecise
  binary representation, since the imprecision already happened before
  `Decimal` ever saw it.
  - `decimal.getcontext().prec = n` sets **global** precision (significant
    digits) for all subsequent `Decimal` arithmetic in the program.
  - `Decimal(...).as_integer_ratio()` — converts to an exact fraction
    tuple, e.g. `Decimal('2.6').as_integer_ratio()` → `(13, 5)`.

```python
complex('1+2j')   # (1+2j) — parsed from a string
2j                 # (0+2j) — imaginary literal, suffix j
1 + 2j             # (1+2j)
x = complex('1+2j')
x.real             # 1.0
x.imag             # 2.0
```
- **`complex`** — Python's built-in complex number type (`j` suffix for
  the imaginary part, like `i` in math but Python uses `j` — an
  engineering convention). `.real`/`.imag` extract the two components as
  `float`s.

```python
float('inf')       # inf
5 + float('inf')   # inf — anything + infinity is infinity
float('nan')       # nan
float('inf') + float('nan')   # nan — nan "poisons" any arithmetic it touches
float('-inf') + float('inf')  # nan — indeterminate form (∞ − ∞)
```
- **`float('inf')` / `float('-inf')` / `float('nan')`** — special
  floating-point values for infinity and "not a number" (e.g. the result
  of an undefined operation). `nan` propagates through any arithmetic
  it's involved in.

```python
divmod(10, 3)   # (3, 1) — (quotient, remainder) in one call
```
- **`divmod(a, b)`** — returns a tuple of `(a // b, a % b)` in a single
  call, instead of computing floor-division and modulo separately.

## 2026-09-25 — `3 - list comprehension.py` (university/kolokwium python 2024)

Goes further than the list comprehensions seen so far (a single `for` +
optional single `if`, e.g. `pythonExercises/zad4.py`). Understood,
concepts for reference (verified against actual output):

```python
tab = [a * 2 for a in range(10)]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
- Basic transform-only comprehension (no filter) — same shape as before,
  just multiplying instead of filtering.

```python
tab2 = [(a, b) for a in (1, 2, 3) for b in (1, 2)]
# [(1, 1), (1, 2), (2, 1), (2, 2), (3, 1), (3, 2)]
```
- **Multiple `for` clauses in one comprehension** — equivalent to nested
  `for` loops, left-to-right (`a` is the *outer* loop, `b` the *inner*
  one — `b` cycles fully for each `a`, same order as writing two nested
  `for` statements). Produces the Cartesian product of the two ranges
  here, built into tuples with `(a, b)`.

```python
tab4 = [(a, b) for a in range(1, 10) if a > 2
                for b in range(1, 10) if a % b == 0 and a != b and b != 1]
tab5 = [(a, b) for a in range(1, 10) if a > 2
                for b in range(1, 10) if a % b == 0 if a != b if b != 1]
# both produce: [(4, 2), (6, 2), (6, 3), (8, 2), (8, 4), (9, 3)]
```
- **`for`+`if` clauses can be chained/repeated** — each `for` can have
  its own `if` filter attached, applied at that nesting level (here:
  filter `a` first, *then* loop/filter `b` for each surviving `a`) —
  not one single filter applied at the very end.
- **Multiple consecutive `if` clauses = implicit `and`.** `tab5` proves
  `if cond1 if cond2 if cond3` behaves identically to one
  `if cond1 and cond2 and cond3` (`tab4`) — same output either way; just
  a stylistic choice for how to write several combined conditions.

```python
tab6 = [x for x in range(100) if 1024 in [x ** k for k in range(1, 11)]]
# [2, 4, 32]
```
- **A comprehension nested inside another comprehension's `if` clause.**
  For each `x` from 0–99, the inner comprehension
  `[x ** k for k in range(1, 11)]` builds a list of `x` raised to every
  power 1–10; the outer `if 1024 in [...]` keeps `x` only if `1024`
  appears somewhere in that list of powers. Result: `2` (2¹⁰ = 1024),
  `4` (4⁵ = 1024), `32` (32² = 1024) — every `x` that has *some* integer
  exponent (1–10) landing exactly on 1024.

## 2026-09-25 — `3-instrukcje-warunkowe.py` (university/kolokwium python 2024)

```python
a = 7 if 5 > 6 else 9          # 9
b = 'test1' if 'a' in 'abc' else 'test2'      # 'test1'
c = 'test3' if 'a' not in 'abc' else 'test4'  # 'test4'
```

- **Ternary conditional expression** (`x if cond else y`) — a full
  `if/else` compressed into a single expression that evaluates to a
  value, rather than a statement that runs a block. Equivalent to JS's
  `cond ? x : y`, just with the condition in the middle instead of first.
  This is exactly what makes a conditional possible *inside* a `lambda`
  (which can only contain one expression, no statements) — e.g.
  `lambda x: 'pos' if x > 0 else 'neg'`.
- **`in` / `not in` on a string checks substring presence**, not just
  element membership. `'a' in 'abc'` asks "does `'a'` appear anywhere
  inside `'abc'`?" — same `in` operator already used for list/dict
  membership (`pythonExercises2/zad1.py`), just applied to strings, where
  it means "is this a substring" rather than "is this exactly one
  element." `not in` is the direct negation of that check.

## 2026-09-25 — `3-lancuchy znakow.py` (university/kolokwium python 2024)

Dense file covering a lot of string-specific ground. Understood, concepts
for reference (verified against actual output):

```python
multiline = """line1
line2
line3"""
```
- **Triple-quoted strings (`"""..."""`)** — span multiple lines literally,
  newlines included as-is. Same syntax also doubles as the multi-line
  docstring convention (not used for that here, just as a plain string).

```python
t1 = '\temp'     # '\temp' → actually a TAB + "emp" ('\t' is an escape sequence)
t2 = '\\temp'    # a literal backslash + "temp" (escaped backslash)
t3 = r'\temp'    # a raw string: '\t' is NOT treated as an escape — literal backslash-t-e-m-p
```
- **Escape sequences** (`\t`, `\n`, etc.) inside normal strings vs.
  **raw strings** (`r'...'`), where backslashes are left completely
  literal — useful for things like Windows paths or regex patterns where
  you don't want `\` interpreted specially.

```python
a = 'tekst testowy'
a[:2] + a[3:8] + 'k' + a[8:]   # 'te' + 'st te' + 'k' + 'testowy' = 'test tekstowy'
```
- Building a new string by **concatenating slices around a "hole"** —
  effectively replacing the character at index 2 (`'k'`) with a different
  `'k'` by skipping it in the slices and inserting it manually. Strings
  are immutable, so this is how you get a "modified" string — you can
  never mutate one in place.

```python
d = "tekst"
d += ' nowy'    # 'tekst nowy' — string concatenation via +=
d *= 2          # 'tekst nowytekst nowy' — string REPEATED, via *=
```
- **`+=`/`*=` on strings** — same augmented-assignment operators seen on
  numbers (`pythonExercises/zad3.py`) and instance attributes
  (`pythonExercises3/zad2.py`), here doing string concatenation and
  **repetition** (`str * int` repeats the string `int` times).

```python
ord('a')   # 97 — character → its Unicode code point (int)
chr(98)    # 'b' — code point (int) → character
```
- **`ord()` / `chr()`** — convert between a single character and its
  numeric Unicode code point, inverse of each other.

```python
s = 'ala ma kota'
'ma' in s          # True — substring check (see 3-instrukcje-warunkowe.py)
s.find('ma')       # 4 — index of first match, or -1 if not found
s = (s + "\n").rstrip()   # strips trailing whitespace/newline only
s.upper() / s.lower()     # 'ALA MA KOTA' / 'ala ma kota'
'*'.join(s.split())       # 'ala*ma*kota' — split() with no args splits on any whitespace run
s.startswith('ala')       # True
```
- **`str.find(sub)`** — like `in` but returns the **index** of the first
  match (or `-1` if absent) instead of just `True`/`False`.
- **`str.rstrip()`** — strips whitespace from the **right side only**
  (there's also `.lstrip()` for left-only); `.strip()` (used earlier in
  `pythonExercises2/zad2.py`) does both sides.
- **`str.split()` with no argument** — splits on *any* run of whitespace
  (spaces, tabs, newlines), unlike `str.split(",")` (used in
  `pythonExercises/zad4.py`) which splits on one exact separator.
- **`str.startswith(prefix)`** — the mirror of `str.endswith(...)`
  (used in `pythonExercises2/zad1.py`).

```python
city = "łódź"          # Python 3 strings are Unicode by default — non-ASCII just works
source = "kraków"
u = source.encode('utf8')          # b'krak\xc3\xb3w' — str → bytes
type(u)                            # <class 'bytes'>
b = source.encode('iso-8859-2')    # b'krak\xf3w' — different encoding → different bytes!
result = source + u.decode('utf8') # bytes → str again, THEN concatenate
# source + u directly would raise TypeError — can't mix str and bytes with +
```
- **`str.encode(encoding)`** — converts text (`str`) into raw
  **`bytes`**, using a specific text encoding (`utf8`, `iso-8859-2`,
  etc.). The *same* string produces *different* byte sequences depending
  on encoding — there's no one universal "the bytes of this string,"
  encoding is always part of the deal.
- **`bytes.decode(encoding)`** — the inverse: raw bytes → text, given the
  encoding they were written in (get this wrong and you get garbled text
  or an error).
- **`str` and `bytes` are distinct types that can't be mixed with `+`** —
  matches the earlier "Python won't silently coerce between unrelated
  types" behavior from the type-system notes; you must explicitly
  `.decode()` bytes back to `str` first.

```python
str(234), repr(234)     # '234', '234'  — same for plain numbers
str('abc'), repr('abc') # 'abc', "'abc'" — repr() includes the quotes
```
- **`str()` vs `repr()`** — `str()` gives the human-readable display
  form; `repr()` gives an unambiguous, "as valid Python source as
  possible" form — for a string, that means the quotes are included, so
  you can see it *is* a string (matters more once nested inside other
  structures, e.g. printing a `list` of strings shows each one via
  `repr()`).

```python
'first value %s, second value %s' % (r1, r2)   # old %-style formatting
'number value is %.2f' % math.pi                # %.2f → 2 decimal places
'value = %10d' % n1                              # %10d → right-align in a width-10 field

'{0} - {1} - {1} - {0}'.format('ala', 'kota')          # positional placeholders, reusable
'{0} - {1!r} - {1!s} - {0}'.format('ala', 'kota')      # !r forces repr(), !s forces str()
```
- **`%`-style string formatting** — an older formatting mechanism
  (`'%s'`, `'%.2f'`, `'%10d'` etc., printf-style from C) predating both
  `.format()` and f-strings. You'll still encounter it in older codebases
  and some logging APIs.
- **`str.format()`** — the formatting method that came before f-strings;
  `{0}`/`{1}` are positional placeholders (reusable — `{1}` can appear
  twice), and `!r`/`!s` force a value through `repr()`/`str()`
  specifically inside the placeholder.
- All three formatting styles (`%`, `.format()`, f-strings) coexist in
  Python; f-strings (used throughout the exercises so far) are the
  modern preferred choice, but the other two are common enough in
  existing code to be worth recognizing.

## 2026-09-26 — `3-listy-i-krotki.py` (university/kolokwium python 2024)

Large file covering list/tuple mutation methods and unpacking patterns.
Understood, concepts for reference (verified against actual output):

```python
b = range(20, 90, 5)
print(b)          # range(20, 90, 5) — NOT a list!
c = list(b)
print(c)           # [20, 25, 30, 35, ..., 85]
```
- **`range(start, stop, step)`** — the 3-argument form (earlier exercises
  only used `range(n)` or `range(1, 13)`, i.e. 1 or 2 args). `range(...)`
  itself is a **lazy object**, not a list — printing it shows
  `range(20, 90, 5)` literally; `list(b)` is what actually materializes
  the values. Same lazy-object idea as `csv.DictReader` or the `zip()`
  object from earlier files.

```python
d = c[3:7]                       # slicing works on lists exactly like strings
e = d + ['a', 'b'] * 3           # list concatenation (+) and repetition (*)
e[3:] = []                       # slice assignment — deletes a whole range at once
del e[:3]                        # del with a slice — same idea, different syntax
```
- **`list + list`** concatenates; **`list * n`** repeats — same operators
  as string concatenation/repetition (`3-lancuchy znakow.py`), just on
  lists.
- **Slice assignment** (`e[3:] = []`) — assigning to a slice replaces
  (here: deletes, since the replacement is empty) that whole range of
  elements in place. Lists are **mutable**, unlike strings, so this
  actually works (no "build a new one via concatenation" workaround
  needed, unlike the string version in the previous file).
- **`del e[:3]`** — the `del` statement also accepts a slice, removing
  that range of elements; different syntax from slice-assignment, same
  net effect.

```python
e.append("test1")            # adds ONE item to the end
e.extend(["test2", "test3"]) # adds MULTIPLE items (unpacks the iterable)
e.extend("test4")            # extends with a STRING → adds each character separately!
e.insert(2, 'test5')         # inserts one item at a specific index
e.reverse()                  # reverses the list in place
```
- **`.append(x)` vs `.extend(iterable)`** — `.append()` always adds
  exactly one new element (even if it's itself a list); `.extend()`
  iterates its argument and adds each item individually. Gotcha:
  `.extend("test4")` doesn't add the string `"test4"` as one item — it
  iterates the string **character by character**, adding `'t'`, `'e'`,
  `'s'`, `'t'`, `'4'` as five separate elements.
- **`.insert(index, value)`** — inserts at a specific position, shifting
  everything after it along.
- **`.reverse()`** — reverses the list **in place** (mutates it, returns
  `None`).

```python
e.remove('test3')     # removes the first item EQUAL to this value
e.pop(1)               # removes AND returns the item at this index
e.index('e')           # returns the index of the first occurrence
```
- **`.pop(index)`** — like `.remove()` (used in `pythonExercises3/zad3.py`)
  but removes **by index** instead of by value, and **returns** the
  removed item instead of just discarding it. `.pop()` with no argument
  removes/returns the *last* item.
- **`.index(value)`** — the reverse lookup of `.remove()`: given a value,
  find its position.

```python
sorted(e)        # returns a NEW sorted list; e itself is unchanged
e.sort()          # sorts e IN PLACE; returns None
e.sort(reverse=True)
```
- **`sorted(x)` (built-in function) vs `x.sort()` (list method)** — key
  distinction: `sorted()` works on any iterable and always returns a
  brand-new list, leaving the original untouched; `.sort()` only exists
  on lists, mutates in place, and returns `None`. (`.sort(reverse=True)`
  itself was already seen in `pythonExercises/zad5.py`.)

```python
f = 1, 2, 3        # tuple — the COMMA creates it, not the parentheses
g = (1, 2, 3)       # same thing, parens are just visual/optional here
h = 1,               # a ONE-element tuple — needs a trailing comma
i = (1,)             # same — (1) alone would just be the int 1, not a tuple
```
- **Tuples are created by the comma, not by parentheses.** `f = 1, 2, 3`
  is a tuple exactly like `g = (1, 2, 3)` — parens are optional except
  where needed for clarity/precedence. For a **single-element tuple**,
  the trailing comma is *mandatory*: `(1)` is just the integer `1` in
  parentheses; `(1,)` is a 1-item tuple.

```python
var1, var2 = 1, 2
var1, var2 = var2, var1    # swaps them — no temp variable needed
print(var1, var2)          # 2 1
```
- **The classic Python swap idiom.** The right-hand side `var2, var1`
  builds a tuple `(var2's value, var1's value)` first, *then* unpacks it
  into `var1, var2` — so both swap simultaneously without needing a
  throwaway temp variable, unlike the usual `temp = a; a = b; b = temp`
  pattern in most other languages.

```python
l = [1, 2, 3]
[la, lb, lc] = l        # unpacking with a LIST pattern on the left
(x, y, z) = l            # unpacking with a TUPLE pattern on the left — both work identically

t = 'x1', 'y2', 'z3'
t1, t2, t3 = [t10, t20, t30] = t   # unpacking into TWO targets at once, from the same tuple
```
- **Unpacking doesn't care whether the left side is written with `[]` or
  `()`** — both are just patterns describing "how many names, in what
  shape," not a type requirement matching the right-hand side.
- **Chained assignment with unpacking**
  (`t1, t2, t3 = [t10, t20, t30] = t`) — Python evaluates the right-hand
  side once (`t`) and assigns it to *both* targets in the chain, each
  unpacked independently. Equivalent to unpacking `t` twice, once into
  `t1, t2, t3` and once into `t10, t20, t30`.

## 2026-09-26 — `4 - zbiory.py` (university/kolokwium python 2024)

Set operations and the `frozenset` type. Verified against actual output.

```python
s1 = set('zdanie z literami')   # from a string — one element per character, duplicates dropped
s2 = set([1, 68, 66, 66])        # from a list — [1, 68, 66, 66] → {1, 66, 68} — dup removed
s3 = {6, 5, 5}                   # set literal — {6, 5, 5} → {5, 6} — dup removed
```
- **Three ways to build a `set`**: from any iterable via `set(...)`
  (string, list, etc. — each element/character becomes one set member,
  duplicates automatically collapse), or a **literal** with `{}`.
  ⚠️ **Gotcha:** `{}` on its own is an **empty `dict`**, not an empty set
  — `type({})` is `dict`. An empty set can only be written `set()`.

```python
s4.add(4)                       # add one element (from pythonExercises/zad4.py)
s4.remove(5)                    # remove one element — raises KeyError if not present
s4.update(['test1', 'test2'])   # merge in multiple elements from any iterable
s4.update('kot')                # updating with a STRING adds each character separately
                                  # (same gotcha as list.extend("test4") in the previous file)
```
- **`set.remove(x)`** — like `list.remove(x)`, but raises **`KeyError`**
  if `x` isn't present (not `ValueError`, which is what the list version
  raises) — a set is more like a dict internally (hence `KeyError`), even
  though it only stores keys with no values.
- **`set.update(iterable)`** — the set equivalent of `list.extend()`:
  merges every element from the given iterable in, one at a time. Same
  string-iterates-per-character gotcha applies.

```python
s1 & s2     # intersection — elements in BOTH
s1 | s2     # union — elements in EITHER
s1 - s2     # difference — in s1 but NOT in s2
s1 |= s2    # in-place union (augmented assignment) — mutates s1 directly,
            # same object afterward (unlike int += which rebinds to a new object)
s1 >= s2    # superset check: does s1 contain every element of s2?
s1 <= s2    # subset check: does s2 contain every element of s1?
```
- **`&`/`|`/`-`** — intersection/union/difference, the standard set
  algebra operators. **`|=`** (and similarly `&=`, `-=`, `^=`) mutate the
  set **in place** rather than rebinding to a new object — because `set`
  is mutable, unlike `int`/`str`/`tuple`.
- **`>=`/`<=` on sets mean subset/superset, not size comparison** —
  `a >= b` asks "is `a` a superset of `b`" (contains every element of
  `b`); `a <= b` asks "is `a` a subset of `b`." (`>`/`<` are the *proper*
  subset/superset versions — subset/superset **and** not equal.) Two sets
  can be neither `<=` nor `>=` each other if they only partially overlap.

```python
s30 = set('kot')            # {'k', 't', 'o'} — mutable
s30f = frozenset('kot')      # frozenset({'k', 't', 'o'}) — immutable
s30.remove('k')              # fine — set is mutable
s30f.remove('k')             # AttributeError — frozenset has no .remove()/.add()/.update()
```
- **`frozenset`** — the immutable counterpart to `set`, same relationship
  as `tuple` is to `list`. No mutating methods at all (no `.add()`,
  `.remove()`, `.update()`). The payoff for giving up mutability is
  **hashability**: a `frozenset` can be used as a `dict` key or as a
  member of another `set` (`hash(frozenset(...))` works,
  `hash(a_regular_set)` raises `TypeError: unhashable type: 'set'`) —
  useful whenever you need "set of things" semantics *and* need that
  collection to itself be hashable.

## 2026-09-26 — `4-pliki.py` (university/kolokwium python 2024)

File-reading/writing mechanics beyond the basic `with open(...) as f:` +
`.read()`/`.readlines()` already seen in `pythonExercises2/zad2.py`.

```python
f = open(path)
txt = f.read(40)     # read only the first 40 CHARACTERS, not the whole file
f.close()
```
- **`f.read(n)`** — limits how much to read to `n` characters instead of
  the whole file (plain `f.read()` reads everything). The file keeps an
  internal **position/cursor** that automatically advances as you read —
  a second `f.read()` call afterward continues from where the first one
  stopped, rather than starting over.
- **`repr(txt)` after reading a file** — reused from `3-lancuchy
  znakow.py`'s `str()` vs `repr()`; printing `repr(txt)` shows `\n` as a
  literal two-character escape instead of rendering an actual line break,
  which is why it's a common debugging habit right after a file read —
  "show me exactly what's in this string, unprettified."

```python
f = open(path)
a = f.readline()     # reads just ONE line (up to and including the next \n)
b = f.readlines()     # reads ALL remaining lines into a list of strings
f.close()

f = open(path)
for line in f:        # iterating a file object directly yields one line at a time
    print(line)
f.close()
```
- **`f.readline()`** — reads a single line (this is what `readlines()`
  from `pythonExercises2/zad2.py` does repeatedly under the hood, one
  call at a time instead of all at once).
- **Iterating a file object directly with `for line in f:`** — a file
  object is itself iterable, yielding one line per iteration; equivalent
  to, but more idiomatic than, manually calling `.readline()` in a loop.

```python
f.seek(9)    # move the file's read position to byte offset 9; returns the new position
```
- **`f.seek(offset)`** — jumps the file's internal cursor to a specific
  position, overriding where the *next* read starts from (`f.seek(0)`
  rewinds to the very start, letting you re-read without reopening).
  - **Byte offsets ≠ character offsets in general.** For plain ASCII
    text, 1 character = 1 byte in UTF-8, so they line up. But non-ASCII
    characters (`ó`, `ł`, emoji, ...) take **multiple bytes** in UTF-8
    (e.g. `"kraków"` is 6 characters but 7 bytes — `ó` alone is 2 bytes:
    `b'krak\xc3\xb3w'`), so an arbitrary numeric `.seek()` can land
    mid-character on non-ASCII text, causing decode errors or garbled
    output. Python's docs say only `0` or a value previously returned by
    `.tell()` are safe to `.seek()` to on a text-mode file.
  - **There's no true "seek by character count"** for an open stream,
    because variable-width encoding means you can't compute a byte
    offset from a character count without decoding through the data
    first. Safe alternatives: read the whole file into a string and use
    normal (character-based) string slicing, or `f.read(n)` — discarding
    the result — to skip forward exactly `n` **characters** (since
    `.read(n)` in text mode counts characters, not bytes, decoding as it
    goes).

```python
with open("file2.txt", mode="w", encoding='utf-8') as f:
    ...
    f.write('wartość: %2d - potęga: %3d\n' % (a, b))
```
- **`open(path, mode="w", ...)`** — opens for **writing**, overwriting
  the file if it exists (same `'w'` mode already seen in
  `pythonExercises2/zad1.py`'s report generator).
- **`%`-style formatting reused** for building each line
  (`3-lancuchy znakow.py`), here with width specifiers (`%2d`, `%3d`)
  right-aligning numbers in a fixed-width field.

```python
r = range(1, 51)
res = [(a, b) for a in r for b in [a ** c for c in [2]] if b < 1000]
```
- **A comprehension's `for` source can itself be another comprehension.**
  `[a ** c for c in [2]]` is a roundabout way to compute `[a ** 2]` (a
  single-item list, since `c` only ever takes the one value `2`), so the
  outer `for b in [...]` effectively runs once per `a`, binding
  `b = a ** 2`. Combined with the outer `for a in r` and the
  `if b < 1000` filter, the whole expression pairs every `a` with its
  square, keeping only squares under 1000 — same "chained `for`/`if`"
  shape as `3 - list comprehension.py`, just with a nested comprehension
  as one of the iteration sources instead of a plain range/list.

## 2026-09-26 — `4-słowniki.py` (university/kolokwium python 2024)

Goes deeper into `dict` than `pythonExercises/zad4.py`. Verified against
actual output.

```python
d1 = {}
d1['zwierz'] = 'pies'   # assigning to a new key adds it
d1[78] = 514              # keys don't have to be strings — any hashable type works

d2 = {"klucz": "wartość", 123: 'abc', True: [1, 4, 6]}   # mixed key types in one dict
```
- **Dict keys can be any hashable type**, mixed freely in the same dict —
  strings, ints, even `bool` (`True`/`False`). Gotcha worth knowing:
  `bool` is technically a subtype of `int` (`True == 1`), so `True` and
  `1` would collide as the *same* dict key if both were used.

```python
d3 = dict()                          # empty dict via constructor (like list(), set())
dict1 = dict(zip(keys, values))       # build a dict directly from a zip() of two iterables!
dict2 = dict.fromkeys([1, 2, 3])       # {1: None, 2: None, 3: None} — same default value (None) for every key
dict3 = dict.fromkeys([1, 2, 3], 5)    # {1: 5, 2: 5, 3: 5} — custom default value for every key
```
- **`dict(zip(keys, values))`** — directly ties together the `zip()`
  concept from the notes' "concepts not yet covered" list with `dict`
  construction: `zip` pairs two iterables positionally, `dict(...)` turns
  those pairs straight into key→value entries in one call. This is
  exactly the same result as the `{state: capital for state, capital in
  zip(a, b)}` dict comprehension discussed earlier — `dict(zip(...))`
  is a shorter non-comprehension way to write the same thing when no
  transformation/filtering is needed.
- **`dict.fromkeys(iterable, default=None)`** — a dedicated constructor
  for "give me a dict with these keys, all sharing one default value."

```python
dict4 = {'a': 'valueA', 'b': 'valueB'}
dict4.get('a')          # 'valueA'
dict4.get('c')          # None — missing key, no error
dict4.get('c', 'brak')  # 'brak' — custom fallback instead of None
```
- **`dict.get(key, default=None)`** — reads a value **without raising**
  if the key is missing (unlike `dict4['c']`, which would raise
  `KeyError`). Optionally takes a fallback value to return instead of
  `None`. Safer than indexing when a key might not exist.

```python
dict5 = {"key1": "value1", "key2": "value2", "key3": "value3"}
'key2' in dict5          # True — `in` on a dict checks KEYS, not values
dict5.keys()               # dict_keys(['key1', 'key2', 'key3'])
dict5.values()             # dict_values(['value1', 'value2', 'value3'])
dict5.items()               # dict_items([('key1', 'value1'), ...])
```
- **`in` on a dict checks membership among keys only**, not values —
  `'value1' in dict5` would be `False` even though that string is a
  value in the dict.
- **`.keys()`/`.values()`/`.items()` return "view" objects**
  (`dict_keys`, `dict_values`, `dict_items`), not plain lists — they
  print differently (`dict_keys([...])`) and stay **live/in-sync** with
  the dict if it changes afterward, rather than being a frozen snapshot.
  Wrap in `list(...)` if you need an actual independent list.

```python
dict6 = {'python': 2.7, 97: 'a', 65: 'A'}
dict6['python'] = 3.0      # overwrite an existing key's value
del dict6[97]                # delete a key (del statement, same as del on a list slice earlier)
dict6.pop('python')          # removes AND returns the value for a key (like list.pop, but by key)
dict6.update({1: 2, 3: 56})  # merge another dict in
dict6.update({'one': "xd", 65: 10})
# → {65: 10, 1: 2, 3: 56, 'one': 'xd'}
```
- **`dict.pop(key)`** — same idea as `list.pop(index)` (removes and
  returns), but by **key** instead of by index.
- **`dict.update(other)`** — merges another dict's entries in.
  Interesting insertion-order detail confirmed by the actual output
  above: updating the value of an **existing** key (`65`) does **not**
  move it — it stays in its original position; only a genuinely **new**
  key (`'one'`) gets appended at the end. Dicts preserve insertion order,
  and `.update()` only affects that order for brand-new keys.

## 2026-09-27 — `5- petle - cz 1.py` / `5 - petle cz.2.py` (university/kolokwium python 2024)

Loop control flow: `continue`, `break`, and the distinctly-Python
`for`/`while`...`else` construct. Verified against actual output
(including simulating stdin for the `input()`-based `while` example).

```python
for litera in 'napis':
    print(litera)   # n, a, p, i, s — one character per iteration
```
- **Iterating a string directly** — no need for `list('napis')` first;
  a string is itself iterable, same as a file object
  (`4-pliki.py`) or a `range`.

```python
for element in lista_z_zerami:
    if element == 0:
        continue     # skip the rest of THIS iteration, move to the next one
    print(element)
```
- **`continue`** — immediately jumps to the next loop iteration, skipping
  any remaining code in the loop body for the current one. For
  `[1, 0, 0, 4, 5]`, the two `0`s never reach `print()`, but the loop
  keeps going afterward → prints `1, 4, 5`.

```python
for element in lista_z_zerami:
    if element == 0:
        break        # exit the loop ENTIRELY, right now
    print(element)
```
- **`break`** — stops the loop completely, right where it is (no more
  iterations at all, unlike `continue`). For the same list, this prints
  only `1` — the loop dies the moment it hits the first `0`.

```python
for element in lista:              # [1,2,3,4,5] — no zeros
    if element == 0:
        break
    print(element)
else:
    print("wykonano bez przerwania")   # runs — loop finished normally

for element in lista_z_zerami:      # has zeros
    if element == 0:
        break
    print(element)
else:
    print('wykonano bez przerwania')   # does NOT run — loop was broken out of
```
- **`for`/`while` loops can have an `else` clause** — this is a Python-
  specific construct with no direct equivalent in JS. **The `else` block
  runs only if the loop completes normally (runs out of items /
  condition becomes false), and is skipped entirely if the loop was
  exited via `break`.** Mental model: "else" here means "else, if we
  never broke out." Confirmed: `lista` (no zeros) reaches the `else` and
  prints the message; `lista_z_zerami` hits `break` on the first `0` and
  the `else` block never runs.
- Same rule applies to **`while`...`else`** (`5 - petle cz.2.py`):
  ```python
  s = ''
  while s != 'b':
      s = input()
      if len(s) == 3: break
  else:
      print('nie uzyto breaka')
  ```
  If the user types a 3-character string, `break` fires and the `else`
  is skipped (nothing printed). If they eventually type `'b'` without
  ever entering exactly 3 characters, the `while` condition naturally
  becomes `False`, the loop ends without a `break`, and `else` runs,
  printing `'nie uzyto breaka'` ("break wasn't used"). Both cases
  verified by feeding simulated input.

```python
for ((a, b), c) in zip([(1, 'a'), (2, 'b'), (3, 'c')], [4, 5, 6]):
    print(a, b, c)              # 1 a 4  /  2 b 5  /  3 c 6

for (a, b) in zip([(1, 'a'), (2, 'b'), (3, 'c')], [4, 5, 6]):
    print(a, b)                 # (1, 'a') 4  /  (2, 'b') 5  /  (3, 'c') 6

for a in zip([(1, 'a'), (2, 'b'), (3, 'c')], [4, 5, 6]):
    print(a)                    # ((1, 'a'), 4)  /  ((2, 'b'), 5)  /  ((3, 'c'), 6)
```
- **Nested unpacking in a `for` loop.** `zip(...)` here pairs each tuple
  `(n, letter)` with a plain int, producing items shaped like
  `((1, 'a'), 4)`. How much you unpack on the left is up to you:
  - `for ((a, b), c) in ...` — unpacks **both levels**: `a`/`b` come from
    inside the inner tuple, `c` is the int.
  - `for (a, b) in ...` — unpacks only the **outer** level: `a` becomes
    the whole inner tuple `(1, 'a')` (still packed), `b` becomes the int.
  - `for a in ...` — **no unpacking at all**: `a` is the entire pair
    `((1, 'a'), 4)`.
  This is the same "unpacking pattern shape must match how much you want
  to pull apart" idea from `3-listy-i-krotki.py`'s
  `[la, lb, lc] = l`/`(x, y, z) = l`, just applied per-loop-iteration and
  showing it can nest to match nested tuple structure.

## 2026-09-27 — `5 - zmienne i obiekty.py` (university/kolokwium python 2024)

One of the most important files so far — Python's actual object model:
identity vs equality, aliasing, mutability's real consequences, shallow
vs deep copy, and even a self-referencing list. Verified against actual
output (exact `id()` numbers vary per run, but the *relationships*
between them are what matter and are stable).

```python
a = {}
b = {}
c = b
a == b     # True  — same CONTENT (both empty dicts)
a is b     # False — DIFFERENT objects in memory
b is c     # True  — SAME object (c is just another name for b)
a is c     # False
```
- **`==` checks value/content equality; `is` checks identity** (are these
  literally the *same object* in memory — same `id()`). Two separate
  empty dicts are `==` (equal content) but not `is` (different objects).
  `c = b` doesn't create a new dict — it just makes `c` another name
  pointing at the *same* object as `b`, so `b is c` is `True`.
- Proof this matters: mutating through one alias affects the other.
  `c[36] = 'z'` also shows up when printing `b`, since `b`/`c` are the
  same object — but `a` (a genuinely separate dict) is unaffected.

```python
l1 = []
l2 = l1          # alias — same list object
l1 += [1, 2, 3]
l2 += [4, 5, 6]
print(l1, l2)     # [1, 2, 3, 4, 5, 6]  [1, 2, 3, 4, 5, 6]  — BOTH have everything!

s1 = ''
s2 = s1           # alias — same string object (initially)
s1 += '123'
s2 += '456'
print(s1, s2)      # 123   456   — each has only its OWN addition
```
- **This is the single most important contrast in the file.** `l1 += [...]`
  on a **mutable** list *mutates the existing object in place* (same
  underlying list `l2` is still aliased to) — so both names see the
  combined result, since there was only ever one list. `s1 += '...'` on
  an **immutable** string *can't* mutate anything — it creates a brand
  new string object and rebinds only `s1` to it; `s2` still points at the
  original, untouched object, so `s1`/`s2` end up completely independent.
  Confirmed via `id()`: `s1`/`s2` share an id *before* the `+=`, but have
  **different** ids *after* — while `l1`/`l2` stay the same object
  throughout. Direct, concrete payoff of the mutable/immutable
  distinction from the type-system notes and the `set |=` behavior seen
  in `4 - zbiory.py`.

```python
a = [1, 2, 3]
b = a[:]          # full slice on a list = an actual independent COPY, not an alias!
del b[1]
print(a, b)        # [1, 2, 3]   [1, 3]  — only b changed
```
- **`a[:]` on a list makes a real (shallow) copy** — unlike `c = b`
  above. This is *the* idiom for "give me an independent copy of this
  list."

```python
d1 = {'a': [1, 2, 3]}
d2 = d1.copy()          # dict.copy() is a SHALLOW copy
d2['a'].append(4)
print(d1, d2)             # {'a': [1, 2, 3, 4]}  {'a': [1, 2, 3, 4]}  — BOTH changed!

import copy
d3 = copy.deepcopy(d1)   # deepcopy is a TRUE independent copy, recursively
d3['a'].append(5)
print(d1, d2, d3)          # d1/d2 unaffected: {'a': [1,2,3,4]} twice; d3: {'a': [1,2,3,4,5]}
```
- **Shallow copy (`.copy()`, or `a[:]`) only copies the top-level
  container** — if that container holds *other mutable objects* (like a
  list nested inside a dict), those nested objects are still **shared**
  between the original and the copy. Mutating the nested list through
  `d2` also shows up in `d1`, because `d1['a']` and `d2['a']` are
  literally the same list object — only the outer `dict` was actually
  copied.
- **`copy.deepcopy(x)`** — recursively copies *everything*, including
  nested mutable objects, giving you a truly independent structure.
  `d3['a']` is its own separate list, so mutating it doesn't touch `d1`
  or `d2` at all.

```python
a = [1, 2]
a.append(a)         # a list containing ITSELF
print(a)             # [1, 2, [...]]  — Python detects the cycle, prints [...] instead of looping forever
print(a is a[2])      # True — a[2] IS a, literally
print(a[2][2][2])      # [1, 2, [...]] — chasing the self-reference any number of times just gets back `a`
```
- **A list (or dict) can contain a reference to itself.** Since Python
  containers hold *references*, not copies, `a.append(a)` puts a
  reference to `a` inside `a`. Printing something with a circular
  reference doesn't infinite-loop — Python's `repr()` detects the cycle
  and prints `[...]` as a placeholder instead.

```python
isinstance(1, int)      # True
isinstance(1, str)       # False
isinstance(True, bool)    # True
isinstance(True, int)     # True — bool IS a subclass of int (confirms the earlier
                            #        True/1 dict-key-collision note from 4-słowniki.py)
```
- Concrete confirmation of the `bool` subclass-of-`int` fact mentioned
  earlier: `isinstance(True, int)` is `True` because `bool` inherits from
  `int` — `isinstance()` (unlike `type() ==`) respects that inheritance
  relationship.

```python
napis = '7 skrzyń fig'
stats = {'cyfry': 0, 'litery': 0, 'spacje': 0}
for litera in napis:
    if litera.isdigit():
        stats.update({'cyfry': stats.get('cyfry') + 1})
    elif litera.isalpha():
        stats.update({'litery': stats.get('litery') + 1})
    elif litera.isspace():
        stats.update({'spacje': stats.get('spacje') + 1})
print(stats)   # {'cyfry': 1, 'litery': 9, 'spacje': 2}
```
- **`str.isdigit()` / `.isalpha()` / `.isspace()`** — character-type
  checks; `.isalpha()`/`.isdigit()` already seen in
  `pythonExercises4/zad4.py`'s password generator, `.isspace()` new here
  (checks for whitespace characters).
- **Manual counter pattern**: `stats.get('key') + 1` (safe read, avoids
  `KeyError`) combined with `.update({'key': ...})` to write back — this
  is exactly the kind of thing `collections.Counter` exists to simplify
  (not covered yet, but worth knowing the name — it's a `dict` subclass
  built specifically for counting things, avoiding this manual
  get-then-update dance).

## 2026-09-27 — `5-funkcje.py` (university/kolokwium python 2024)

Short file, no genuinely new syntax — mostly a plain function definition
(`def user(imie, nazwisko): return imie + ' ' + nazwisko`, same shape as
`pythonExercises/zad5.py`) plus one worthwhile reinforcement:

```python
def wypisz(a):
    for x in a:
        print(x)

wypisz('abcde')                        # works — iterates characters
wypisz([1,2,3,4,5,6,7,8,9,10])          # ALSO works — iterates list elements
```
- **Concrete demonstration of duck typing** (concept introduced earlier
  via PyCharm's `{__le__, __add__}` inferred hints in
  `pythonExercises3/zad1.py`, and in the type-system notes). `wypisz(a)`
  never declares what type `a` should be — it just does `for x in a:`.
  Since both a `str` and a `list` are iterable, the exact same function
  body works correctly on either, with zero type checking or branching.
  Python doesn't care that one call passes a string and the other a list
  — it only cares that whatever's passed *supports iteration*.

## 2026-09-27 — `5-prawda-i-falsz.py` (university/kolokwium python 2024)

Truthiness, made explicit with `bool()`, plus `or`/`and` returning actual
values rather than plain booleans. Verified against actual output.

```python
bool([])       # False
bool(0)        # False
bool(0.0)      # False
bool('')       # False
bool(None)     # False
bool({})       # False
bool(())       # False
bool(set())    # False

bool([0])      # True !
```
- **`bool(x)`** explicitly converts anything to `True`/`False` using
  Python's truthiness rules — makes concrete the truthy/falsy checks
  already relied on implicitly in earlier files (`if
  product_without_white_characters:` in `pythonExercises/zad4.py`,
  `if numbers_of_elements_per_set:` in `pythonExercises2/zad4.py`).
  **Every built-in "empty" value is falsy**: `0`, `0.0`, `''`, `None`,
  and every *empty* container (`[]`, `{}`, `()`, `set()`) regardless of
  its type.
- **`bool([0])` is `True`** — an important distinction: a **non-empty**
  container is truthy *even if the thing inside it is itself falsy*.
  Only the container's own emptiness matters for its own truthiness, not
  what's stored inside it. `[0]` has one element, so it's a non-empty
  list → truthy, even though that one element (`0`) is falsy on its own.

```python
[] or {} or 0            # 0      — none truthy, returns the LAST value
[] or 'kot' or 0          # 'kot'  — first truthy value, short-circuits (0 never evaluated)
1 or 2                     # 1      — first operand already truthy, stops there
2 or 1                     # 2

'dom' and {1: 'p'} and 78    # 78     — all truthy, returns the LAST value
'dom' and {} and 78           # {}     — first falsy value, short-circuits (78 never evaluated)
```
- **`or`/`and` return one of their actual operand values, not just
  `True`/`False`** (same behavior as JS's `||`/`&&`). Both **short-circuit**
  (stop evaluating as soon as the outcome is decided) and scan
  left-to-right:
  - **`or`** stops at the **first truthy** value and returns it; if none
    are truthy, returns the **last** operand.
  - **`and`** stops at the **first falsy** value and returns it; if none
    are falsy, returns the **last** operand.
- Practical patterns this enables: `x or 'default'` — "use `x` if it's
  non-empty/non-zero, otherwise fall back" (like JS's
  `x || 'default'`); `user and user.name` — "only access `.name` if
  `user` is truthy/exists," Python's rough equivalent of JS optional
  chaining (`user?.name`), built from a general-purpose operator rather
  than dedicated syntax.

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

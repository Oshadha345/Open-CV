# Python’s `sys` module
---

## 1. What is `sys`?

The `sys` module provides access to interpreter-level variables and functions. Anything that’s about your Python runtime, the command-line args you passed in, or the standard I/O streams lives in `sys`.

```python
import sys
```

---

## 2. `sys.argv` – your script’s command-line arguments

- __Type__ : list of strings
- `sys.argv[0]` is the script name, the rest are whatever typed after it


```bash
$ python myscript.py foo 123
```

```python
import sys

print(sys.argv) # --> ['myscript.py','foo','123']
```

Use it to read inputs without a full CLI parser.

---

## 3. `sys.exit()`- terminate with a status code


- `sys.exit(0)` -> clean exit
- `sys.exit(1)` or any non-zero  -> signals an error to the OS

```python
import sys

if len(sys.argv) < 2:
    sys.exit("❌ Usage: python myscript.py <arg>")

# ... rest of your code
```

---

## 4. `sys.stdin`, `sys.stdout`, `sys.stderr` - low-level I/O streams

These are file-like objects you can read/write directly—useful for piping.

```python
import sys

# Echo everything from stdin to stdout:
for line in sys.stdin:
    sys.stdout.write(f"> {line}")
```

Anything you write to `sys.stderr` will still show up on the console but won’t get mixed in if someone redirects stdout to a file.

---

## 5. Runtime Information

- `sys.version` - the full Python version string
- `sys.platform`- OS/platform identifier
- `sys.path`    - list of directories python search when `import`


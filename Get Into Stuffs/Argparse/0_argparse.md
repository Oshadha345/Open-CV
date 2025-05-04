# ArgParse

---

## 🧠Why `argparse`?

Imagine you build a program that resizes images. Instead of hardcoding values inside your script, wouldn’t it be better if users could run it like:

```bash
python resize.py input.jpg --width 300 --height 200
```
This is where `argparse` shines: it turns __terminal arguments__ into __Python variables__ effortlessly.

---

## 🔍 BREAKDOWN OF KEY OPTIONS

| Method                     | What it does                             |
| -------------------------- | ---------------------------------------- |
| `add_argument()`           | Adds a new input to your script          |
| `type=int` or `type=float` | Converts the input to the correct type   |
| `choices=[]`               | Restricts the value to a given list      |
| `action="store_true"`      | Turns a flag into a Boolean (True/False) |
| `required=True`            | Makes an optional arg required           |
| `help="..."`               | Adds helpful info for `--help` screen    |

- refer to `Calculator_CLI.py` to see how above commands applied in practice
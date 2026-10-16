# Session 03 Exit Ticket

**Topic:** Lists, Tuples, Sets and Dictionaries

## 1. Which operation or function was most useful?

The set operators (`-`, `&`, `|`). One line like `required - observed` replaced a whole loop with `if` checks. `setdefault()` was also handy, because it creates the `tags` list only if it is missing and lets me `append` in the same line.

## 2. What input caused the most interesting result?

Luis, the student with an empty grades list. Calculating `sum([]) / len([])` would crash with a division by zero, so `average()` checks `if not grades` and returns `None`. The duplicate `"food"` in the `observed` set was also interesting: sets silently keep only one copy.

## 3. Which check proves that your code works?

The `assert` statements in the final challenge, especially `assert average("S2") is None` and `assert ranked == [(8.5, "Ana")]`. Together they prove that missing grades are handled safely and the ranking is correct, and the cell prints `All checks passed`.

## 4. What would you reuse in the cumulative project?

- A dictionary indexed by ID, built from a list of records (`by_id`)
- The `average()` function with its `None` guard
- A set to collect unique values
- `assert` checks to confirm each step still works

[![codecov](https://codecov.io/gh/lancasterg/pysafe-config/branch/main/graph/badge.svg)](https://codecov.io/gh/USERNAME/REPOSITORY)

# pysafe-config

`pysafe-config` is a lightweight Python library designed to simplify the process of reading environment variables.

It provides a set of four fully type-hinted public functions to read environment variables, one for each of the following types `{str, int, float, bool}`.

### Links
- [pypi](https://pypi.org/project/pysafe-config/)
- [docs](https://lancasterg.github.io/pysafe-config/)

## Why it exists

### The Problem: Boilerplate and Error-Prone Environment Variable Handling

Handling environment variables isn't something you should be worrying about when writing an application or service in Python. 
However, it can involve writing repetitive and error-prone code, especially when dealing with large numbers of environment variables requiring casting to their expected types. 
Other libraries exist to help manage your environment ([Dynaconf](https://www.dynaconf.com/), [py-dotenvsafe](https://pypi.org/project/py-dotenv-safe/)), but what if you just want a type-aware (and as type-safe as possible in Python!) version `os.getenv`?


Consider the common scenario of retrieving an environment variable, `SAMPLING_RATIO` as a float:

```python
import os
SAMPLING_RATIO = os.getenv("SAMPLING_RATIO", None)

if SAMPLING_RATIO is None:
    raise RuntimeError("SAMPLING_RATIO is unset")
else:
    SAMPLING_RATIO = float(SAMPLING_RATIO)
```

This approach is susceptible to `ValueError` if the conversion fails, requires explicit checks for `None` in the case that the variable is unset, and potentially requires additional validation for weird edge-cases like `"-inf"`.

### The Solution: `pysafe-config`

`pysafe-config` streamlines this process, allowing you to retrieve and validate environment variables with minimal code. The previous example can be reduced to a single clear line.

```python
from pysafe_config import getenv_float

SAMPLING_RATIO: float = getenv_float("SAMPLING_RATIO")

# or, for non-critical env vars

SAMPLING_RATIO: float | None = getenv_float("SAMPLING_RATIO", required=False)
```



## Features and Benefits

*   **Strict By Default**: Raises an exception if no environment variable is set by default, unless it has explicitly been marked as optional, preventing silent failures.
*   **Consistent Validation**: Enforces strict, consistent and reliable validation rules for different types, using a sensible and deterministic approach.
*   **Clear and Verbose Error Messages**: Provides descriptive error messages for missing or invalid environment variables.
*   **Reduced Boilerplate**: Significantly cuts down the amount of code needed to read and validate environment variables.
*   **Type Safety**: Works with all modern type linters. No more checking for Nones and raising errors in config files.

## Installation

#### poetry
```bash
poetry add pysafe-config
```

#### pip
```bash
pip install pysafe-config
```

## Usage

The default behaviour is that a `RuntimeError` will be raised if the variable is missing, or a `ValueError` if the type conversion fails.
This behaviour can be switched off if the function is called with `required=False`

```python
from pysafe_config import (
    getenv_int,
    getenv_str,
    getenv_bool,
    getenv_float,
)
# Optional string with a default value
LOG_LEVEL: str | None = getenv_str("LOG_LEVEL", default="INFO", required=False)

# Required integer - raises a RuntimeError if MAX_RETRIES is unset
MAX_RETRIES: int = getenv_int("MAX_RETRIES")

# Required boolean with no default -  raises a RuntimeError if DEBUG_MODE is unset
DEBUG_MODE: bool = getenv_bool("DEBUG_MODE", required=True)

# Optional float with no default value - can return None
SCALING_FACTOR: float | None = getenv_float("SCALING_FACTOR", required=False)

# Required boolean - raises a ValueError if RETURN_UPSTREAM_ERRORS is not a sensible boolean value
RETURN_UPSTREAM_ERRORS: bool | None = getenv_bool("RETURN_UPSTREAM_ERRORS")
```

### Supported Boolean Values

`pysafe-config` provides robust parsing for boolean environment variables. The following case-insensitive values are recognised:

| True values | False values |
|-------------|--------------|
| "true"      | "false"      |
| "1"         | "0"          |
| "yes"       | "no"         |
| "y"         | "n"          |
| "on"        | "off"        |
| "enable"    | "disable"    |
| "enabled"   | "disabled"   |
| "t"         | "f"          |

### Supported Float Values

Float values must adhere to a strict format:

*   Contain only digits (`0-9`), optionally preceded by a single `+` or `-` sign.
*   Include exactly one decimal point to separate the whole and fractional parts.
*   Not contain any whitespace, commas, or alphabetic characters.

| Valid strings | Invalid strings |
|---------------|-----------------|
| "50.2"        | "50"            |
| "-0.0"        | "5.5.5"         |
| "+1000.5"     | " 12.3"         |
| "-99.0"       | "12,3"          |
| "0.0001"      | "ten"           |
| "+.5"         | "5."            |
| "-1.23"       | "" (empty)      |

### Supported Integer Values

Integer values must adhere to a strict format:

*   Contain only digits (`0-9`), optionally preceded by a single `+` or `-` sign.
*   Not contain any whitespace.
*   Not include decimal points, letters, or special symbols.

| Valid strings | Invalid strings |
|---------------|-----------------|
| "100"         | " 100"          |
| "1"           | "10.5"          |
| "-50"         | "1,000"         |
| "+1000"       | "12a"           |
| "0"           | "++5"           |
| "-0"          | "5-"            |
| "123456"      | "ten"           |
| "-123456"     | "" (empty)      |

## Contributing

Contributions are welcome! Please refer to the `CONTRIBUTING.md` for guidelines.

## License

This project is licensed under the MIT License.

## Release docs
The release process needs work, but for now:

1. Ensure to bump the version number in pyproject.toml
2. Get the names of the closed PRs since the last release 
3. Create a new release, paste in the names of the previous MRs into the changelog
4. Create the new tag, being sure to use the next version up since the previous release
5. Go to Actions and approve the github workflow
6. Once finished, try installing the latest version in a shell using `pip install pysafe-config`

## Future work
- Add a function for parsing enums from environment variables
- Add a function that allows the user to pass the type they are expecting into a get_env function
  - `get_env("NUM_ROWS", int, ...)`
- Test the error strings in error messages
- put build passing / failing tag on repo
- put code coverage tag on repo (It is 100%)
- Create a web page for proper docs
# Example usage

```bash
pip install pysafe-config
# or
poetry add pysafe-config
```

Export the env vars:
```bash
export NUM_PRINTS=5
export MESSAGE="Hello user"
```

Run the example


```python
from pysafe_config import getenv_int, getenv_str, getenv_bool

NUM_PRINTS: int = getenv_int("NUM_PRINTS")
MESSAGE: str = getenv_str("MESSAGE")
RUN_EXAMPLE: bool = getenv_bool("RUN_EXAMPLE", default=True, required=False)


def print_message_n_times():
    for i in range(NUM_PRINTS):
        print(f"{MESSAGE} {i}")


def main():
    if RUN_EXAMPLE:
        print_message_n_times()
    else:
        print("Do nothing")

if __name__ == "__main__":
    main()
```

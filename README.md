# DontTrust

Don't trust your users! Form validation library for Python.

## Quick install

```shell
pip install donttrust
```

## Usage

Donttrust is not limited to any framework and has no dependencies. Just import it and you're good to go!

```python
# Example usage
from donttrust import DontTrust, Schema, ValidationError

trust = DontTrust(username=Schema().string().required().alphanum(),
                  password=Schema().string().required(),
                  remember_me=Schema().boolean().default(False))

try:
    data = trust.validate(username="hello123", password="abcdefg")
    # data["username"], data["password"] ...
except ValidationError as e:
    print(e.field, e.message)
    # Other error handling
```

For more info and examples, visit the docs

## Development

1. Clone or fork this repo
2. Make your changes
   > Note: Do **NOT** change the version number in `setup.py`. I'll do that myself.
3. Run the tests in the `/tests` directory (Done automatically with Github Actions)
4. PR and away!

---
title: "Boolean Schema"
order: 7
description: "Learn about the BooleanSchema"
keywords: "donttrust,form,validation,boolean,schema"
slug: "boolean-schema"
---

## Boolean schema

Makes the schema have a value of `True`, `False` or any truthy/falsy value.

```python
from donttrust import Schema

try:
  print(Schema().boolean().validate("test"))  # True
except:
  # No exception raised (because truthy)
```

```python
from donttrust.schema import BooleanSchema

try:
  print(BooleanSchema("field").validate(True))  # True
except:
  # No exception raised
```

## Methods

This schema has all of the methods of the base Schema class, and these ones too:

### `truthy(val1, val2)` and `falsy(val1, val2)`

`val1` and `val2` will be counted as truthy/falsy values respectively

<div class="w3-panel w3-pale-blue w3-border w3-leftbar w3-border-blue w3-padding">
  <h5>What are truthy and falsy values?</h5>
  <p>Truthy values are values that evaluate to true when they're converted to boolean. By default, these are: True, an int which is not 0, a non-empty str, etc.</p>
  <p>Falsy values are values that evaluate to false when they're converted to boolean.
  By default, these are: False, 0, an empty str/list/dict, etc.</p>
</div>

```python
schema = Schema().boolean().truthy("yes").falsy("no")

print(schema.validate(True))  # True
print(schema.validate(0))  # False
print(schema.validate("no"))  # False
print(schema.validate("yes"))  # True
```

### `strict()`

Only allow `True` and `False` to be accepted as values. This overrides `truthy()` and `falsy()`.

```python
schema = Schema().boolean().strict()

print(schema.validate(0))  # Exception
print(schema.validate(False))  # False
print(schema.validate(True))  # True
print(schema.validate(""))  # Exception
```

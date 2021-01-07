---
title: "String Schema"
description: "Learn about the StringSchema"
keywords: "string,schema,donttrust,form,validation"
slug: "string-schema"
order: 5
---

## String schema

Makes the schema to have a value with the `str` type.

```python
from donttrust import Schema

try:
  print(Schema().string().validate(123))
except:
  # Exception raised
```

```python
from donttrust.schema import StringSchema

try:
  print(StringSchema("field").validate("test"))  # test
except:
  # No exception raised
```

## Methods

This schema has all of the methods of the base Schema class, and these ones too:

### `allow_empty()`

Allows empty strings

### `min(length1)` and `max(length2)`

Makes the string be alteast `length1` characters and/or be greater than `length2` characters.

```python
try:
  print(Schema().string().min(1).max(4).validate("abcde"))
except:
  # Exception raised
```

### `lower()` and `upper()`

The validated value has to be lowercase / uppercase respectively.

```python
try:
  print(Schema().string().lower().validate("ASFasdsa"))
except:
  # Exception thrwon
```

### `alphanum()`

The validated value has to be alphanumeric

```python
print(Schema().string().alphanum().validate_without_exception("test123"))  # test123
```

### `regex(pattern)` and `flags(flag)`

String should match the regex pattern `pattern` with the flag `flag`.

```python
import re

print(Schema().string().regex(r"\w").flag(re.I).validate_without_exception("@@"))  # False
```

### `strip()`, `to_lower()` and `to_upper()`

Strips/Lowercases/Uppercases the value after validation (if validation succeedes, that is).

```python
print(Schema().string().to_lower().strip().validate_without_exception("   HELLO    "))  # hello
```

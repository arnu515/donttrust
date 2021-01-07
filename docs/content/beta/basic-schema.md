---
title: "Basic Schema"
description: "Get to know the base schema of DontTrust"
keywords: "donttrust, schema, basic, form, validation"
slug: basic-schema
order: 3
---

## The Basic Schema

The [Basic Schema](/apiref/docstrings/donttrust.html?highlight=schema#donttrust.schema.Schema) is the main Schema for form validation. It isn't restricted to any type. All other schemas inherit this schema.

## Usage

Import:

```python
from donttrust import Schema
# OR
from donttrust.schema import Schema
```

Create:

```python
schema1 = Schema("username").required().disallow("admin")

schema2 = Schema().required()

schema3 = Schema()
```

Validate:

```python
try:
  schema1.validate("admin")
except:
  # Catch exceptions here

# Without an exception:
v = schema1.validate_without_exception("admin")
print(v)  # False

v = schema2.validate(10)
print(v)  # 10
```

## Methods

### `required()`

It makes the field required. If this method is called and the field is `None` and NOT any another falsy value (like `False` or `0`).

```python
try:
  v = Schema().required().validate(None)
  print(v)
except:
  # Exception is thrown
```

### `default(value)`

This value is returned if the validated value is `None`. Does NOT work with `required`.

```python
try:
  v = Schema().default("test").validate(None)
  print(v)  # test
except:
  # No exception thrown
```

### `allow(value1, value2, ...)`

Only `value1`, `value2`, etc will be allowed as valid values for the schema, i.e. they will be whitelisted.

```python
try:
  v = Schema().allow("test").validate("invalid value")
  print(v)
except:
  # Exception is thrown
```

### `disallow(value1, value2, ...)`

Don't allow `value1`, `value2`, etc to be valid values of the Schema, i.e. they will be blacklisted.

```python
try:
  v = Schema().disallow("test", "a", "b").validate("test")
  print(v)
except:
  # Exception is thrown
```

<div class="w3-panel w3-pale-yellow w3-text-yellow w3-border w3-leftbar w3-border-yellow w3-padding">
  <strong>Warning:</strong> If you use both <code>allow()</code> and <code>disallow()</code>, <code>disallow()</code> will be preferred.
</div>

### `reset_allow()` and `reset_disallow()`

Resets the whitelist and blacklist respectively.

```python
try:
  v = Schema().disallow("test").reset_disallow().validate("test")
  print(v)  # test
except:
  # No exception thrown
```

### `validate(value)`

The function we've been seeing so much! Validates the schema with the value and raises an exception which will inherit [`DontTrustBaseException`](/apiref/docstrings/donttrust.html#donttrust.exceptions.DontTrustBaseException) if validation fails.

```python
import donttrust

try:
  print(donttrust.Schema().required().validate(None))
except donttrust.exceptions.DontTrustBaseException as e:
  # Handles all exceptions raised by DontTrust (except ValidationError, but more on that later)
  print(e.message)
```

### `validate_without_exception(value)`

Same as `validate`, but returns `False` instead of raising exception when validation fails.

```python
schema = Schema("field").required()

print(schema.validate_without_exception("abc"))  # abc
print(schema.validate_without_exception(None))  # False
```

<div class="w3-panel w3-pale-yellow w3-border w3-leftbar w3-border-yellow w3-padding">
  <strong>ATTENTION!</strong>

  <pre><code class="language-python">schema = Schema().required()

print(schema.validate_without_exception(None))  # False
print(schema.validate_without_exception(False))  # False</code></pre>
</div>

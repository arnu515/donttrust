---
title: "The DontTrust Object"
description: "Learn to create a validation object by combining multiple schemas"
keywords: "donttrust,object,schema,form,validation"
slug: "donttrust-object"
order: 10
---

The DontTrust object allows you to combine multiple schemas as one to make validation easier.

## Syntax

First, import the classes

```python
from donttrust import DontTrust, Schema
```

Then, create the object

```python
trust = DontTrust(fieldname=Schema().whatever())
```

To validate,

```python
print(trust.validate(fieldname="value"))
```

The fieldname MUST be the same as defined above.

You can also use a dictionary:

```python
print(trust.validate({"fieldname": "value"}))
```

Other methods for validation:

- `validate`
- `validate_and_return_json_object`
- `validate_without_exception`

## Methods

### `validate(dictionary OR **kwargs)`

Validate a dictionary or key-word separated arguments. Raises exception if validation fails.

### `validate_and_return_json_object(dictionary OR **kwargs)`

Same as `validate`, but returns a dictionary with `{"error": error_message, "field": field_name}` if validation fails and `{"data": data}` if it succeedes.

### `validate_without_exception(dictionary OR **kwargs)`

Same as `validate`, but returns `False` instead of throwing errors.

## Errors thrown

This object throws the [`donttrust.ValidationError`](/apiref/docstrings/donttrust.html?highlight=validationerror#donttrust.ValidationError) if validation fails, unlike normal Schemas, which throw an instance of `DontTrustBaseException`.

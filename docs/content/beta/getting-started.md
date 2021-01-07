---
title: "Getting Started"
order: 2
slug: "getting-started"
description: "Learn how to get started with DontTrust"
keywords: "donttrust,python,get,started"
---

## Basic example

Let's look at a really simple example using the `Schema()` class.

```python
from donttrust import Schema

# "username" is the name of the field.
# It is used to format error messages.
# This is optional, but recommended.
schema = Schema("username").string().required()

try:
    schema.validate("abcdefg")
except Exception as e:
    print(e)
    # Other error handling
```

Analysing the above example, we can see that we called the `Schema()` class with the field name as `username`.

This Schema is then made into a `StringSchema` and is then made required.

Finally, we validate the schema with the `validate(value)` function.

We put the validation logic in a `try...except` block because the `validate` function will throw an error if there's an error in validation. Use the `validate_without_exception` function to not throw an exception and just return `False` if there's an error in validation.

## Types of Schemas

Currently, DontTrust supports these schemas:

- `string`
- `number` including `int`, `float` and `complex`
- `boolean`
- `date`
- `email`

### Use a specific schema

To use a schema of a certain datatype,

```python
from dontrust import Schema

schema = Schema("field").string()
schema = Schema("field").number()
# ...
```

The general syntax is `Schema().DATATYPE()` where `DATATYPE` can be any of the types listed above.

#### Alternative method

You can directly import a Schema class from `donttrust.schema` without using `Schema().DATATYPE()`.

```python
from donttrust.schema import StringSchema
from donttrust.schema import BooleanSchema
from donttrust.schema import NumberSchema
from donttrust.schema import EmailSchema
from donttrust.schema import DateSchema
```

<div class="w3-panel w3-pale-blue w3-border w3-leftbar w3-border-blue w3-padding">
  In these schemas, the <code>field</code> parameter (<code>Schema(field)</code>) is <b>required</b>
</div>

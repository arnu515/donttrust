---
title: "Number Schema"
order: 6
description: "Learn about the NumberSchema"
keywords: "donttrust,form,validation,number,schema"
slug: "number-schema"
---

## Number schema

Makes the schema to have a value of `int`, `float` or `complex` (`int` by default).

```python
from donttrust import Schema

try:
  print(Schema().number().validate("test"))
except:
  # Exception raised
```

```python
from donttrust.schema import NumberSchema

try:
  print(NumberSchema("field").validate(123))  # test
except:
  # No exception raised
```

## Methods

This schema has all of the methods of the base Schema class, and these ones too:

### `min(l1)` and `max(l2)`

Requires the number to be &lt; l2 and/or &gt; l1.

```python
print(Schema().number().min(-5).max(-2).validate_without_exception(1))  # False
```

### `equals(num)`

The number must equal `num`

```python
print(Schema().number().equals(5).validate(5))  # 5
```

### `port()`

Requires the number to be a valid port (&gt;`0` &amp; &lt;`65535`)

### `positive()` and `negative()`

The number should be either positive
(including `0`) or negative (excluding `0`) respectively

### `int()`, `float()` and `complex()`

Requires that the number should be of type `int`, `float` or complex. Integer by default.

```python
print(Schema().number().validate)
```

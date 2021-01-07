---
title: "Email Schema"
order: 8
description: "Learn about the EmailSchema"
keywords: "donttrust,form,validation,email,schema"
slug: "email-schema"
---

## Email schema

Makes the schema have a value of a valid email.

```python
from donttrust import Schema

try:
  print(Schema().email().validate("test"))
except:
  # Exception raised
```

```python
from donttrust.schema import EmailSchema

try:
  print(EmailSchema("field").validate("test@gmail.com"))  # test@gmail.com
except:
  # No exception raised
```

## Methods

This schema has all of the methods of the base Schema class, and these ones too:

### `allow_tlds(a, b, c, ...)` and `disallow_tlds(a, b, c, ...)`

Allows or disallows the top-level domains `a`/`b`/`c` respectively. A top level domain is `.com`, `.net`, etc.

Behaves similar to `allow()` and `disallow()`, where `disallow` is preferred over `allow`.

```python
print(Schema().email().allow_tlds(".com").validate("test@email.org"))  # Exception thrown
```

### `allow_mail_providers(a, b, ...)` and `disallow_mail_providers(a, b, ...)`

Allows/disallows emails with mail providers `a` and `b`.

```python
print(Schema.email().disallow("gmail").validate("test@gmail.com"))  # Raises exception
```

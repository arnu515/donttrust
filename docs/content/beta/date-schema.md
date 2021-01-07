---
title: "Date Schema"
order: 9
description: "Learn about the DateSchema"
keywords: "donttrust,form,validation,date,schema"
slug: "date-schema"
---

## Date schema

Makes the schema have a value of a valid date. This date can be a timestamp, a `datetime.datetime()` object, or a valid `ISO` date string.

```python
from donttrust import Schema

try:
  print(Schema().date().validate("test"))
except:
  # Exception raised
```

```python
from donttrust.schema import DateSchema

try:
  print(DateSchema("field").validate("2020-10-04"))  # datetime.datetime(2020, 10, 04)
except:
  # No exception raised
```

## Methods

This schema has all of the methods of the base Schema class, and these ones too:

### `min(date1)` and `max(date2)`

Date has to be greater than `date1` and/or less than `date2`.

`date1` and `date2` support the same values as the main `DateSchema` class, but with an additional value of `today`, which just infers to today's date.

```python
from datetime import datetime
from donttrust.schema import DateSchema

print(DateSchema("DOB").min(datetime(1950, 1, 1)).max('today'))
```

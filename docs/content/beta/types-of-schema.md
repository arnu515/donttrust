---
title: "Other types of Schema"
slug: "types-of-schema"
keywords: "donttrust, form, validation, schema, type"
description: "Learn the different types of schemas in DontTrust"
order: 4
---

## Types of schema

There are many different types of schemas, namely:

- `string`
- `number`
- `boolean`
- `date`
- `email`

### Changing the schema type:

There are two ways to change the type of a schema:

```python
# 1. Use the Schema.TYPE() function:

from donttrust import Schema

schema = Schema().string()
schema = Schema().number()
schema = Schema().boolean()
schema = Schema().date()
schema = Schema().email()
```

OR

```python
# 2. Directly use the class

from donttrust.schema import StringSchema
from donttrust.schema import BooleanSchema
from donttrust.schema import NumberSchema
from donttrust.schema import EmailSchema
from donttrust.schema import DateSchema

schema = StringSchema("fieldname")
schema = BooleanSchema("fieldname")
schema = NumberSchema("fieldname")
schema = EmailSchema("fieldname")
schema = DateSchema("fieldname")
```

<div class="w3-panel w3-pale-blue w3-border w3-leftbar w3-border-blue w3-padding">
  When you use the second method, you HAVE to fill the <code>field</code> parameter.
</div>

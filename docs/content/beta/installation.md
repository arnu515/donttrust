---
title: "Installation"
order: 1
slug: "installation"
description: "Learn how to install DontTrust to your python project using either pip or setup.py"
keywords: "donttrust,python,install,pip,setup.py"
---

## Installing using pip

Create a virtualenv first (Optional):

```sh
python3 -m venv venv
source venv/bin/activate
# Windows
# venv\Scripts\activate
```

Install with pip using

```sh
pip install donttrust
```

## Using `setup.py`

1. Clone the repo (requires [git](https://git-scm.com) installed):

```sh
git clone https://github.com/arnu515/donttrust.git donttrust
cd donttrust
```

2. Install

```sh
python3 setup.py install
```

## Use

Now, you can use the library

```python
from donttrust import DontTrust, Schema

trust = DontTrust(test=Schema().string())

data = trust.validate_and_return_json_object(test="abcd")
```

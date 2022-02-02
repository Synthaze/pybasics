# pybasics - 0.3

Basic utils in Python.

## Install

```python
pip3 install pybasics
```

## Examples

```python

# Read/Write text files
from pybasics import read_file
from pybasics import write_file

str_data = read_file('data.dat', split=False)
write_file('data.dat', str_data, mode='w', join=False)


# Read/Wite json files and pretty print
from pybasics import read_json
from pybasics import write_json
from pybasics import pretty_json

json_data = read_json('data.json')
pretty_json(json_data)
write_json('data.json', json_data)


# Read/Write pickle binary files
from pybasics import read_pickle
from pybasics import write_pickle

pickle_data = read_pickle('data.pickle')
write_pickle('data.pickle', pickle_data)


# Get list of subdirectories in path
from pybasics import list_dir

subdirs = list_dir('.')


# Get filename with most recent modification in path
from pybasics import last_file

lastfile = last_file('.')


# Requests
from pybasics import try_except
from pybasics import webcheck

url = 'https://google.com'

if webcheck(url):
  # Run your code
  pass

data = try_except(url)


# Mongodb
from pybasics import mgdb
from pybasics import mgcol

mydb = mgcol('dbname', create=False, port=27017)
mycol = mgcol('dbname', 'colname', create=False, port=27017)
```

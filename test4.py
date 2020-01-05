import datetime
from flask import Flask
from werkzeug.contrib.cache import SimpleCache
from pathlib import Path

app = Flask(__name__)
app.secret_key = 'my secret key'
cache = SimpleCache()


mylist= ['a','b','c','d','e']

print(len(mylist))


cache.set('mycached_items', mylist, timeout=60*15 )


if 1 == 1:
    s = '******see what is in cache = \n'\
            f'{cache.get("mycached_items")[0]}***'

print(s)

print(f"this is my list .... {'.'.join([x for x in mylist])}")
out_file = '.'
p = Path(out_file)/ 'python' / 'scripts' / 'test.py'

print(f'{p}')

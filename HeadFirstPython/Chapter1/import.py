import os
from os import getcwd
import sys
import datetime
import time
import html
"""
This program is the second example in the book Head First Python

@author: Tiago Saraiva
@date: 2024-01-09
"""
print("--------------------------------------------------")
where_am_i = getcwd()
print(where_am_i)
print("--------------------------------------------------")
print(sys.platform)
print(sys.version)
print("--------------------------------------------------")
print(os.environ)
print(os.getenv('USERPROFILE'))
print("--------------------------------------------------")
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print("--------------------------------------------------")
formated_date = datetime.date.isoformat(datetime.date.today())
print(formated_date)
print("--------------------------------------------------")
print(time.strftime("%H:%M"))
print(time.strftime("%A %p"))
print("--------------------------------------------------")
print(html.escape("This HTML fragment contains a <script>script</script> tag."))
print(html.unescape("I &hearts; Python's &lt;standard library&gt;."))

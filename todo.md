## Todolist

1. clean environment , ModuleNotFoundError: No module named 'win32gui'
```
C:\work\nut\code\hook>python hook.py
Traceback (most recent call last):
  File "C:\work\nut\code\hook\hook.py", line 1, in <module>
    import clipboard_monitor
  File "C:\Users\caiyu\AppData\Local\Programs\Python\Python39\lib\site-packages\clipboard_monitor\__init__.py", line 1, in <module>
    import win32gui
ModuleNotFoundError: No module named 'win32gui'
```
pip install pywin32


Set WShell = CreateObject("WScript.Shell")
' Указываем путь к твоему виртуальному окружению Python и скрипту
WShell.Run """C:\Users\ymax1\Documents\GitHub\PC-controller\.venv\Scripts\python.exe"" ""C:\Users\ymax1\Documents\GitHub\PC-controller\server.py""", 0, False
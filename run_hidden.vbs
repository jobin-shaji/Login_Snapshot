' filepath: x:\Custom\mycustomlog\run_hidden.vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "x:\Custom\mycustomlog\hide_terminal.bat" & Chr(34), 0
Set WshShell = Nothing
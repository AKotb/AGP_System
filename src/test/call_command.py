import os

# ArcGIS Python Interpreter
arcinterpreter = r"C:\Python27\ArcGIS10.4\python.exe"

# Anaconda Python Interpreter
anainterpreter = r"C:\ProgramData\Anaconda2\python.exe"

python_script = r"C:\Users\ahmed.kotb\workspace\AGPS_PYT27\src\test\call_command2.py"
command = 'cmd /k "{0} {1}"'.format(arcinterpreter, python_script)
# case two parameters (for example):
# command = 'cmd /k "{0} {1} {2} {3}"'.format(interpreter, python_script, param1, param2)
os.system(command)
import cx_Freeze
import sys
import os
base=None
if sys.platform=="win32":
      base="win32GUI"
os.environ["TCL_LIBRARY"]=r"C:\Users\91962\AppData\Local\Programs\Python\Python37\tcl\tcl8.6"
os.environ["TK_LIBRARY"]=r"C:\Users\91962\AppData\Local\Programs\Python\Python37\tcl\tk8.6"
executables=[cx_Freeze.Executable("main.py",base=base,icon="icon.ico")]
cx_Freeze.setup(
      name="Vpad Text Editor",
      options={"build_exe":{"packages":["tkinter","os"],"include_files":["icon.ico","tcl86t.dll","tk86t.dll","icons2"]}},
      version="1.0",
      description="Desktop Application Made By Shivang Saxena",
      executables=executables
)

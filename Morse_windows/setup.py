import cx_Freeze
import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

executables = [cx_Freeze.Executable("morseCode.py")]

cx_Freeze.setup(
    name="Morse code",
    options={'build_exe':{'packages':['pygame'], 'include_files':['images/bg.jpg', 'images/f-1.png', 'images/type.png', 'audio/beep.wav'],
                          }}, executables=executables)

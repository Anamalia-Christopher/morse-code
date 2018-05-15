from setuptools import setup

APP = ["morseCode.py"]
APP_NAME = "Morse"
DATA_FILES = ["bg.jpg", "f-1.png", "type.png", "beep.wav"]

OPTIONS = {
    'argv_emulation': True,

    "iconfile": "morse_icon.icns"



}
setup(name=APP_NAME,
      app=APP,
      data_files=DATA_FILES,
      options={"py2app": OPTIONS},
      setup_requires=["py2app"]
)

# for the building , i had to do python setup.py -A and that was what worked
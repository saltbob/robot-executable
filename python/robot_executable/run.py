# Make imports explicit so that pyinstaller figures them out
import importlib
from robot.run import run
import SeleniumLibrary

from robot.libraries import (
    BuiltIn, Collections, DateTime, Dialogs, Easter,
    OperatingSystem, Process, Remote, Reserved,
    Screenshot, String, Telnet, XML)

def main():
    run("robot/bot.robot", outputdir="./output")

if __name__ == '__main__':
    main()

import os
import sys
import shutil
import requests
import contextlib
import platform
from pathlib import Path
from zipfile import ZipFile, ZipInfo

_local_path = os.path.realpath(os.path.dirname(__file__))

class ZipFileWithPermissions(ZipFile):
    """ Custom ZipFile class handling file permissions. """
    def _extract_member(self, member, targetpath, pwd):
        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)

        targetpath = super()._extract_member(member, targetpath, pwd)

        attr = member.external_attr >> 16
        if attr != 0:
            os.chmod(targetpath, attr)
        return targetpath


@contextlib.contextmanager
def pushd(new_dir):
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)

try:
    import serial
except ImportError:
    print("Installing pyserial module")
    res = os.system("pip3 install pyserial")
    if res != 0:
        print("pyserial module installation failed")
        sys.exit(1)
    import serial

if os.name == 'nt':  # sys.platform == 'win32':
    from serial.tools.list_ports_windows import comports
elif os.name == 'posix':
    from serial.tools.list_ports_posix import comports
else:
    raise ImportError("Sorry: no implementation for your platform ('{}') available".format(os.name))

# List of supported board USB IDs.  Each board is a tuple of unique USB vendor
# ID, USB product ID.
BOARD_IDS = \
    [{
        "name": "wio terminal",
        "info": ("2886", "802D"),
        "isbootloader": False
    },
    {
        "name": "wio terminal",
        "info": ("2886", "002D"),
        "isbootloader": True
    }]

def getAllPortInfo():
    return comports(include_links=False)

def getAvailableBoard():
    for info in getAllPortInfo():
        port, desc, hwid = info
        ii = hwid.find("VID:PID")
        #hwid: USB VID:PID=2886:002D SER=4D68990C5337433838202020FF123244 LOCATION=7-3.1.3:1.
        if ii != -1:
            for b in  BOARD_IDS:
                (vid, pid) = b["info"]
                if vid == hwid[ii + 8: ii + 8 + 4] and pid == hwid[ii + 8 + 5 :ii + 8 + 5 + 4 ]:
                    if b["isbootloader"] == True :
                        return port, True
                    else:
                        return port, False
    return None, False

def downloadFile(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

_ambd_flash_tool = Path(_local_path, "ambd_flash_tool")

def getFlashTool():
    if not _ambd_flash_tool.exists():
        zipfn = str(_ambd_flash_tool) + ".zip"
        downloadFile("https://github.com/Seeed-Studio/ambd_flash_tool/archive/refs/heads/master.zip", zipfn)
        with ZipFileWithPermissions(zipfn) as zf:
            zf.extractall(_local_path)
        Path(_local_path, "ambd_flash_tool-master").rename(_ambd_flash_tool)
    _tool = Path(_ambd_flash_tool, 'tool')
    _platform = platform.platform()
    if 'Windows' in _platform:
        _tool = str(Path(_tool, 'windows', "amebad_image_tool.exe"))
    elif 'Linux' in _platform:
        _tool = str(Path(_tool, 'linux', 'amebad_image_tool'))
    elif _platform.find('Darwin') >= 0 or _platform.find('macOS') >= 0:
        _tool = str(Path(_tool, 'macos', 'amebad_image_tool'))
    else:
        raise Exception("Platform not supported")
    return _tool

_port, _isbootloader = getAvailableBoard()
_tool = getFlashTool()

firmware = sys.argv[1]

with ZipFile(firmware) as zf:
    zf.extractall(_ambd_flash_tool)

with pushd(_ambd_flash_tool):
    os.system(f"{_tool} {_port}")

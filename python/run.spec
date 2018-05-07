# -*- mode: python -*-
from pathlib import Path

block_cipher = None

def get_robot_htmldata():
    import os
    import glob
    from itertools import chain

    import robot
    from robot.htmldata.template import HtmlTemplate

    robot_dir = os.path.dirname(robot.__file__)
    robot_folder = os.path.basename(robot_dir)
    html_base_dir = HtmlTemplate._base_dir
    common_path = os.path.commonpath([robot_dir, html_base_dir])

    def destination(source):
        return os.path.join(
            robot_folder,
            os.path.relpath(
                os.path.dirname(source), common_path
            )
        )

    return [
        (source, destination(source)) for source in
        chain(*(
            glob.glob(html_base_dir + f"\\**\\*.{ext}", recursive=True)
            for ext in ("html", "css", "js")
        ))
    ]

a = Analysis(['robot_executable\\run.py'],
             pathex=[Path('.')],
             binaries=[],
             # Add Robot Framework html report templates
             datas=[
                 *get_robot_htmldata(),
                 ((Path(".") / ".." / "robot" / "bot.robot").resolve(), "robot")
             ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='run',
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='run')

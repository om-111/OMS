# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['OMS.py'],
             pathex=['C:\\Users\\Om\\Desktop\\Builder'],
             binaries=[],
             datas=[('pdfreaders-f.png','.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='OMS',
          debug=False,
          icon='pdfreaders-f.ico',
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )

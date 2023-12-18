# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['Merge2PDF.py'],
    pathex=['.\\merge2pdf'],
    binaries=[],
    datas=[('../resources/icon', 'resources'), ('../resources/help.html', 'resources')],
    hiddenimports=['Merge2PDF_UI', 'utils', 'resources_rc'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Merge2PDF',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['..\\resources\\icon\\Merge2PDF_Icon.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Merge2PDF',
)

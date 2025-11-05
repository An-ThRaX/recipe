# -*- mode: python ; coding: utf-8 -*-
import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

# Collect Flet runtime and any other necessary data
datas = collect_data_files('flet')

# Include your SQLite DB
datas.append(('recipes.db', '.'))

# Include the assets
datas.append(('recipe_app/assets/', 'assets'))
# Main script
block_cipher = None

a = Analysis(
    ['recipe_app/main.py'],
    pathex=[str(Path(__name__).parent)],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='RecipeApp',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # GUI app, no console
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='RecipeApp'
)

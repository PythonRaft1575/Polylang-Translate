from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

setup(
    name="Polylang",
    version="1.0",
    description="Translation App",
    executables=executables,
)

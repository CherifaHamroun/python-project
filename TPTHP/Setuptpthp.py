from cx_Freeze import setup,Executable
setup(
    name = "TPTHP",
    version = "0.1",
    description = "TPAUTOMATE",
    executables = [Executable("TPTHPV3.py")]
)
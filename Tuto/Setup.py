from cx_Freeze import setup,Executable
setup(
    name = "MonProgramme",
    version = "0.1",
    description = "Affichage réussit",
    executables = [Executable("Exécutablecx_freeze.py")]
)
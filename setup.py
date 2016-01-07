import cx_Freeze

executables = [cx_Freeze.Executable("Race.py")]

cx_Freeze.setup(
    name="Road Runner",
    options={"build_exe": {"packages":["pygame"],
                           "include_files":["racecar.png"]}},

    executables = executables

    )

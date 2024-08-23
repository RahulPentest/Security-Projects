import venv
import subprocess
import os
import sys

def create_environment(venv_name: str, install_packages: list = None):
    try:
        venv.create(venv_name, with_pip=True)

        system_platform = sys.platform

        if system_platform == "win32":
            executable_path = os.path.join(venv_name, "Scripts", "python.exe")
        elif system_platform == "darwin":
            executable_path = os.path.join(venv_name, "bin", "python")
        else:
            return "Error: Operating system not recognized!"

        command_template = [executable_path, "-m", "pip", "install"]

        if install_packages:
            for package_name in install_packages:
                command = command_template[:]
                command.append(package_name)
                subprocess.run(command, check=True)
        
        return "Created the virtual Environment!"

    except Exception as error:
        return f"The error: {error} occurred."


# < ------------ NOTES ------------ >
# subprocess.run() takes a list as an argument
#   the first element in the list must be the command or executable to run
#   all the other elements are additional commands supporting the initial command/executable
#   check=True will raise an exception if the command fails

# new_list = original_list --> "new_list" will be a reference to the "original_list" and not a copy of the "original_list"
#   therefore, modifying "new_list" will modify the "original_list"

# the "is" operator in Python checks if two variables refer to the same object in memory, 
#   while "==" checks if the values of the two variables are equal

# mutable Default Arguments -> using mutable objects (like lists or dictionaries) as default arguments in functions can lead to unintended side effects, 
#   as changes to the mutable object persist across function calls
import subprocess
import pkg_resources
import sys


"""
This script checks and installs the necessary packages as listed in `requirements.txt`.

Running the Analysis
--------------------
After completing the setup, you can run the project scripts to perform the credit risk analysis.
"""


required = {pkg.split('==')[0] for pkg in open('requirements.txt').readlines()}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    print("Installing missing packages:", missing)
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)

print("All required packages are installed.")

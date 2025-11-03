#& Setting up Python Virtual Environment and Installing NumPy

#? Why do this?
#* A virtual environment (venv) is like a private workspace for Python.
#* It keeps your project’s packages separate from the system so nothing breaks.
#* NumPy is a library for working with numbers and arrays — it needs to be installed inside the venv.

#& Steps

#* Step 1: Check Python version
python --version
#? Shows the installed Python version (e.g., Python 3.11.5 or 3.12.11).

#* Step 2: Check which Python is being used
where python   # (Windows cmd)
#? Lists all Python executables on PATH. We saw:
#? - C:\msys64\mingw64\bin\python.exe  (MSYS2 build, problematic)
#? - C:\Python311\python.exe           (official build, correct one)
#? - WindowsApps\python.exe            (stub, ignore)

#* Step 3: Inspect Python inside interpreter
import sys
print(sys.version)
print(sys.executable)

#? sys.version shows compiler info:
#? - If it says [GCC ...] → MSYS2 build (bad for NumPy wheels).
#? - If it says [MSC ...] → Official python.org build (good).
#? sys.executable shows the exact path of the Python binary.

#* Step 4: Create a virtual environment with the official Python
C:\Python311\python -m venv venv

#* Step 5: Activate the virtual environment
#? On cmd:
venv\Scripts\activate
#? On PowerShell:
venv\Scripts\Activate.ps1
#? On bash (Git Bash/MSYS2):
source venv/Scripts/activate

#* Step 6: Upgrade pip and tools
python -m pip install --upgrade pip setuptools wheel

#* Step 7: Install NumPy
pip install numpy

#* Step 8: Verify installation
python -c "import numpy as np; print(np.__version__)"

#* Step 9: Test NumPy with a script
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))

#& Errors Encountered and Fixes

#? Error 1: "bash: venv\Scripts\activate: command not found"
#* Cause: Used Windows-style path in bash.
#* Fix: Used `source venv/Scripts/activate` in bash, or switched to cmd/PowerShell.

#? Error 2: "subprocess-exited-with-error" when installing NumPy
#* Cause: MSYS2 Python build tried to compile NumPy from source (needed cmake/ninja).
#* Fix: Switched to official Python.org build (MSC), which has prebuilt NumPy wheels.

#? Error 3: SSL certificate verification failed
#* Cause: MSYS2 Python’s SSL setup.
#* Fix: Avoided MSYS2 Python entirely, used official Python.org build.

#& Why this works
#* Official Python (MSC build) supports prebuilt NumPy wheels → no compiling errors.
#* Virtual environment isolates dependencies → safe and reversible.
#* Upgrading pip ensures smooth installs.
#* Diagnostic commands (`sys.version`, `sys.executable`, `where python`) help confirm you’re using the right interpreter.

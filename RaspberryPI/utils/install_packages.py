import subprocess
import subprocess
import sys

def install_and_import(packages):
    for package in packages:

        try:
            __import__(package)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        finally:
            globals()[package] = __import__(package)

install_and_import(['numpy', 'wikipedia'])

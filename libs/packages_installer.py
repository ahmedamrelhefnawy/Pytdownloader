import subprocess
import sys

def get_python_version():
    python_path = sys.executable
    if 'conda' in python_path:
        return 'conda'
    else:
        return 'pip'
    
class installer():
    
    version = get_python_version()
    
    
    @staticmethod
    def install_requirements():
        if installer.version == 'pip':
            installer.pip_installer()
        elif installer.version == 'conda':
            installer.conda_installer()

    @staticmethod
    def pip_installer():
        subprocess.run([r".\installers\installer_pip.bat"])
        
    @staticmethod
    def conda_installer():
        subprocess.run([r".\installers\installer_conda.bat"])

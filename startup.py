import os
import subprocess
import sys


def create_venv():
    # Check if the venv directory exists
    if not os.path.exists('venv'):
        # Create a virtual environment
        os.system('python3 -m venv venv')
        print("Virtual environment created.")
    else:
        print("Virtual environment already exists.")


def print_activation_instructions():
    # Print instructions to activate the virtual environment
    if sys.platform == 'win32':
        print("Run 'venv\\Scripts\\activate' to activate the virtual environment.")
    else:
        print("Run 'source venv/bin/activate' to activate the virtual environment.")


def install_numpy():
    # Install numpy in the virtual environment
    subprocess.call(
        f"{sys.executable} -m pip install -r requirements.txt", shell=True)


if __name__ == "__main__":
    create_venv()
    print_activation_instructions()
    # Uncomment the following line if you want to install numpy automatically after creating the venv
    install_numpy()

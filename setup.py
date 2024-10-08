import subprocess
import sys
import os

def create_conda_environment():
    print("Creating Conda environment...")
    subprocess.check_call(["conda", "env", "create", "-f", "environment.yml"])

def setup_project():
    print("Setting up the Email Classifier project...")
    if not os.path.exists(os.path.join(sys.prefix, 'conda-meta')):
        print("This script must be run in a Conda environment. Please activate the environment first.")
        sys.exit(1)
    
    create_conda_environment()
    print("Setup complete! Activate the environment with 'conda activate email_classifier'")

if __name__ == "__main__":
    setup_project()
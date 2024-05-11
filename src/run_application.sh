#!/bin/bash

# Check that Python3 is installed 
./python_setup.sh

# Check that Pip3 is installed
./pip_setup.sh

# Create a virtual environment
./venv_setup.sh

#Install required packages
./package_install.sh

#Run the application
echo 'Initiating Baker3000'
python3 main.py
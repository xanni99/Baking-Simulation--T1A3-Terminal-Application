#!/bin/bash
# Check that Pip3 is installed
if ! [[ -x "$(command -v pip3)" ]]
then
  echo 'ERROR: 
    This program requires Pip3 to be installed.
    To install Pip3, please visit https://pypi.org/project/pip/' >&2
  exit 1
fi

echo 'Pip3 is installed correctly.'
# !/bin/bash
# Check that Python3 is installed 
if ! [[ -x "$(command -v python3)" ]]
then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]
    then
        echo 'Python 3 is installed correctly.'
    else
        echo 'ERROR: 
        This program requires the updated version of Python3 to be installed.
        To update your version please visit https://www.python.org/downloads/' >&2
    fi 
     exit1  
else
    echo 'Python set up is complete'
fi
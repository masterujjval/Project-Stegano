#!/bin/bash

if which python3
then
    
    clear

else
    echo "python3 not found..Installing...."
    sudo apt install python3
    echo "clearing terminal"
    sleep 2
    clear
fi

echo -e  '\n'
echo "***********************CYBERSECURITY TOOLS*******************************"
echo "Which tool to use?"
echo "1) Image Encryption"
echo "2) Text Encryption"
 
read ans

case $ans in
    "1")
        python3 main.py
        ;;
    "2")
        bash binder
        ;;
    *)
        echo "Invalid Input"
        ;;
esac

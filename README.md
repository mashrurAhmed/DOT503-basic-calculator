# DOT503-basic-calculator

A simple calculator app. 
It asks for input in the format x + y. 
x and y are any number with an operator (+, -, *, /) between them. The spaces are mandatory.
You may use the result of your previous calculation by typing the letter 'r' instead of a number.
You can exit the program anytime by typing the letter 'N'.

Requirements to build this project: 
..* Python 3, prefarably latest.
..* pip package manager installed.

Install pybuilder using pip: `pip install pybuilder`.
If the installation gives a warning about the install directory not being in PATH, please add it to your environment's PATH variable.

To start the build, type in the command `pyb -v` on the project console.
The '-v' tag describes verbose results such that if the build fails, the reasons are clearly displayed.
A folder 'target' will be created, containing the distributable package compressed using gunzip, alongside build reports etc.
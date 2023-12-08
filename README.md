# Project Title: AirBnB Clone Console Project

## Command Interpreter
The command interpreter is a tool designed to facilitate interaction with the project.
It provides a command-line interface for managing and interacting with various classes and functionalities.

### How to start it:
To start the command interpreter, run the `console.py` script in your terminal.

### How to use it:
Once the interpreter is running, you can enter commands in the prompt. The supported commands include:

create: Create a new instance of a class.
show: Display information about a specific instance.
destroy: Delete a specified instance.
all: Display information about all instances or all instances of a specific class.
update: Update the attributes of a specific instance.
For detailed information about each command and their usage, you can use the help command within the interpreter.

### examples:
Interactive Mode

$ ./console.py
(hbnb) create BaseModel

(hbnb) show BaseModel 1234-1234-1234

(hbnb) destroy BaseModel 1234-1234-1234

(hbnb) all

(hbnb) update BaseModel 1234-1234-1234 attribute_name "new_value"

(hbnb) quit

Non-Interactive Mode

 echo "create BaseModel" | ./console.py

$ echo "show BaseModel 1234-1234-1234" | ./console.py

$ echo "destroy BaseModel 1234-1234-1234" | ./console.py

$ echo "all" | ./console.py

$ echo "update BaseModel 1234-1234-1234 attribute_name 'new_value'" | ./console.py

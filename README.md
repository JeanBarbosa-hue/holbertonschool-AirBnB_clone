# AirBnB Console

![](https://github.com/JeanBarbosa-hue/holbertonschool-AirBnB_clone/blob/master/image/airbnb-door.gif)

The AirBnB Console is a command-line interface (CLI) for managing objects in the AirBnB project. It allows users to create, view, update, and delete instances of various classes, such as User, Listing, and more.

## Getting Started

These instructions will guide you on how to set up and use the AirBnB Console on your local machine.

### Prerequisites

- Python 3.x
- Git

### Installation

1. Clone the repository to your local machine:

    $ git clone https://github.com/your-username/airbnb-console.git

2. Navigate to the project directory:

    $ cd airbnb-console


3. (Optional) Create and activate a virtual environment:

    $ python3 -m venv venv
    $ source venv/bin/activate


4. Install the required dependencies:

    $ pip install -r requirements.txt


### Execution

Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

### Usage

1. Run the console by executing the `console.py` script:

    $ python console.py

2. Once the console starts, you can enter various commands to interact with the objects:
    (hbnb) create User
    (hbnb) show User 12345
    (hbnb) all
    (hbnb) update User 12345 email test@example.com
    (hbnb) destroy User 12345
    (hbnb) quit

The available commands include `create`, `show`, `all`, `update`, `destroy`, and more. Use the `help` command for more information on each command.

3. The console automatically saves the objects to a JSON file (`file.json`) and loads them when starting the console.

## Project Structure

The project consists of the following files and directories:

- `console.py`: The main script for the AirBnB Console.
- `models/`: Directory containing the model classes.
- `models/base_model.py`: The BaseModel class, the base class for all other models.
- `models/user.py`: The User class, which inherits from BaseModel.
- `models/listing.py`: Example additional model class (you can create more).
- `models/__init__.py`: Initialization file for the models package.
- `models/storage.py`: The FileStorage class for managing object serialization and deserialization.
- `file.json`: The JSON file where the objects are stored.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.



# AirBnB Clone

## Description

This project is the first step toward building a complete clone of the AirBnB web application.

The project includes a command-line interpreter (console) that allows users to manage AirBnB objects. The command interpreter can be used to create, display, update, and delete objects.

## Command Interpreter

The command interpreter provides an interactive way to manage objects in the AirBnB application.

### How to Start It

Run the console from the project root:

    ./console.py

The prompt should look like:

    (hbnb)

### How to Use It

Once the console is running, type commands at the `(hbnb)` prompt.

For example:

    (hbnb) help
    (hbnb) quit

The console also supports non-interactive mode. For example:

    echo "help" | ./console.py

### Examples

Create a new BaseModel instance:

    (hbnb) create BaseModel

Display an instance:

    (hbnb) show BaseModel <id>

Display all instances:

    (hbnb) all

Display all instances of a specific class:

    (hbnb) all BaseModel

Update an instance:

    (hbnb) update BaseModel <id> name "My Object"

Delete an instance:

    (hbnb) destroy BaseModel <id>

Display command help:

    (hbnb) help

Exit the console:

    (hbnb) quit

You can also exit using EOF (Ctrl+D).

## Project Structure

    AirBnB_clone/
    ├── AUTHORS
    ├── README.md
    ├── console.py
    ├── models/
    └── tests/

## About This Repository

This repository is maintained by Mutsinzi Enock as part of the continued development of the AirBnB clone project.

GitHub: Mutsinzi-E
Email: mutsinzienock56@gmail.com

## Authors

See the AUTHORS file for the list of contributors.

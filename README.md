# AirBnB Clone - The Console

![AirBnB Logo](https://upload.wikimedia.org/wikipedia/commons/6/69/Airbnb_Logo_Bélo.svg)

## Diagrams

graph LR
    A[Instance] --> B[Dictionary]
    B --> C[JSON String]
    C --> D[File]
    D --> C
    C --> B
    B --> A

classDiagram
    BaseModel <|-- User
    BaseModel <|-- State
    BaseModel <|-- City
    BaseModel <|-- Place

## Overview

The aim with this project is to build a simple command interpreter to manage AirBnB objects. This command interpreter is the first step towards building a full web application.

## Table of Contents

- [Introduction](#introduction)
- [Concepts](#concepts)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Author](#Author)

## Introduction

This project includes the following components:
- A parent class (BaseModel) to handle initialization, serialization, and deserialization of future instances.
- A simple flow of serialization/deserialization: `Instance <-> Dictionary <-> JSON string <-> File`.
- All classes used for AirBnB (User, State, City, Place, etc.) that inherit from BaseModel.
- A storage engine to abstract the file storage.
- Unit tests to validate all classes and storage engines.

## Concepts

- **Python packages**: Understanding how to create and manage Python packages.
- **AirBnB clone**: Creating a command interpreter similar to a shell but for AirBnB objects.

## Features

- Command interpreter to manage AirBnB objects.
- Serialization and deserialization of instances to and from JSON.
- CRUD operations for the AirBnB objects.
- Unit testing.

## Requirements

- Python 3.8.5
- Ubuntu 20.04 LTS
- `pycodestyle` 2.8.*

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Katalyst99/AirBnB_clone.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AirBnB_clone
    ```
3. Ensure all files are executable:
    ```bash
    chmod 777 console.py
    ```

## Usage

To start the command interpreter, run:
```bash
./console.py

To start in non-interactive mode:
echo "help" | ./console.py

Also regarding tests:
echo "python3 -m unittest discover tests" | bash

## Project Structure

AirBnB_clone/
├── models/
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── place.py
│   ├── __init__.py
│   └── engine/
│       └── file_storage.py
├── tests/
│   ├── test_models/
│   │   ├── test_base_model.py
│   │   └── ...
│   └── __init__.py
├── console.py
├── README.md
└── file.json

## AUTHORS
* Katleho Lekale(https://github.com/Katalyst99) - @katleho_lekale(https://twitter.com/katleho_lekale)

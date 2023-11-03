# The Console

<h1 align="center">
    <img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="30" alt="AirBnB logo"> AirBnB clone
</h1> 

![hbnb](https://zupimages.net/up/23/44/hwzw.png)

<h2>
     Description
</h2>

<p>
This is the first part of a project that simulates an airbnb application.Here we apply object oriented programming, python data translation and command interpreted logic to deliver a local database that can be modified by commands.
The tools used in this project are :
 
 <br>
    <img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="15" alt="AirBnB logo"> python3 <br>
    <img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="15" alt="AirBnB logo"> json files where a database is  simulated and also serves to translate  data between languages <br>
    <img src="https://cdn.icon-icons.com/icons2/836/PNG/512/Airbnb_icon-icons.com_66791.png" height="15" alt="AirBnB logo"> PyCodeStyle

This marks the initial phase of the project, emulating an Airbnb-style application. We're establishing a mechanism to manage the components our web page will utilize by interacting with a JSON-formatted database. In this context, we implement object-oriented programming, Python data translation, and command interpretation logic to provide a locally modifiable database through commands.

![Console](https://zupimages.net/up/23/44/k6bj.png)
"Structure of the project"


## Installation

![hbnb](https://www.gifsanimados.org/data/media/56/computadora-y-ordenador-imagen-animada-0085.gif) 

Python3.4+ has to be installed if you desire to use the console:
```
sudo apt-get install python3
```
To have access to the console use the following command:
```
git clone https://github.com/Holbiwan/holbertonschool-AirBnB_clone
```

## Classes 

<p>

|            | BaseModel | User | State | City | Place | Review | Amenity | FileStorage |
| ---------- | --------- | ---- | ----- | ---- | ----- | ------ | ------- | ----------- |
| Defined In | models/base_model.py | models/user.py | models/state.py | models/city.py | models/place.py | models/review.py | models/amenity.py | models/engine/file_storage.py |
| Inherits From | N/A | BaseModel | BaseModel | BaseModel | BaseModel | BaseModel | BaseModel | N/A |
| Methods (Pub / Pri) | __str__(), save(), to_dict() Pub | Inh | Inh | Inh | Inh | Inh | Inh | all(), new(obj), save(), reload() Pub |

</p>

<p>

| **Command / Usage**                                     | **Descriptions**                                  |
| ------------------------------------------------------- | ------------------------------------------------- |
| quit                                                    | returns true, breaking cmdloop                    |
| EOF (Ctrl+D)                                            | prints goodbye msg to SO, then breaks loop        |
| create {{class name}}                                   | creates an instance of specified class            |
| show {{class name}} {{instance}}                        | prints str rep of class instance given class & id |
| destroy {{class name}} {{instance}}                     | destroy specified instance of class               |
| all {{class name}}                                      | prints str rep of all class instances in mem      |
| update {{class name}} {{instance}} {{attribute}} "{{value}}" | updates value of instance attribute in mem        |

</p>

## Using the Console
The console is a command line interpreter that permits management of the backend 
of HolbertonBnB. It can be used to handle and manipulate all classes utilized by 
the application (achieved by calls on the `storage` object defined above).

The HolbertonBnB console can be run both interactively and non-interactively. 
To run the console in non-interactive mode, pipe any command(s) into an execution 
of the file `console.py` at the command line.

Alternatively, to use the HolbertonBnB console in interactive mode, run the 
file `console.py` by itself:

## Run

* If you want to execute the console use:

```
python3 console.py
```
or
```
./console.py
```

## Storage

The above classes are handled by the abstracted storage engine defined in the
[FileStorage](./models/engine/file_storage.py) class.

Every time the backend is initialized, HolbertonBnB instantiates an instance of
`FileStorage` called `storage`. The `storage` object is loaded/re-loaded from
any class instances stored in the JSON file `file.json`. As class instances are
created, updated, or deleted, the `storage` object is used to register
corresponding changes in the `file.json`.

## Examples

Interactive mode:
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
(hbnb)
(hbnb) quit
$
```
Non-interactive mode:
```
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
```

## Testing

If you want to personalize the classes and execute unit tests to confirm that 
your changes haven't modify the functionality use:

```
python3 -m unittest discover tests
```

## **Authors** :writing_hand:

* **Jean-Luc BILO** - [Github](https://github.com/Luckisback)
* **Sabrina PAPEAU** - [Github](https://github.com/Holbiwan)

#!/usr/bin/python3
"""The program that contains the entry point of the command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Class that defines the console behavior"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF to exit the program"""
        return True

    def do_quit(self, arg):
        """'quit' command to exit the program"""
        return True

    def emptyline(self):
        """"Documented commands (type help <topic>):
            =======================================
            EOF    help    quit
        """
        pass

    def do_create(self, line):
        '''Creates a new instance of BaseModel'''

        if len(line) == 0:
            print('** class name missing **')

        elif line not in self.list_class:
            print("** class doesn't exist **")

        else:
            new_instance = eval(line)()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, line):
        '''
        Prints the string representation of an instance based on
        the class name and id
        '''

        line = line.split()
        obj_dict = storage.all()

        if not line:
            print('** class name missing **')
            return

        if line[0] not in self.list_class:
            print('** class doesn\'t exist **')
            return

        if len(line) < 2:
            print('** instance id missing **')
            return

        k = '{}.{}'.format(line[0], line[1])
        if k in obj_dict:
            print(obj_dict[k])
        else:
            print('** no instance found **')

    def do_destroy(self, line):
        '''Deletes an instance based on the class name and id'''

        line = line.split()
        obj_dict = storage.all()

        if not line:
            print('** class name missing **')
            return

        if line[0] not in self.list_class:
            print('** class doesn\'t exist **')
            return

        if len(line) < 2:
            print('** instance id missing **')
            return

        k = '{}.{}'.format(line[0], line[1])
        if k in obj_dict:
            del obj_dict[k]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        '''
        Prints all string representation of all instances based
        or not on the class name.
        '''

        line = line.split()
        obj_dict = storage.all()

        if len(line) == 0:
            print([str(obj) for obj in obj_dict.values()])
        elif line[0] not in self.list_class:
            print('** class doesn\'t exist **')
        else:
            print([str(obj) for obj in obj_dict.values()
                  if type(obj).__name__ == line[0]])

    def do_update(self, line):
        '''Updates an instance based on the class name and id
           by adding or updating attribute
        '''

        lines = line.split()
        obj_all = storage.all()

        # Vérification de la présence du nom de classe.
        if len(lines) == 0:
            print('** class name missing **')
            return

        class_name = lines[0]
        if class_name not in self.list_class:
            print('** class doesn\'t exist **')
            return

        if len(lines) == 1:
            print('** instance id missing **')
            return

        id = lines[1]
        key = '{}.{}'.format(class_name, id)
        if key not in obj_all:
            print('** no instance found **')
            return

        if len(lines) == 2:
            print('** attribute name missing **')
            return
        if len(lines) == 3:
            print('** value missing **')
            return

        name = lines[2]
        name_value = lines[3]
        setattr(obj_all[key], name, name_value)
        obj_all[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
"""Defines the HBnB console."""
import re
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def default(self, line: str):
        """Default behavior for cmd module when input is invalid"""

        if '.' not in  line:
            print("*** Unknown syntax: {}".format(line))
            return False

        args = line.split(".")
        class_name = args[0]
        func = args[1]
        match = re.search(r'"([^"]*)"', args[1])
        if match:
            id = match.group(1)
            line = f"{class_name} {id}"
        if (func == "all()"):
            self.do_all(class_name)
        elif (func == "count()"):
            self.do_count(class_name)
        elif "show" in func:
            self.do_show(line)
        elif "destroy" in func:
            self.do_destroy(line)

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, line):
        """Usage: create <class>
        Create a new class instance and print its id.
        """

        args = line.split()
        if args is None or len(args) == 0:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = globals()[args[0]]()
            storage.save()
            print(instance.id)

    def do_show(self, line):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """

        args = line.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, line):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""

        args = line.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instances = storage.all()
            if key in instances:
                del (instances[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        args = line.split()
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            lst_objects = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    lst_objects.append(obj.__str__())
                elif len(args) == 0:
                    lst_objects.append(obj.__str__())

            print(lst_objects)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>).
       Update a class instance of a given id by adding or updating
        a given attribute key/value pair"""

        args = line.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            instances = storage.all()
            attribute_name = args[2]
            attribute_value = args[3]
            if key in instances:
                instance = instances[key]
                try:
                    attribute_value = eval(attribute_value)
                    setattr(instance, attribute_name, attribute_value)
                    storage.save()
                except (SyntaxError, NameError):
                    print("** value missing **")
            else:
                print("** no instance found **")

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""

        args = line.split()
        if args is None or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for obj in storage.all().values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3

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

    def do_EOF(self, line):
        """EOF signal to exit the program."""
        print()
        return True

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def emptyline(self):
        pass

    def do_create(self, line):

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
                del(instances[key])
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, line):
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



if __name__ == '__main__':
    try:
        HBNBCommand().cmdloop()
    except KeyboardInterrupt:
        print()
        pass

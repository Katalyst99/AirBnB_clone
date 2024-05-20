#!/usr/bin/python3
"""This is the module for the command interpreter entry point"""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """The class for the console defined"""
    prompt = "(hbnb) "
    c_cls = ['BaseModel', 'User', 'State', 'City'
             'Amenity', 'Place', 'Review']

    def do_create(self, line):
        """Creates a new instance of BaseModel, nd prints the id."""
        if line == "":
            print('** class name missing **')
        elif line not in self.c_cls:
            print("** class doesn't exist **")
        else:
            c_name = eval(line)
            instance = c_name()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints string rep of instance based on name and id"""
        if not line:
            print('** class name missing **')
        else:
            strings = line.split()
            if len(strings) == 1:
                if strings[0] not in self.c_cls:
                    print("** class doesn't exist **")
                else:
                    print('** instance id missing **')
                return

            c_name, id_inst = strings[0], strings[1]
            if c_name not in self.c_cls:
                print("** class doesn't exist **")
                return

            key = "{}.{}".format(c_name, id_inst)
            inst = storage.all().get(key)
            if inst:
                print(inst)
            else:
                print('** no instance found **')

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print('** class name missing **')
            return
        strings = line.split()
        if len(strings) == 1:
            if strings[0] not in self.c_cls:
                print("** class doesn't exist **")
            else:
                print('** instance id missing **')
            return
        if strings[0] not in self.c_cls:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(strings[0], strings[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print('** no instance found **')

    def do_all(self, line):
        """Prints all string rep of all instances based or
        not on the class name"""
        obj_inst = []
        obj_all = storage.all()
        if line:
            if line not in self.c_cls:
                print("** class doesn't exist **")
                return
            for val in obj_all.values():
                if type(val).__name__ == line:
                    obj_inst.append(str(val))
        else:
            for val in obj_all.values():
                obj_inst.append(str(val))
        print(obj_inst)

    def do_update(self, line):
        """ Updates an instance based on the class name
        and id by adding or updating attribute"""
        strings = line.split()
        if len(strings) == 0:
            print('** class name missing **')
            return
        if len(strings) == 1:
            print('** instance id missing **')
            return
        if strings[0] not in self.c_cls:
            print("** class doesn't exist **")
            return
        key = f"{strings[0]}.{strings[1]}"
        if key not in storage.all():
            print('** no instance found **')
            return
        if len(strings) == 2:
            print('** attribute name missing **')
            return
        if len(strings) == 3:
            print("** value missing **")
            return
        inst = storage.all()[key]
        name_atr = strings[2]
        val_atr = strings[3].strip('"')

        if hasattr(inst, name_atr):
            type_atr = type(getattr(inst, name_atr))
            try:
                val_atr = type_atr(val_atr)
            except ValueError:
                pass
        else:
            try:
                val_atr = eval(val_atr)
            except (NameError, SyntaxError):
                pass
        setattr(inst, name_atr, val_atr)
        inst.save()

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """End of file command to exit the program"""
        return True

    def emptyline(self):
        """Should not execute anything when an empty line + ENTER"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

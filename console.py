#!/usr/bin/python3
""" This module contains the entry point of the command line interpreter """

import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This class contains command interpreter for program """
    class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
            }

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """This method exits the command interface when an EOF signal
        is passed"""
        print("")
        return True

    def emptyline(self):
        """This method does nothing when an emptyline is pased"""
        pass

    def do_create(self, arg):
        """This method creates a new instance"""
        if not arg:
            print("** class name missing **")
            return
        elif arg not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.class_dict[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """This method prints string representation of instance based on
        the class name and id"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            target_class, target_id = args[0], args[1]
            target_key = "{}.{}".format(target_class, target_id)
            all_obj = storage.all()

            if target_key not in all_obj:
                print("** no instance found **")
            else:
                target_instance_dict = all_obj[target_key]
                print(target_instance_dict)

    def do_destroy(self, arg):
        """This method deletes an instance based on the class name and id"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            target_class, target_id = args[0], args[1]
            target_key = "{}.{}".format(target_class, target_id)
            if target_key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[target_key]
                storage.save()

    def do_all(self, arg):
        """This method prints all string representation of all instances
        based or not on the same class name"""
        args = arg.split()
        instances_to_print = []

        if not arg:
            for instance in storage.all().values():
                instances_to_print.append(str(instance))
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        else:
            for key, instance in storage.all().items():
                if args[0] in key:
                    instances_to_print.append(str(instance))

        print(instances_to_print)

    def do_update(self, arg):
        """This method updates an instance based on class name and id
         by adding or updating attribute"""
        args = arg.split()

        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.class_dict:
            print("** class doesn't exist **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(args[0], args[1]) not in storage.all():
            print("** no instance found **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) == 3:
            print("** value missing **")
            return
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            attribute_value = args[3].strip('\"').strip('\'')
            attribute_type = type(eval(args[3]))
            setattr(storage.all()[instance_key], args[2],
                    attribute_type(attribute_value))
            storage.all()[instance_key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()

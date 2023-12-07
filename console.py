#!/usr/bin/python3
""" This module contains the entry point of the command line interpreter """
import cmd

class HBNBCommand(cmd.Cmd):
    """ This class contains command interpreter for program """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        # might need some reviewing
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

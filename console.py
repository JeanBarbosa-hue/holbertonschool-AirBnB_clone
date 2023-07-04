#!/usr/bin/python3

"""Module containing class called HBNBCommand"""

import cmd


class HBNBCommand(cmd.Cmd):
    """class called HBNBCommand with quit, EOF, Help, and emptyline methods."""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program method"""
        return True

    def do_EOF(self, arg):
        """Exit the program method"""
        return True

    def do_help(self, arg):
        """List available commands"""
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

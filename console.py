#!/usr/bin/python3
"""
    Console for the AirBnB project.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """Console class for the command interpreter."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""

        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()

            new_instance.save()

            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + '.' + instance_id
            instance = storage.all().get(key)
            if instance:
                print(instance)
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) < 2:
                if args[0] not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + '.' + instance_id
            instance = storage.all().get(key)
            if instance:
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except IndexError:
            if len(args) < 2:
                if args[0] not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
        else:
            args = arg.split()
            if args[0] not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            print([str(obj) for obj in objects.values()
                  if type(obj).__name__ == args[0]])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            instance_id = args[1]
            key = class_name + '.' + instance_id
            instance = storage.all().get(key)
            if not instance:
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            if len(args) < 4:
                print("** value missing **")
                return
            attr_name = args[2]
            attr_value = args[3]
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                setattr(instance, attr_name, attr_type(attr_value))
                instance.save()
            else:
                print("** attribute doesn't exist **")
        except IndexError:
            if len(args) < 2:
                if args[0] not in ["BaseModel"]:
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            else:
                print("** no instance found **")

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def help_quit(self):
        """Help information for quit command."""
        print("Quit command to exit the program.")
        print()

    def help_EOF(self):
        """Help information for EOF command."""
        print("EOF command to exit the program.")
        print()

    def help_create(self):
        """Help information for create command."""
        print("Create a new instance of BaseModel, save it, and print the id.")
        print()

    def help_show(self):
        """Help information for show command."""
        print("Print the string representation of an instance.")
        print()

    def help_destroy(self):
        """Help information for destroy command."""
        print("Delete an instance based on the class name and id.")
        print()

    def help_all(self):
        """Help information for all command."""
        print("Print all string representations of instances.")
        print()

    def help_update(self):
        """Help information for update command."""
        print("Update an instance based on the class name and id.")
        print()


if __name__ == '__main__':

    HBNBCommand().cmdloop()

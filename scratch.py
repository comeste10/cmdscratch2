import cmd
import turtle

class TurtleShell(cmd.Cmd):
    intro = 'Welcome to the Turtle Shell. Type help or ? to list commands.\n'
    prompt = 'turtle> '

    def __init__(self):
        super().__init__()
        self.turtle = turtle.Turtle()
        self.screen = turtle.Screen()

    def do_forward(self, arg):
        'Move the turtle forward by the specified distance.'
        try:
            distance = int(arg)
            self.turtle.forward(distance)
        except ValueError:
            print('Invalid distance.')

    def do_backward(self, arg):
        'Move the turtle backward by the specified distance.'
        try:
            distance = int(arg)
            self.turtle.backward(distance)
        except ValueError:
            print('Invalid distance.')

    def do_right(self, arg):
        'Turn the turtle right by the specified angle.'
        try:
            angle = int(arg)
            self.turtle.right(angle)
        except ValueError:
            print('Invalid angle.')

    def do_left(self, arg):
        'Turn the turtle left by the specified angle.'
        try:
            angle = int(arg)
            self.turtle.left(angle)
        except ValueError:
            print('Invalid angle.')

    def do_penup(self, arg):
        'Lift the turtle\'s pen up.'
        self.turtle.penup()

    def do_pendown(self, arg):
        'Put the turtle\'s pen down.'
        self.turtle.pendown()

    def do_color(self, arg):
        'Set the turtle\'s pen color.'
        self.turtle.color(arg)

    def do_exit(self, arg):
        'Exit the turtle shell.'
        print('Exiting...')
        return True

if __name__ == '__main__':
    TurtleShell().cmdloop()

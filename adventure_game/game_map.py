import turtle


class GameMap:
    def __init__(self):
        self.t = turtle.Turtle()
        self.t.color('green', 'red')
        self.pensize = 4
        self.t.pen(pencolor='purple', pensize=self.pensize, speed=9)

    def build_turtle_map(self):
        room_width = 50
        map_width = 4 * self.pensize + 3 * room_width

        self.t.penup()

        self.t.back(map_width // 2)
        self.t.right(90)
        self.t.back(map_width // 2)
        self.t.left(90)

        self.t.pendown()

        # map boundary
        for i in range(4):
            self.t.fd(map_width)
            self.t.right(90)

        self.t.fd(54)
        self.t.right(90)
        self.t.fd(56)
        self.t.penup()
        self.t.fd(54)
        self.t.pendown()
        self.t.fd(56)

        self.t.left(90)
        self.t.fd(56)
        self.t.left(90)

        self.t.penup()
        self.t.fd(56)
        self.t.pendown()
        self.t.fd(54)
        self.t.fd(56)

        self.t.right(90)
        self.t.fd(56)
        self.t.right(90)
        self.t.fd(56)
        self.t.right(90)

        self.t.penup()
        self.t.fd(56)
        self.t.pendown()
        self.t.fd(56)
        self.t.penup()

        self.t.fd(28)
        self.t.right(90)
        self.t.fd(28)

    def get_turtle(self):
        return self.t

    def call_mainloop(self):
        turtle.mainloop()


if __name__ == '__main__':
    game = GameMap()
    game.build_turtle_map()
    game.call_mainloop()

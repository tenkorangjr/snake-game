from turtle import Turtle

# DEFINING CONSTANTS
SQUARE_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create our snake body as segments and as elements in
        list segments"""
        for position in SQUARE_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for snake in self.segments:
            snake.goto(1000, 1000)
        self.__init__()

    def move(self):
        """Move the snake by the constant pixels"""
        for seg_index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_index - 1].xcor()  # new x coordinate of the segment right before it
            new_y = self.segments[seg_index - 1].ycor()  # new y coordinate of the segment right before it
            self.segments[seg_index].goto((new_x, new_y))  # move the segment to the position of the preceding segment

        self.head.forward(MOVING_DISTANCE)

    def up(self):
        """Move the snake up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """MOve the snake down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Move the snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """MOve the snake to the right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
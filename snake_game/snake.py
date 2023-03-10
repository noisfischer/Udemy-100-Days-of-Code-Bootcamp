from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake() # Calls on the following method below
        self.head = self.all_segments[0] # Defines which segment will be the head (the first index)

    def create_snake(self): # Creates 3 segmented snake
        for snakes in range(3):
            self.add_segment(snakes)

    x = 0
    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(self.x, 0)
        self.x = -400
        self.all_segments.append(new_segment)


    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.all_segments[-1].position) #get position of last segment

    def move(self):
        # Purpose: move tail-end segment up to 2nd-to-last segment position and so on
        # In range, the first input gives us index 3, 0 is index 1, and -1 is how many indexes
        # we will subtract by. So From index 3 down to index 1
        for segment_number in range(len(self.all_segments) - 1, 0, -1):  # start=2, stop=0, step=-1
            new_x = self.all_segments[segment_number - 1].xcor() # Getting the coordinates of the segment ahead of it
            new_y = self.all_segments[segment_number - 1].ycor()
            self.all_segments[segment_number].goto(new_x, new_y) # Moving to the coordinates of the segment ahead of it

        self.head.forward(MOVE_DISTANCE)
        # Now our snake will continuously move forward and the whole tail will follow the head (first segment)

    def up(self):
        if self.head.heading() != DOWN:  #Prevents you from turning around 180
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # basically reinitializes our snake if we get game over without exiting the game and restarting
    def reset(self):
        self.x = 0
        for seg in self.all_segments:
            seg.goto(1000, 1000)
        self.all_segments.clear()
        self.create_snake()
        self.head = self.all_segments[0]

from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.block_list = []
        self.location = 0
        self.direction = "right"
        self.create()
        self.head = self.block_list[0]

    def create(self):
        for i in range(3):
            block = Turtle('square')
            block.penup()
            block.color('white')
            block.setx(-MOVE_DISTANCE * i)
            self.block_list.append(block)

    def move(self, eat):
        # handle move
        if eat:
            copy_block = self.block_list[-1].clone()
            self.block_list.append(copy_block)
        last_block = self.block_list.pop()
        first_block = self.block_list[0]
        pos = first_block.pos()

        # judge direction
        if self.direction == 'up':
            last_block.goto(pos[0], pos[1] + MOVE_DISTANCE)

        if self.direction == 'left':
            last_block.goto(pos[0] - MOVE_DISTANCE, pos[1])

        if self.direction == 'right':
            last_block.goto(pos[0] + MOVE_DISTANCE, pos[1])

        if self.direction == 'down':
            last_block.goto(pos[0], pos[1] - MOVE_DISTANCE)

        self.block_list.insert(0, last_block)
        self.head = self.block_list[0]

    def change_direction(self, direction):
        if direction == 'up' and self.direction != 'down':
            self.direction = 'up'

        if direction == 'left' and self.direction != 'right':
            self.direction = 'left'

        if direction == 'right' and self.direction != 'left':
            self.direction = 'right'

        if direction == 'down' and self.direction != 'up':
            self.direction = 'down'

    def up(self):
        self.change_direction('up')

    def down(self):
        self.change_direction('down')

    def right(self):
        self.change_direction('right')

    def left(self):
        self.change_direction('left')
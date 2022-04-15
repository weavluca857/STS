import pygame

WHITE = (255, 255, 255)

class Player(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self, joystick, y_pos):
        # Call the parent's constructor
        super().__init__()

        self.width = 75
        self.height = 15
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(WHITE)
        self.joystick = joystick

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.screenheight = pygame.display.get_surface().get_height()
        self.screenwidth = pygame.display.get_surface().get_width()

        self.rect.x = 0
        self.rect.y = y_pos

    # Update the player
    def update(self):
        self.joystick.update()
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = self.joystick.up

        # Move x according to the axis. We multiply by 15 to speed up the movement.
        self.rect.x = int(self.rect.x + horiz_axis_pos * 15)

        # Make sure we don't push the player paddle off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
        if self.rect.x < 0:
            self.rect.x = 0

    def updateAI(self, ball_pos, paddle_pos):
        self.joystick.update(paddle_pos, ball_pos)
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = self.joystick.up

        # Move x according to the axis. We multiply by 15 to speed up the movement.
        self.rect.x = int(self.rect.x + horiz_axis_pos * 15)

        # Make sure we don't push the player paddle off the right side of the screen
        if self.rect.x > self.screenwidth - self.width:
            self.rect.x = self.screenwidth - self.width
        if self.rect.x < 0:
            self.rect.x = 0
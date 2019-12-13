import random

import pygame


pygame.init ()

# Name of colours with their values from 0 to 255
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (23, 210, 155)
Red = (255, 0, 0)
Gold = (255, 255, 0)

width, height = [ 500, 500 ]
Mid_Point = [ 250, 250 ]  # This is the mid-point of the screen
# Create an 500x500 sized screen
Window = pygame.display.set_mode ( (width, height) )
# The score at the beginning of the game
Score = 0

# Random food positions
FoodPosition = [ random.randint ( 6, 22 ) * 20, random.randint ( 6, 22 ) * 20 ]
# The snake segments height and width
SnakeSize = [ 10, 10 ]
# snake segments margin
Margin = 1

# Speed vector of the snake
change_x = SnakeSize[ 0 ] + Margin
change_y = 0
# initial number of segments that constitutes the snake. Snake size is 1 initially
Initial_Size = 1
Move_To_Direction = "Right"


# Eat_food = pygame.mixer.Sound ( 'WA0011.m4a' )
# pygame.mixer.music.load ( 'WA0011.m4a' )


class Snake_Segment ( pygame.sprite.Sprite ):
    """ Class of a snake segment. """

    def __init__(self, x, y):
        # Constructor function

        # Call parent's constructor
        super(Snake_Segment, self).__init__()

        # Set height, width
        self.image = pygame.Surface ( SnakeSize )
        self.image.fill ( Gold )

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect ()
        self.rect.x = x
        self.rect.y = y
        # Set speed vector of the snake
        self.change_x = SnakeSize[ 0 ] + Margin
        self.change_y = 0


# check if the snake touches the food
def Touch(x, y, FoodX, FoodY):
    if abs ( x - FoodX ) < (SnakeSize[ 0 ]) and ((SnakeSize[ 1 ]) > abs ( y - FoodY )):
        return 1
    return 0


List_locations = pygame.sprite.Group ()

# Create an initial snake
List_of_segments = [ ]  # List of snake segments
clock = pygame.time.Clock ()

for i in range ( Initial_Size ):
    x = Mid_Point[ 0 ] - (SnakeSize[ 0 ] + Margin) * i
    y = Mid_Point[ 1 ]
    segment = Snake_Segment ( x, y )

    # create small rectangle that's gonna be added to the tail of the snake after eating the food

    List_of_segments.append ( segment )  # append the segment by updating the list
    List_locations.add ( segment )  # add the segment to the list

# Main game loop
Finish = False
def gameOver():

    if x > 500 or x < 0 or y >500 or y <0:

        return True
    else:
        return False
       # pygame.quit ()


while not Finish:
    for event in pygame.event.get ():
        if event.type == pygame.QUIT or gameOver():
            Finish = True

        # direction based on the key pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and not Move_To_Direction == "Right":
                Move_To_Direction = "Left"
                change_x = (SnakeSize[ 0 ] + Margin) * -1
                change_y = 0
            elif event.key == pygame.K_RIGHT and not Move_To_Direction == "Left":
                Move_To_Direction = "Right"
                change_x = (SnakeSize[ 0 ] + Margin)
                change_y = 0
            elif event.key == pygame.K_UP and not Move_To_Direction == "Down":
                Move_To_Direction = "Up"
                change_x = 0
                change_y = (SnakeSize[ 1 ] + Margin) * -1
            elif event.key == pygame.K_DOWN and not Move_To_Direction == "Up":
                Move_To_Direction = "Down"
                change_x = 0
                change_y = (SnakeSize[ 1 ] + Margin)

    # updated position of the new segments
    x = List_of_segments[ 0 ].rect.x + change_x
    y = List_of_segments[ 0 ].rect.y + change_y

    # check if the head touches any part of the snake, quit the game
    for i in range ( len ( List_of_segments ) ):
        if Touch ( x, y, List_of_segments[ i ].rect.x, List_of_segments[ i ].rect.y ):
            # clear and fill the screen
            Window.fill ( Black )
            List_locations.draw ( Window )

            # Flip screen
            pygame.display.flip ()

            # update the score boards
            clock.tick ( 10 )
            font = pygame.font.Font ( 'freesansbold.ttf', 32 )
            Text = font.render ( "Well done: Your score is " + str ( Score ), True, Red )
            TextPosition = Text.get_rect ()
            TextPosition.center = Mid_Point
            Window.blit ( Text, TextPosition )
            pygame.display.update ()
            pygame.time.delay ( 1000 )
            Finish = True

    # remove the last item for the list
    Original_segment = List_of_segments.pop ()
    List_locations.remove ( Original_segment )

    segment = Snake_Segment ( x, y )

    # Insert new segment into the list
    List_of_segments.insert ( 0, segment )
    List_locations.add ( segment )

    #  Draw and clear the screen
    Window.fill ( Black )
    if Touch ( x, y, FoodPosition[ 0 ], FoodPosition[ 1 ] ):
        Score += 3
        segment = Snake_Segment ( x, y )
        List_of_segments.append ( segment )  # increase the size of the snake
        List_locations.add ( segment )
        segment = Snake_Segment ( x, y )

        List_of_segments.append ( segment )  # increase the size of the snake by appending to previous size
        List_locations.add ( segment )

        FoodPosition = [ random.randint ( 6, 22 ) * 20, random.randint ( 6, 22 ) * 20 ]
        # locate the new food, make sure the score board is not touched by the food. That is why I chose those numbers
    pygame.draw.rect ( Window, Green, (FoodPosition[ 0 ], FoodPosition[ 1 ], 10, 10) )
    # draw a new food

    # Title of the window
    pygame.display.set_caption ( 'The Snake Game: ' + str ( Score ) )
    List_locations.draw ( Window )

    # Flip the screen (Refresh the screen)
    pygame.display.flip ()

    # update the score board
    clock.tick ( 10 )


def Message(Text, color):
    font = pygame.font.Font ( 'freesansbold.ttf', 32 )
    Text = font.render ( "Score: " + str ( Score ), True, Red )
    TextPosition = Text.get_rect ()
    TextPosition.center = (100, 100)
    Window.blit ( Text, TextPosition )
    pygame.display.update ()
#to show the score we must call this function
Message("Score",Red)

# check if the snake touches the boundary
def Collision():

    if x > 500 or x < 0 or y >500 or y <0:
        TextPosition = Text.get_rect ()
        Window.blit ( Text, TextPosition )
        pygame.display.update ()
        pygame.time.delay ( 1000 )

        pygame.quit ()


def Quit_Game():
    pygame.display.update ()
    pygame.quit ()

Quit_Game()
quit ()

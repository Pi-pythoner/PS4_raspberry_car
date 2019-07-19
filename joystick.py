import pygame

global joy_left1,joy_axi1
joy_left1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
joy_axi1 = []


def ps4_detect():
    global joy_left1,joy_axi1
    joy_axi1 = [0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000]
    joy_left1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pygame.init()
   
    done = False
    clock = pygame.time.Clock()
    pygame.joystick.init()
    while done == False:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop     
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")
        #joystick_count = pygame.joystick.get_count()
        if 1:
            joystick = pygame.joystick.Joystick(0)
            joystick.init()

            axes = joystick.get_numaxes()

            for i in range(axes):
                axis = joystick.get_axis(i)
                joy_axi1[i]=round(axis,3)             # get the axis data list,keep rounding 3,by Vince

            buttons = joystick.get_numbuttons()

            for i in range(buttons):
                button = joystick.get_button(i)
                joy_left1[i] = button        # get the button status data list,by Vince
    
            # Hat switch. All or nothing for direction, not like joysticks.
            # Value comes back in an array.
            hats = joystick.get_numhats()


            for i in range(hats):
                hat = joystick.get_hat(i)

        #pygame.display.flip()
        

        clock.tick(20)

    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()


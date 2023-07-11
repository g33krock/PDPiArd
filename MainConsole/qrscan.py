import cv2
import serial
import numpy as np
import time
import ast
import random
from tkinter import Tk

# Get screen size
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
player1 = serial.Serial('/dev/ttyUSB0', 9600)
player2 = serial.Serial('/dev/ttyACM1', 9600)

time.sleep(2)

def get_all_player_ready_status(player1_ready, player2_ready):
    players_ready = [player1_ready, player2_ready]
    
    return players_ready

def get_random_monster_action(highestAggroPlayer):
    monster = [
        {'strike':[{'target':target}, {'damage':2}]}, 
        {'swipe':[{'target':[1,9,3]}, {'damage':1}]}, 
        {'heal':[{'target':2}, {'amount':2}]}
    ]
    
    return random.choice(monster)  # Return a random action dictionary

target = 0
damage = 0
healing = 0
poison = 0
bleed = 0
fire = 0
frost = 0
shield = 0

monster_action = get_random_monster_action(target)

player1_ready = False
player2_ready = False

try:
    while True:
        dataString = ser.readline()
        dataDecoded = dataString.decode('utf-8')
        if dataDecoded.startswith('[') and dataDecoded.endswith(']'):
            
            player1.write(dataDecoded.encode('utf-8'))
            player2.write(dataDecoded.encode('utf-8'))
            time.sleep(1)
            

            if player1.in_waiting > 0:
                print(player1.in_waiting)
                line = player1.readline().decode('utf-8', 'ignore').strip()  # ignore invalid characters

                variables = line.split(',')
                # Convert each string in the list to the correct type
                variables[0] = str(variables[0])
                variables[1] = int(variables[1])

                cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                background = cv2.imread('/home/g33krock/Pictures/warrior')
                background = cv2.resize(background, (screen_width, screen_height))
        
                image = np.zeros((600, 800, 3), dtype="uint8")
                font = cv2.FONT_HERSHEY_SIMPLEX
                origin = (50, 300)
                font_scale = 1
                font_color = (0, 0, 0)
                line_type = 2
                
                # List of variable names for display
                variable_names = ['class', 'health', 'baseaggro', 'aggromodifier', 'aggro']
                
                player1_ready = True

                # Starting y-coordinate for the text
                y = 50

                # Loop over the variables and their corresponding names
                for name, value in zip(variable_names, variables):
                    # The text to display for this variable
                    text = f'{name}: {value}'

                    # Add the text to the image
                    cv2.putText(background, text, (50, y), font, font_scale, font_color, line_type)

                    # Increment the y-coordinate for the next line
                    y += 30  # Change this value if you want more or less space between lines

                cv2.imshow("Image", background)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
            if player2.in_waiting > 0:
                line = player2.readline().decode('utf-8', 'ignore').strip()  # ignore invalid characters

                variables = line.split(',')
                # Convert each string in the list to the correct type
                variables[0] = str(variables[0])
                variables[1] = int(variables[1])

                cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                background = cv2.imread('/home/g33krock/Pictures/rogue')
                background = cv2.resize(background, (screen_width, screen_height))
        
                image = np.zeros((600, 800, 3), dtype="uint8")
                font = cv2.FONT_HERSHEY_SIMPLEX
                origin = (50, 300)
                font_scale = 1
                font_color = (0, 0, 0)
                line_type = 2
                
                # List of variable names for display
                variable_names = ['class', 'health', 'baseaggro', 'aggromodifier', 'aggro']
                
                player2_ready = True

                # Starting y-coordinate for the text
                y = 50

                # Loop over the variables and their corresponding names
                for name, value in zip(variable_names, variables):
                    # The text to display for this variable
                    text = f'{name}: {value}'

                    # Add the text to the image
                    cv2.putText(background, text, (50, y), font, font_scale, font_color, line_type)

                    # Increment the y-coordinate for the next line
                    y += 30  # Change this value if you want more or less space between lines

                cv2.imshow("Image", background)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                
            if get_all_player_ready_status(player1_ready, player2_ready) == [True, True]:
                background = cv2.imread('/home/g33krock/Pictures/dragon')
            
                cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
                image = np.zeros((600, 800, 3), dtype="uint8")
                font = cv2.FONT_HERSHEY_SIMPLEX
                origin = (50, 300)
                font_scale = 1
                font_color = (0, 0, 0)
                line_type = 2
                monster_action_string = str(monster_action)
            
                cv2.putText(background, monster_action_string, origin, font, font_scale, font_color, line_type)
            
                cv2.imshow("Image", background)
                

except KeyboardInterrupt:
    cv2.destroyAllWindows()
    print("Program interrupted by user, closing ports.")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    player1.close()
    player2.close()
    ser.close()




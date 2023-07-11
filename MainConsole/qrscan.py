import cv2
import serial
import numpy as np
import time
import ast
from tkinter import Tk

# Get screen size
root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
player1 = serial.Serial('/dev/ttyUSB0', 9600)
player2 = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)

try:
    while True:
        dataString = ser.readline()
        dataDecoded = dataString.decode('utf-8')
        if dataDecoded.startswith('[') and dataDecoded.endswith(']'):
            cv2.destroyAllWindows()
            background = cv2.imread('/home/g33krock/Pictures/dragon')
        
            image = np.zeros((600, 800, 3), dtype="uint8")
            font = cv2.FONT_HERSHEY_SIMPLEX
            origin = (50, 300)
            font_scale = 1
            font_color = (0, 0, 0)
            line_type = 2
            
            cv2.putText(background, dataDecoded, origin, font, font_scale, font_color, line_type)
            
            cv2.imshow("Image", background)
            
            player1.write(dataDecoded.encode('utf-8'))
            player2.write(dataDecoded.encode('utf-8'))
            time.sleep(1)
            
            cv2.waitKey(0)
            
            cv2.destroyAllWindows()
            

            if player1.in_waiting > 0:
                cv2.destroyAllWindows()
                line = player1.readline().decode('utf-8', 'ignore').strip()  # ignore invalid characters

                variables = line.split(',')
                # Convert each string in the list to the correct type
                variables[0] = str(variables[0])
                variables[1] = int(variables[1])

                
                background = cv2.imread('/home/g33krock/Pictures/warrior')
                background = cv2.resize(background, (screen_width, screen_height))
                cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
                image = np.zeros((600, 800, 3), dtype="uint8")
                font = cv2.FONT_HERSHEY_SIMPLEX
                origin = (50, 300)
                font_scale = 1
                font_color = (0, 0, 0)
                line_type = 2
                
                # List of variable names for display
                variable_names = ['class', 'health', 'baseaggro', 'aggromodifier', 'aggro']

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
                cv2.destroyAllWindows()
                line = player2.readline().decode('utf-8', 'ignore').strip()  # ignore invalid characters

                variables = line.split(',')
                # Convert each string in the list to the correct type
                variables[0] = str(variables[0])
                variables[1] = int(variables[1])

                
                background = cv2.imread('/home/g33krock/Pictures/rogue')
                background = cv2.resize(background, (screen_width, screen_height))
                cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        
                image = np.zeros((600, 800, 3), dtype="uint8")
                font = cv2.FONT_HERSHEY_SIMPLEX
                origin = (50, 300)
                font_scale = 1
                font_color = (0, 0, 0)
                line_type = 2
                
                # List of variable names for display
                variable_names = ['class', 'health', 'baseaggro', 'aggromodifier', 'aggro']

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

except KeyboardInterrupt:
    print("Program interrupted by user, closing ports.")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    player1.close()
    player2.close()
    ser.close()




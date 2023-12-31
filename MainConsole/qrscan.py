import cv2
import serial
import numpy as np
import time
import random
from tkinter import Tk
from threading import Thread

root = Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
player1 = serial.Serial('/dev/ttyUSB1', 9600)
player2 = serial.Serial('/dev/ttyACM0', 9600)

time.sleep(2)

def get_all_player_ready_status(player1_ready, player2_ready):
    players_ready = [player1_ready[0], player2_ready[0]]
    return players_ready

def get_random_monster_action(target):
    monster = [
        {'strike':[{'target':target}, {'damage':2}]}, 
        {'swipe':[{'target':[1,9,3]}, {'damage':1}]}, 
        {'heal':[{'target':2}, {'amount':2}]}
    ]
    
    return random.choice(monster)

target = 0
damage = 0
healing = 0
poison = 0
bleed = 0
fire = 0
frost = 0
shield = 0
health = 20

p1Step = 1
p1Aggro = 0
p1AdjustedAggro = 0
p1Damage = 0
p1Healing = 0
p1Poison = 0
p1Bleed = 0
p1Fire = 0
p1Frost = 0
p1Shield = 0
p1DamageTarget = 0
p1HealingTarget = 0
p1ShieldTarget = 0
p1DamageMod = 0
p1HealingMod = 0
p1ShieldMod = 0
p1ModTarget = 0
p1Special = 0

p2Step = 1
p2Aggro = 0
p2AdjustedAggro = 0
p2Damage = 0
p2Healing = 0
p2Poison = 0
p2Bleed = 0
p2Fire = 0
p2Frost = 0
p2Shield = 0
p2DamageTarget = 0
p2HealingTarget = 0
p2ShieldTarget = 0
p2DamageMod = 0
p2HealingMod = 0
p2ShieldMod = 0
p2ModTarget = 0
p2Special = 0

p3Step = 1
p3Aggro = 0
p3AdjustedAggro = 0
p3Damage = 0
p3Healing = 0
p3Poison = 0
p3Bleed = 0
p3Fire = 0
p3Frost = 0
p3Shield = 0
p3DamageTarget = 0
p3HealingTarget = 0
p3ShieldTarget = 0
p3DamageMod = 0
p3HealingMod = 0
p3ShieldMod = 0
p3ModTarget = 0
p3Special = 0

player1_secondary = [p1Step, 1, p1Aggro, p1AdjustedAggro, p1Damage, p1Healing, p1Poison, p1Bleed, p1Fire, p1Frost, p1Shield, p1DamageTarget, p1HealingTarget, p1ShieldTarget, p1DamageMod, p1HealingMod, p1ShieldMod, p1ModTarget, p1Special]
player2_secondary = [p2Step, 2, p2Aggro, p2AdjustedAggro, p2Damage, p2Healing, p2Poison, p2Bleed, p2Fire, p2Frost, p2Shield, p2DamageTarget, p2HealingTarget, p2ShieldTarget, p2DamageMod, p2HealingMod, p2ShieldMod, p2ModTarget, p2Special]
player3_secondary = [p3Step, 3, p3Aggro, p3AdjustedAggro, p3Damage, p3Healing, p3Poison, p3Bleed, p3Fire, p3Frost, p3Shield, p3DamageTarget, p3HealingTarget, p3ShieldTarget, p3DamageMod, p3HealingMod, p3ShieldMod, p3ModTarget, p3Special]


player1_ready = [False]
player2_ready = [False]

player1_aggro = [0]
player2_aggro = [0]

all_player_secondaries = [player1_secondary, player2_secondary, player3_secondary]

def handle_player(player, player_aggro, player_ready):
    try:
        while True:
            if player.is_open and player.in_waiting > 0:
                data = player.readline()
                line = data.decode('utf-8', 'ignore').strip()

                variables = line.split(',')
                variables = [int(variable) for variable in variables]
                player_aggro[0] = variables[3]
                player_ready[0] = True
                
                
                for i in range(len(variables)):
                    all_player_secondaries[variables[1] - 1][i] = variables[i]
                
                print(all_player_secondaries)
                
            else:
                time.sleep(0.01)
    except Exception as e:
        print(f"Error in handle_player: {str(e)}")


thread1 = Thread(target=handle_player, args=(player1, player1_aggro, player1_ready))
thread2 = Thread(target=handle_player, args=(player2, player2_aggro, player2_ready))


thread1.setDaemon(True)
thread2.setDaemon(True)

thread1.start()
thread2.start()

try:
    while True:
        dataString = ser.readline()
        dataDecoded = dataString.decode('utf-8')
        if dataDecoded.startswith('[') and dataDecoded.endswith(']'):
            
            player1.write(dataDecoded.encode('utf-8'))
            player2.write(dataDecoded.encode('utf-8'))
            time.sleep(1)
            
        if player1_ready[0] and player2_ready[0]:
            if player1_aggro[0] > player2_aggro[0]:
                target = 1
            elif player1_aggro[0] < player2_aggro[0]:
                target = 2
            else:
                target = 1
            print("P1 aggro:" + str(player1_aggro[0]))
            print("P2 aggro:" + str(player2_aggro[0]))
            print("Target:" + str(target))
            print("calling background file...")
            background = cv2.imread('/home/g33krock/Pictures/dragon')

            cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

            image = np.zeros((600, 800, 3), dtype="uint8")
            font = cv2.FONT_HERSHEY_SIMPLEX
            origin = (50, 300)
            font_scale = 1
            font_color = (0, 0, 0)
            line_type = 2
            
            monster_action = get_random_monster_action(target)
            monster_action_string = str(monster_action)
            print(str(monster_action))

            cv2.putText(background, monster_action_string, origin, font, font_scale, font_color, line_type)
            
            print("About to display image...")
            cv2.imshow("Image", background)
            cv2.waitKey(10000)
            cv2.destroyAllWindows()

            player1_ready[0] = False
            player2_ready[0] = False
            player1.reset_input_buffer()
            player2.reset_input_buffer()

except KeyboardInterrupt:
    print("Program interrupted by user, closing ports.")

except Exception as e:
    print(f"Error: {str(e)}")

finally:
    thread1.join()
    thread2.join()

    player1.close()
    player2.close()
    ser.close()
    cv2.destroyAllWindows()




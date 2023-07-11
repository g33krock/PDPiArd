
#include <Adafruit_SSD1306.h>
#include <Adafruit_GFX.h>
#include <Wire.h>
#include <Servo.h>
#include "images.h"

Servo servo1;  

Servo servo2;  

const int OLED_WIDTH = 128;
const int OLED_HEIGHT = 64;

Adafruit_SSD1306 display(OLED_WIDTH, OLED_HEIGHT, &Wire, -1);

#define BUTTON_ONE 2
#define BUTTON_TWO 4
#define BUTTON_THREE 7
#define BUTTON_FOUR 8
#define BUTTON_FIVE 12

const int GREEN_LED = 6;
const int RED_LED = 5;
const int YELLOW_LED = 3;
const int BLUE_LED = 9;

byte lastButtonState1 = LOW;
byte lastButtonState2 = LOW;
byte lastButtonState3 = LOW;
byte lastButtonState4 = LOW;
byte lastButtonState5 = LOW;

unsigned long debounceDuration = 50; // millis
unsigned long lastTimeButtonStateChanged = 0;

int pos = 20;    // variable to store the servo position
int prevPos = pos;
int tens;
int ones;

int numbers[11] = {0};

bool thisPlayer = false;
int aggro = 0;
float aggroMultiplier = 1;
int damage = 0;
int healing = 0;
int poison = 0;
int bleed = 0;
int fire = 0;
int frost = 0;
int shield = 0;

int prevPlayerAggro = 0;
int modifiedPlayerAggro = 1;

String playerClass = "warrior";
int playerHealth = 20;
int playerAggro = 0;

void setup() {
  Serial.begin(9600);

  randomSeed(analogRead(0));

  servo1.attach(14);
  servo2.attach(15);
  servo2.write(((215/10)*tens));
  servo1.write(((215/10)*ones));
  pinMode(BUTTON_ONE, INPUT);
  pinMode(BUTTON_TWO, INPUT);
  pinMode(BUTTON_THREE, INPUT);
  pinMode(BUTTON_FOUR, INPUT);
  pinMode(BUTTON_FIVE, INPUT);
  pinMode( GREEN_LED, OUTPUT );
  pinMode( RED_LED, OUTPUT );
  pinMode( YELLOW_LED, OUTPUT );
  pinMode( BLUE_LED, OUTPUT );

  // Initialize OLED display
  display.begin(SSD1306_SWITCHCAPVCC, 0x3C);
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(WHITE);
  display.setCursor(0, 0);

  display.clearDisplay();
  display.drawBitmap(0, 0, dungeongate, 128, 64, WHITE);

  display.setCursor(50, 40);
  display.print("Paper");
  display.setCursor(43, 50);
  display.print("Dungeon");
  display.display();
  resetValues();
}
void loop() {
  static int valueIndex = 0;

  if (Serial.available() > 0) {
    String incomingData = Serial.readString();

    int i = 0;
    for (int index = 0; index < incomingData.length(); index++) {
      char c = incomingData[index];
      if (c >= '0' && c <= '9') {
        numbers[i] = c - '0';
        i++;
        }
      }

      if (numbers[0] == 1) {
        updateValuesAndDisplay();
        valueIndex = 0;
        sendVariables();
    }
  }

    
  
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState1 = digitalRead(BUTTON_ONE);
    if (buttonState1 != lastButtonState1) {
      lastTimeButtonStateChanged = millis();
      lastButtonState1 = buttonState1;
      if (buttonState1 == LOW) {
        // do an action, for example print on Serial
        pos = pos + 1;
        tens = pos / 10;
        ones = pos % 10;
        servo2.write(((215/10)*tens));
        servo1.write(((215/10)*ones));
        delay(100);
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        analogWrite( GREEN_LED, 0 );
        analogWrite( RED_LED, 0 );
        analogWrite( YELLOW_LED, 0 );
        analogWrite( BLUE_LED, 0 );
        display.clearDisplay();
        display.setCursor(30, 28);
        display.print(pos);
        display.display();
      }
    }
  }
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState2 = digitalRead(BUTTON_TWO);
    if (buttonState2 != lastButtonState2) {
      lastTimeButtonStateChanged = millis();
      lastButtonState2 = buttonState2;
      if (buttonState2 == LOW) {
        // do an action, for example print on Serial
        pos = pos + 10;
        tens = pos / 10;
        ones = pos % 10;
        servo2.write(((215/10)*tens));
        servo1.write(((215/10)*ones));
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        analogWrite( GREEN_LED, 20 );
        analogWrite( RED_LED, 20 );
        analogWrite( YELLOW_LED, 20 );
        analogWrite( BLUE_LED, 20 );
        display.clearDisplay();
        display.setCursor(30, 28);
        display.print(pos);
        display.display();
      }
    }
  }
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState3 = digitalRead(BUTTON_THREE);
    if (buttonState3 != lastButtonState3) {
      lastTimeButtonStateChanged = millis();
      lastButtonState3 = buttonState3;
      if (buttonState3 == LOW) {
        // do an action, for example print on Serial
        pos = pos - 1;
        tens = pos / 10;
        ones = pos % 10;
        servo2.write(((215/10)*tens));
        servo1.write(((215/10)*ones));
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        analogWrite( GREEN_LED, 110 );
        analogWrite( RED_LED, 110 );
        analogWrite( YELLOW_LED, 110 );
        analogWrite( BLUE_LED, 110 );
        display.clearDisplay();
        display.setCursor(30, 28);
        display.print(pos);
        display.display();
      }
    }
  }
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState4 = digitalRead(BUTTON_FOUR);
    if (buttonState4 != lastButtonState4) {
      lastTimeButtonStateChanged = millis();
      lastButtonState4 = buttonState4;
      if (buttonState4 == LOW) {
        // do an action, for example print on Serial
        pos = pos - 10;
        tens = pos / 10;
        ones = pos % 10;
        servo2.write(((215/10)*tens));
        servo1.write(((215/10)*ones));
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        analogWrite( GREEN_LED, 255 );
        analogWrite( RED_LED, 255 );
        analogWrite( YELLOW_LED, 255 );
        analogWrite( BLUE_LED, 255 );
        display.clearDisplay();
        display.setCursor(30, 28);
        display.print(pos);
        display.display();
      }
    }
  }
  if (millis() - lastTimeButtonStateChanged > debounceDuration) {
    byte buttonState5 = digitalRead(BUTTON_FIVE);
    if (buttonState5 != lastButtonState5) {
      lastTimeButtonStateChanged = millis();
      lastButtonState5 = buttonState5;
      if (buttonState5 == LOW) {
        // do an action, for example print on Serial
        pos = 0;
        tens = pos / 10;
        ones = pos % 10;
        servo2.write(((215/10)*tens));
        servo1.write(((215/10)*ones));
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(WHITE);
        display.setCursor(0, 0);
        analogWrite( GREEN_LED, 255 );
        analogWrite( RED_LED, 255 );
        analogWrite( YELLOW_LED, 255 );
        analogWrite( BLUE_LED, 255 );
        display.clearDisplay();
        display.setCursor(30, 28);
        display.print(pos);
        display.display();
      }
    }
  }
}
void resetValues() {
  for (int i = 0; i < 11; i++) {
    numbers[i] = 0;
  }
}

void updateValuesAndDisplay() {
  bool thisPlayer = numbers[0];
  int aggro = numbers[1];
  float aggroMultiplier = numbers[2] * 0.1;  // Assuming you want to divide by 10
  int damage = numbers[3];
  int healing = numbers[4];
  int poison = numbers[5];
  int bleed = numbers[6];
  int fire = numbers[7];
  int frost = numbers[8];
  int shield = numbers[9]; 

  pos = prevPos - (damage - shield) + healing;
  tens = pos / 10;
  ones = pos % 10;

  modifiedPlayerAggro = (prevPlayerAggro + aggro) * (100/100);
  playerAggro = modifiedPlayerAggro;

  display.clearDisplay();
  display.setCursor(30, 0);
  display.print("Action Report");
  
  display.setCursor(0, 17);
  display.print("Aggro: ");
  display.println(aggro);

  display.setCursor(65, 17);
  display.print("x : ");
  display.println(aggroMultiplier);

  display.setCursor(0, 27);
  display.print("Damage: ");
  display.println(damage);

  display.setCursor(65, 27);
  display.print("Healing: ");
  display.println(healing);

  display.setCursor(0, 37);
  display.print("Poison: ");
  display.println(poison);

  display.setCursor(65, 37);
  display.print("Bleed: ");
  display.println(bleed);

  display.setCursor(0, 47);
  display.print("Fire: ");
  display.println(fire);

  display.setCursor(65, 47);
  display.print("Frost: ");
  display.println(frost);

  display.setCursor(35, 57);
  display.print("Shield: ");
  display.println(shield);

  display.display();

  delay(500);

  servo2.write(((215/10)*tens));
  servo1.write(((215/10)*ones));

  analogWrite( GREEN_LED, (poison * 25) );
  analogWrite( RED_LED, (bleed * 25) );
  analogWrite( YELLOW_LED, (fire * 25) );
  analogWrite( BLUE_LED, (frost * 25) );

  delay(500);
  
  prevPos = pos;

  resetValues();
}

void sendVariables() {
  playerHealth = pos;
  int randomNumber = random(1, 21); 
  String variables = String(playerClass) + "," + 
                     String(playerHealth) + "," + 
                     String(playerAggro) + "," + 
                     String(randomNumber) + "," + 
                     String(playerAggro + randomNumber);
  Serial.println(variables);
  prevPlayerAggro = playerAggro;
}

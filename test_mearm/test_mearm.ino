#include <Servo.h> //include the servo library

int pos1=90; //declare initial position of the servo 1
int pos2=90; //declare initial position of the servo 2
int pos3=90; //declare initial position of the servo 3
int pos4=90; //declare initial position of the servo 4
int servoPin1 = 9; //declare pin for servo number 1
int servoPin2 = 10; //declare pin for servo number 2
int servoPin3 = 11; //declare pin for servo number 3
int servoPin4 = 12; //declare pin for servo number 4
int servoDelay =15; //delay to allow the servo to reach position;

Servo myservo1; // create a servo object for servo number 1
Servo myservo2; // create a servo object for servo number 2
Servo myservo3; // create a servo object for servo number 3
Servo myservo4; // create a servo object for servo number 4

void setup() {
  Serial.begin(9600); //start serial port
  myservo1.attach(servoPin1); //declare where is the servo number 1
  myservo2.attach(servoPin2); //declare where is the servo number 2
  myservo3.attach(servoPin3); //declare where is the servo number 3
  myservo4.attach(servoPin4); //declare where is the servo number 3
}

void loop() {
  Serial.println("Set the angle for LH servo");  //prompt the user for the left hand servo position
  while(Serial.available()==0){}; //wait until information is received
  pos1 = Serial.parseInt();  //read the position for left hand servo - servo 1
  myservo1.write(pos1);  //write position in left hand servo - servo 1
  Serial.println("Set the angle for RH servo"); //prompt the user for the right hand servo position
  while(Serial.available()==0){};  //wait until information is received
  pos2 = Serial.parseInt();  //read the position for right hand servo - servo 2
  myservo2.write(pos2); //write position in right hand servo - servo 2
  Serial.println("Set the angle for claw servo"); //prompt the user for the top servo
  while(Serial.available()==0){}; //wait until information is received
  pos3 = Serial.parseInt();  //read the position for top (claw) servo - servo 3
  myservo3.write(pos3);  //write position in the top (claw) servo - servo 3
  Serial.println("Set the angle for base servo"); //prompt the user for the base servo position
  while(Serial.available()==0){}; //wait until information is received
  pos4 = Serial.parseInt();  //read the position for the base servo - servo 4
  myservo4.write(pos4); //write position in the base servo - servo 4
  delay(servoDelay) //delay for the servo to reach the position
}

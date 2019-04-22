#include <Servo.h>
Servo myservo; 
String command;
int pos;

void setup() {
 
  myservo.attach(9);
  Serial.begin(9600);
}

void loop()
{    
  if(Serial.available())
    { 
    command = Serial.readStringUntil('\n');
    pos = command.toInt();
    myservo.write(pos);
    Serial.println(command);
    }
}

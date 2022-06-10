// This #include statement was automatically added by the Particle IDE.
#include <ThingSpeak.h>


int analogvalue = 0;
const int led = D7;
int temp_f;
TCPClient client;

char output;

unsigned long myChannelNumber = 1731744;
const char * myWriteAPIKey = "VBNKHANQAXYB3K0L";

void setup(){

  ThingSpeak.begin(client);
  
  Particle.variable("analogvalue", analogvalue);
  Particle.variable("temp_f", temp_f);
 
Serial.begin(9600);

  pinMode(A0, INPUT);
}

void loop()
{
  delay(1500);
  // Read the analog value of the sensor (TMP36)
  analogvalue = analogRead(A0);
  //Convert the reading into degree 
  temp_f = (analogvalue); //To be accurate
  //temp = 69;
  temp_f = temp_f / 33.8;
  
  if (temp_f > 6){
      output = Particle.publish(0);
  }
  
  
  
  Particle.publish("temperature",String (temp_f), ALL_DEVICES);// sends data to cloud
  Particle.publish("output", String (output)), ALL_DEVICES;
  ThingSpeak.setField(1,temp_f);
  Serial.print(temp_f);
  Serial.print(output);
  Serial.println("temp_f");
  Serial.println("output");
  ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);
  delay(3000);

}
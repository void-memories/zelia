#include <MIDI.h>
MIDI_CREATE_DEFAULT_INSTANCE();

int cc = 0;
int AnalogValue = 0; // define variables for the controller data
int lastAnalogValue = 0;
int LED1=8;
int LED2=9;
int LED3=10;

void setup() {
  MIDI.begin(MIDI_CHANNEL_OMNI);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop()
{
  AnalogValue = analogRead(0);
  cc = AnalogValue/8;
  if (lastAnalogValue != cc) {
    MIDI.sendControlChange(16,cc,1);
    lastAnalogValue = cc;
  }

  if (MIDI.read()){
    switch(MIDI.getType())      // Get the type of the message we caught
        {   case midi::NoteOn:       // If it is a note on message,
            
                if( MIDI.getData2() == 0) // note off by zero velocity
                {
                  int incomingData=MIDI.getData2(); 
                  if(incomingData==8)
                  digitalWrite(LED1,LOW);
                  else if(incomingData==9)
                  digitalWrite(LED2,LOW);
                  else if(incomingData==10)
                  digitalWrite(LED3,LOW);
                }
                else
                {
                  int incomingData=MIDI.getData2();
                  if(incomingData==8)
                  digitalWrite(LED1,HIGH);
                  else if(incomingData==9)
                  digitalWrite(LED2,HIGH);
                  else if(incomingData==10)
                  digitalWrite(LED3,HIGH);
                }
                break;
            case midi::NoteOff:
            int incomingData=MIDI.getData2();
               if(incomingData==8)
                  digitalWrite(LED1,LOW);
                  else if(incomingData==9)
                  digitalWrite(LED2,LOW);
                  else if(incomingData==10)
                  digitalWrite(LED3,LOW);
               break;
            // See the online reference for other message types
            default:
                break;
        }
  }
}

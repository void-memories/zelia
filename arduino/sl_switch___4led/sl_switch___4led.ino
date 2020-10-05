#include <LiquidCrystal.h>

#include <MIDI.h>
MIDI_CREATE_DEFAULT_INSTANCE();

const int rs = 12, en = 11, d4 = A5, d5 = A4, d6 = A3, d7 = A2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int pot=A0;

int pushLed1;
int pushLed2;
int pushLed3;
int pushLed4;

int muxSelectorOne1=2;
int muxSelectorOne2=3;
int muxSelectorOne3=4;
int muxOutputOne=5;

int muxSelectorTwo1=6;
int muxSelectorTwo2=7;
int muxSelectorTwo3=8;
int muxOutputTwo=9;
int lastAnalogValue=-1;

int muxStates[8][3]={{0,0,0},{0,0,1},{0,1,0},{0,1,1},{1,0,0},{1,0,1},{1,1,0},{1,1,1}};
int lock[8]={0,0,0,0,0,0,0,0};

char queue[16];
int qLen=0;

int maj_min=1;
int chord_arp=1;
int l_1=1;
int play=0;



void setup() {
  MIDI.begin(MIDI_CHANNEL_OMNI);
  
//  Serial.begin(9600);
  lcd.begin(16, 2);
  
  
  
   pinMode(pot, INPUT);
   pinMode(muxSelectorOne1, OUTPUT);
   pinMode(muxSelectorOne2, OUTPUT);
   pinMode(muxSelectorOne3, OUTPUT);
   pinMode(muxSelectorTwo1, OUTPUT);
   pinMode(muxSelectorTwo2, OUTPUT);
   pinMode(muxSelectorTwo3, OUTPUT);
   pinMode(muxOutputOne, INPUT);
   pinMode(muxOutputTwo, INPUT);

   

}

void displayQueue(){
  for(int i=0;i<qLen;i++)
  lcd.print(queue[i]);
}

void loop() {





  
  for(int i=0;i<8;i++){
    
    digitalWrite(muxSelectorOne1,muxStates[i][0]);
    digitalWrite(muxSelectorOne2,muxStates[i][1]);
    digitalWrite(muxSelectorOne3,muxStates[i][2]);

    
    int buttonStatus=digitalRead(muxOutputOne);
//    Serial.print(buttonStatus);

    if(lock[i]!=buttonStatus){
      lock[i]=buttonStatus;
      switch(i){
        case 4:
        MIDI.sendControlChange(51,1,1);
        play^=1;
        break;

        case 5:
        MIDI.sendControlChange(52,1,1);
        chord_arp^=1;
        break;

        case 6:
        MIDI.sendControlChange(53,1,1);
        maj_min^=1;
        break;

        case 7:
        MIDI.sendControlChange(54,1,1);
        l_1^=1;
        break;
      }
    }
  }
    
    
//    }Serial.print(' ');

    lcd.clear();
//lcd.print("90 chord Cmaj LP"); 
if(play==0)
lcd.print("S");
else
lcd.print("P");

lcd.print(" ");

lcd.print((analogRead(pot)/10)*3);
int cc=analogRead(pot);
if (lastAnalogValue != cc) {
    MIDI.sendControlChange(55,cc/8,1);
    lastAnalogValue = cc;
  }

lcd.print(" ");

if(chord_arp==1)
lcd.print("chd");
else
lcd.print("arp");

lcd.print(" ");

if(maj_min==1)
lcd.print("maj");
else
lcd.print("min");

lcd.print(" ");

if(l_1==1)
lcd.print("LP");
else
lcd.print("1S");





lcd.setCursor(0,1);
  displayQueue();
    

    for(int i=0;i<8;i++){
    
    
    digitalWrite(muxSelectorTwo1,muxStates[i][0]);
    digitalWrite(muxSelectorTwo2,muxStates[i][1]);
    digitalWrite(muxSelectorTwo3,muxStates[i][2]);

    
    int buttonStatus=digitalRead(muxOutputTwo);
//    Serial.print(buttonStatus);

    if(buttonStatus){
      switch(i){
        case 0:
        queue[qLen]='C';
        qLen++;
        MIDI.sendControlChange(56,1,1);
        break;

        case 1:
        queue[qLen]='D';
        qLen++;
        MIDI.sendControlChange(57,1,1);
        break;

        case 2:
        queue[qLen]='E';
        qLen++;
        MIDI.sendControlChange(58,1,1);
        break;

        case 3:
        queue[qLen]='F';
        qLen++;
        MIDI.sendControlChange(59,1,1);
        break;

        case 4:
        queue[qLen]='G';
        qLen++;
        MIDI.sendControlChange(60,1,1);
        break;

        case 5:
        queue[qLen]='A';
        qLen++;
        MIDI.sendControlChange(61,1,1);
        break;

        case 6:
        queue[qLen]='B';
        qLen++;
        MIDI.sendControlChange(62,1,1);
        break;

        case 7:
        if(qLen>0)
        qLen--;
        MIDI.sendControlChange(63,1,1);
        break;
        
      }
      
    }
    
    
    }

    
    
//    Serial.println();
     delay(200);

}

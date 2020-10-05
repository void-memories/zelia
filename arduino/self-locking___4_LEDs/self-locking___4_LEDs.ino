int pushLed1;
int pushLed2;
int pushLed3;
int pushLed4;

int muxSelectorOne1=2;
int muxSelectorOne2=3;
int muxSelectorOne3=4;
int muxOutputOne=5;

int muxStates[8][3]={{0,0,0},{0,0,1},{0,1,0},{0,1,1},{1,0,0},{1,0,1},{1,1,0},{1,1,1}};

void setup() {
   pinMode(muxSelectorOne1, OUTPUT);
   pinMode(muxSelectorOne2, OUTPUT);
   pinMode(muxSelectorOne3, OUTPUT);
   pinMode(6, OUTPUT);
   pinMode(7, OUTPUT);
   pinMode(8, OUTPUT);
   pinMode(9, OUTPUT);
   pinMode(muxOutputOne, INPUT);

}

void loop() {
  for(int i=0;i<8;i++){
    digitalWrite(muxSelectorOne1,muxStates[i][0]);
    digitalWrite(muxSelectorOne2,muxStates[i][1]);
    digitalWrite(muxSelectorOne3,muxStates[i][2]);
    
    int buttonStatus=digitalRead(muxOutputOne);
    if(i==3)
    {
      if(buttonStatus==1)
      digitalWrite(6,HIGH);
      else if(buttonStatus==0)
      digitalWrite(6,LOW);
    }
    
    else if(i==4)
    {
      if(buttonStatus==1)
      digitalWrite(7,HIGH);
      else if(buttonStatus==0)
      digitalWrite(7,LOW);
    }
    else if(i==5)
    {
      if(buttonStatus==1)
      digitalWrite(8,HIGH);
      else if(buttonStatus==0)
      digitalWrite(8,LOW);
    }
    
    else if(i==6)
    {
      if(buttonStatus==1)
      digitalWrite(9,HIGH);
      else if(buttonStatus==0)
      digitalWrite(9,LOW);
    }
    
    }

}

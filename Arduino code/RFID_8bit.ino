#include <SPI.h>
#include <MFRC522.h>

#define ss_pin 10
#define rst_pin 9


MFRC522 rfid(ss_pin,rst_pin);


void setup() {
Serial.begin(9600);
SPI.begin();
rfid.PCD_Init();
}

void loop() {
  if (card_detected()){
    Serial.println(card_id());
    tone(7,3200);

  }else{
    noTone(7);
  }
}

bool card_detected(){
  if (!rfid.PICC_IsNewCardPresent())
  return false;
  if (!rfid.PICC_ReadCardSerial())
  return false;
  return true;
}

String card_id(){
  String id;
  for(byte i=0;i<4;i++){
    id+= String(rfid.uid.uidByte[i],HEX);
    if (i<3)id+=' ';
  }
  id.toUpperCase();
  rfid.PICC_HaltA();
  rfid.PCD_StopCrypto1();
  return id;
}

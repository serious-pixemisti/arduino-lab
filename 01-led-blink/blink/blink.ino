const int pinID = 6;
const int blinkDelay = 500;

void setup() {
  pinMode(pinID, OUTPUT);
}

void loop() {
  digitalWrite(pinID, HIGH);
  delay(blinkDelay);
  digitalWrite(pinID, LOW);
  delay(blinkDelay);
}

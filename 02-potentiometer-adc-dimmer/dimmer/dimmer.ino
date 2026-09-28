const int ledPin = 6;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  int potentValue = analogRead(A0);
  float brightness = map(potentValue, 0, 1023, 0, 255);

  analogWrite(ledPin, brightness);
}

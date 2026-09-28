const int sensorPin = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int tempoReading = analogRead(sensorPin);
  float millivolts = (tempoReading / 1023.0) * 5000.0;
  float tempC = millivolts / 10.0;
  Serial.println(tempC);
  delay(500);
}

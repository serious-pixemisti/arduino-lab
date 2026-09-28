# 02 — LED Brightness Control with Potentiometer and ADC

## Objective

Write a simple Arduino program that uses PWM (rather than a voltage division) to dim an LED using a potentiometer

## Components

- Arduino Uno R3
- LED
- 220 ohm resistor
- Potentiometer
- Breadboard
- Jumper wires

## What I learned

- How to use `analogWrite()` to do PWM
- Mapping a value from one range to another using `map()`

## Code

See `dimmer.ino`.

## Result

Potentiometer provides a voltage to the ADC which returns a value from 0-1023. This is mapped to 0-255 and this new value is used as a brightness value for an LED causing the LED to have variable brightness based on the potentiometer setting.
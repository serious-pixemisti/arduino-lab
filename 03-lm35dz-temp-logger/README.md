# 02 — LM35DZ Sensor Reading and Logging

## Objective

Log about 100 seconds worth of temperature readings to a CSV file and plot a graph from the data.

## Components

- Arduino Uno R3
- LM35DZ Sensor
- Breadboard
- Jumper wires

## What I learned

- How to use Serial in Arduino sketches
- How to use `pyserial` to read Serial output from Arduino sketches in Python
- Saving a DataFrame to a CSV file using Pandas' `.to_csv()` function
- How to plot data from a CSV using Matplotlib Pyplot

## Code

See `temp_reader.ino`, `logger.py`, and `plotter.py`.

## Result

See `lm35dz_log_1.csv` for the data.
See `lm35dz_plot_1.png` for the chart.

Potentiometer provides a voltage to the ADC which returns a value from 0-1023. This is mapped to 0-255 and this new value is used as a brightness value for an LED causing the LED to have variable brightness based on the potentiometer setting.
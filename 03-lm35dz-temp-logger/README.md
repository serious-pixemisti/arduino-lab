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

The LM35DZ was sampled by the Arduino approximately every
0.5 seconds. The Arduino converted the ADC reading into a
temperature estimate and transmitted the measurements over
Serial.

A Python script collected the readings and saved them to a CSV
file using Pandas. The resulting data was then plotted using
Matplotlib.
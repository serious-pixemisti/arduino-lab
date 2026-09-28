import numpy as np
import pandas as pd
import serial
import time

READINGS = 200

arduino = serial.Serial("COM6", 9600)

times = np.zeros(READINGS)
temps = np.zeros(READINGS)

i = 0
start_time = time.time()

while i < READINGS:
    line = arduino.readline().decode('utf-8').strip()
    temperature = float(line)
    elapsed = time.time() - start_time

    times[i] = elapsed
    temps[i] = temperature
    
    i += 1
    print(f"Reading {i}/{READINGS} logged...")

log = pd.DataFrame({
    "time": times,
    "temperature": temps
})
log.to_csv("lm35dz_log_1.csv", index=False)

print("Logging Done!")
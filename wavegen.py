#!/usr/bin/env python3

import numpy as np
from scipy.io import wavfile
from scipy import signal
import os

sampleRate = 48000

t = np.linspace(0, 1, 2048)

work_dir = 'digital'

try:
  os.mkdir(work_dir)
except OSError as error:
  print('')

os.chdir(work_dir)
dir_digital = '[digital] '

y = np.sin(2 * np.pi * t)
y = y.astype('float32')
wavfile.write(dir_digital + 'sine.wav', sampleRate, y)

y = np.sin(np.pi * t)
y = y.astype('float32')
wavfile.write(dir_digital + 'half sine up.wav', sampleRate, y)

y = np.sin(np.pi + np.pi * t)
y = y.astype('float32')
wavfile.write(dir_digital + 'half sine down.wav', sampleRate, y)

y = np.cos(2 * np.pi * t)
y = y.astype('float32')
wavfile.write(dir_digital + 'cosine.wav', sampleRate, y)

y = np.cos(np.pi * t)
y = y.astype('float32')
wavfile.write(dir_digital + 'half cosine.wav', sampleRate, y)

y = signal.square(2 * np.pi * t, 0.5)
y = y.astype('float32')
wavfile.write(dir_digital + 'square.wav', sampleRate, y)

y = signal.sawtooth(2 * np.pi * t, 0.5)
y = y.astype('float32')
wavfile.write(dir_digital + 'triangle.wav', sampleRate, y)

y = signal.sawtooth(2 * np.pi * t, 1)
y = y.astype('float32')
wavfile.write(dir_digital + 'ramp.wav', sampleRate, y)

y = signal.sawtooth(2 * np.pi * t, 0)
y = y.astype('float32')
wavfile.write(dir_digital + 'sawtooth.wav', sampleRate, y)

y = signal.sawtooth(np.pi + 2 * np.pi * t, 0)
y = y.astype('float32')
wavfile.write(dir_digital + 'sawtooth shift.wav', sampleRate, y)

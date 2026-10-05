# -*- coding: utf-8 -*-
import sympy as sym
from sympy.plotting import plot

t = sym.symbols('t')

def get_analog_signal(t, A=1, f=1/10, phi=0):
    return A*sym.sin(2 * sym.pi * f * t + phi)

def get_digital_signal(A=1, f=1/10, phi=0, fs=20, t_final=1):
    import numpy as np

    T = 1 / fs
    t_digital = np.arange(0, t_final, T)
    return t_digital, A * np.sin(2 * np.pi * f * t_digital + phi)

def get_analog_signal_energy(signal):
    return sym.integrate(abs(signal)**2, (t, -sym.oo, sym.oo))

def get_analog_signal_power(signal):
    # sym.limit((1/(2*T)*sym.integrate(f,(t,-sym.oo, sym.oo))),T,sym.oo)
    return get_analog_signal_energy(signal) / (2 * sym.pi)

def plot_analog_signal(signal, t_range=(0, 1), title='Signal'):

    plot(signal, (t, t_range[0], t_range[1]),  title=title, xlabel='Time (s)', ylabel='Amplitude')

def plot_digital_signal(t, signal, t_range=(0, 1), title='Digital Signal'):
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 5))
    plt.plot(t, signal, '.')
    plt.title(title)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.show()

if __name__ == "__main__":
    A = 1  # Amplitud
    f = 1  # Frecuencia
    phi = 0  # Fase
    t_final = 10
    fs = 2

    #analog_signal = get_analog_signal(t, A, f, phi)
    #plot_analog_signal(analog_signal, t_range=(-20, 20), title='Sine Wave Analog Signal')

   
    n,digital_signal = get_digital_signal(A, f, phi, fs, t_final)
    plot_digital_signal(n, digital_signal, t_range=(0, t_final), title='Sine Wave Digital Signal')
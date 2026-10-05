import signal_tool as sig
#phi=sig.sym.pi/2


signal = sig.get_analog_signal(sig.t, A=1, f=1/13, phi=0)
energia = sig.get_analog_signal_energy(signal)
sig.plot_analog_signal(signal,(-30,30),title='Sine Wave Signal')
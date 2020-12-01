def moteur(signal_x,signal_y):
    if signal_x!=0:
        if signal_x<0:
            moteur1_signal=1
            moteur2_signal=signal_y
        else:
            moteur1_signal=signal_y
            moteur2_signal=1
    else:
        moteur1_signal=signal_y
        moteur2_signal=signal_y
    print(moteur1_signal, moteur2_signal)


moteur(1,1)

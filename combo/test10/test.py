import threading
import time
import pandas as pd

from objects.clarius import clarius
from objects.emg import emg
from objects.shimmer import shimmer

record_duration = 5  # length in seconds to record, max 10-20 sec

emg_enable = False
clar_enable = False
shimmer_enable = True

if emg_enable:
    emg = emg()
    emg_thread = threading.Thread(target=emg.record, args=(record_duration,))

if clar_enable:
    clar = clarius
    clar_thread = threading.Thread(target=clar.record, args=(record_duration,))

if shimmer_enable:
    shim = shimmer("com4", sampling_rate=500)
    if shim.connect():

        # make thread
        shim_thread = threading.Thread(
            target=shim.record,
            args=(record_duration, shim.port, "data/shimmer_data.csv"),
        )

    shim2 = shimmer("com7", sampling_rate=500)
    if shim2.connect():

        # make thread
        shim2_thread = threading.Thread(
            target=shim2.record,
            args=(record_duration, shim2.port, "data/shimmer_data.csv"),
        )


time.sleep(3)  # wait for the deiveces to connect
if emg_enable:
    emg_thread.start()

if clar_enable:
    clar_thread.start()

if shimmer_enable:
    shim_thread.start()
    shim2_thread.start()


if emg_enable:
    emg_thread.join()
    emg.get_EEG("data/data_eeg.csv")
    emg.get_acceleration("data/data_imu.csv")
    emg.get_timestamp("data/emg_timestamp.csv")

if clar_enable:
    clar_thread.join()
    clar.quit()

if shimmer_enable:
    shim_thread.join()
    shim2_thread.join()

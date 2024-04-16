import threading
import time
import pandas as pd

from objects.clarius import clarius
from objects.emg import emg
from objects.shimmer import shimmer

record_duration = 5  # length in seconds to record, max 10-20 sec

emg = emg()
clar = clarius()
shim = shimmer()

emg_thread = threading.Thread(target=emg.record, args=(record_duration,))
clar_thread = threading.Thread(target=clar.record, args=(record_duration,))
shim_thread = threading.Thread(target=shim.record, args=(record_duration,))

time.sleep(3)  # wait for the deiveces to connect

if shim.connect("com8", sampling_rate=500):
    emg_thread.start()
    clar_thread.start()

    emg_thread.join()
    clar_thread.join()

# clar save data in the c++ code
pd.DataFrame(emg.get_EEG()).to_csv("data/data_emg.csv", index=False)

clar.quit()

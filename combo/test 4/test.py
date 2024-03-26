import threading
import time
import pandas as pd

from EMG import EMG
from clarius import Clarius


# def initialize_class():
#     emg = EMG()
#     clar = Clarius()
#     return emg, clar  # Return the instances


# initialize_thread = threading.Thread(target=initialize_class)

# initialize_thread.start()

# initialize_thread.join()


def emg_record():
    emg.record(5)


def clar_record():
    clar.clarius_record(5)


emg = EMG()
clar = Clarius()

emg_thread = threading.Thread(target=emg_record)
clar_thread = threading.Thread(target=clar_record)

time.sleep(3)

emg_thread.start()
clar_thread.start()


# emg.record(5)
# clar.clarius_record(5)

emg_thread.join()
clar_thread.join()

pd.DataFrame(emg.get_EEG()).to_csv("data_emg.csv", index=False)
clar.quit()

import subprocess
import threading
import pandas as pd
import time

from EMG import EMG

emg = EMG


def start_EMG():
    emg.record(5)
    pd.DataFrame(emg.get_EEG()).to_csv("data.csv", index=False)


def read_output(stream, output_type):
    for line in stream:
        print(f"Received {output_type}: {line.strip()}")


def clarius_timer(delay, process):
    process.stdin.write("f" + "\n")
    process.stdin.flush()
    time.sleep(delay)
    cmd = ["f", "r", "y"]
    for x in cmd:
        process.stdin.write(x + "\n")
        process.stdin.flush()
        time.sleep(3)


def listen_for_output(process):
    read_output(process.stdout, "stdout")


def listen_for_error(process):
    read_output(process.stderr, "stderr")


def communicate_with_cpp():
    process = subprocess.Popen(
        ["./main"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Start threads to listen for stdout and stderr
    stdout_thread = threading.Thread(target=listen_for_output, args=(process,))
    stderr_thread = threading.Thread(target=listen_for_error, args=(process,))
    stdout_thread.start()
    stderr_thread.start()

    try:
        while True:
            # Get user input
            user_input = input(
                "Enter a message to send to the subprocess (type 'exit' to quit): "
            )

            # Send input to the subprocess's stdin
            process.stdin.write(user_input + "\n")
            process.stdin.flush()

            # Check if user wants to exit
            if user_input.lower() == "exit":
                break
    except KeyboardInterrupt:
        pass
    finally:
        # Close stdin to signal end of input
        process.stdin.close()

    # Wait for the subprocess to complete
    process.wait()


# Example usage
# communicate_with_cpp()

clarius = threading.Thread(target=communicate_with_cpp)
clarius_timer_thread = threading.Thread(target=clarius_timer)
emg_thread = threading.Thread(target=start_EMG)

clarius_timer_thread.start()
clarius.start()
emg_thread.start()

clarius_timer_thread.wait()
clarius.wait()
emg_thread.wait()

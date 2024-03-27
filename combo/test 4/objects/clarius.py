import subprocess
import threading
import time


class clarius:
    def __init__(self):
        self.process = subprocess.Popen(
            ["./main"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

        # Start threads to listen for stdout and stderr
        stdout_thread = threading.Thread(target=self.listen_for_output)
        stderr_thread = threading.Thread(target=self.listen_for_error)
        stdout_thread.start()
        stderr_thread.start()

    def read_output(self, stream, output_type):
        for line in stream:
            print(f"Received {output_type}: {line.strip()}")
            self.output = line

    def listen_for_output(self):
        self.read_output(self.process.stdout, "stdout")

    def listen_for_error(self):
        self.read_output(self.process.stderr, "stderr")

    def record(self, delay):
        print("clar start")
        self.process.stdin.write("f" + "\n")
        self.process.stdin.flush()
        time.sleep(delay)
        self.process.stdin.write("f" + "\n")
        self.process.stdin.flush()

        while True:
            if "frozen" in self.output:  # Check if "frozen" is in the output
                print("r")
                self.process.stdin.write("r" + "\n")
                self.process.stdin.flush()
                break  # Break the loop once "frozen" is found
            time.sleep(0.3)  # Wait for a short duration before checking again

        # Loop until the "raw file" string is received
        while True:
            if "raw data" in self.output:  # Check if "raw file" is in the output
                print("y")
                self.process.stdin.write("y" + "\n")
                self.process.stdin.flush()
                break  # Break the loop once "raw file" is found
            time.sleep(0.3)  # Wait for a short duration before checking again

        while True:
            if "successfully" in self.output:  # Check if "raw file" is in the output
                self.process.stdin.write("y" + "\n")
                self.process.stdin.flush()
                break  # Break the loop once "raw file" is found
            time.sleep(0.3)  # Wait for a short duration before checking again

    def quit(self):
        self.process.stdin.write("q" + "\n")
        self.process.stdin.flush()


if __name__ == "__main__":
    clar = clarius()
    time.sleep(3)
    t = threading.Thread(target=clar.record, args=(5,))
    t.start()
    t.join()
    clar.quit()

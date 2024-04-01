import subprocess
import threading
import time


class Clarius:
    def __init__(self):
        self.connected = False
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

    def listen_for_output(self):
        self.read_output(self.process.stdout, "stdout")

    def listen_for_error(self):
        self.read_output(self.process.stderr, "stderr")

    def clarius_timer(self, delay):
        self.process.stdin.write("f" + "\n")
        self.process.stdin.flush()
        time.sleep(delay)
        cmd = ["f", "r", "y"]
        for x in cmd:
            self.process.stdin.write(x + "\n")
            self.process.stdin.flush()
            time.sleep(5)
        time.sleep(5)

    def quit(self):
        self.process.stdin.write("q" + "\n")
        self.process.stdin.flush()
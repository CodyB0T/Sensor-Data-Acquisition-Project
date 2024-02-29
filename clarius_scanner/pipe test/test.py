import subprocess
import threading
import time


def read_output():
    output = process.stdout.readline().strip()
    print(output)


cpp_program = "./test"

process = subprocess.Popen(
    cpp_program,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)

stdout_thread = threading.Thread(target=read_output)

input_string = input("input start: ")
stdout_thread.start()
process.stdin.write(input_string + "\n")
process.stdin.flush()

for x in range(0, 5):
    print(x)
    time.sleep(1)

stdout_thread.join()

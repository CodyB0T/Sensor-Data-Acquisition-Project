# import subprocess
# import threading
# import time


# def read_output():
#     output = process.stdout.readline().strip()
#     print(output)


# cpp_program = "./main2"

# process = subprocess.Popen(
#     cpp_program,
#     stdin=subprocess.PIPE,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True,
# )

# # stdout_thread = threading.Thread(target=read_output)

# # input_string = input("input start: ")
# # stdout_thread.start()
# # process.stdin.write(input_string + "\n")
# # process.stdin.flush()

# # for x in range(0, 5):
# #     print(x)
# #     time.sleep(1)

# # stdout_thread.join()
# while True:
#     output = process.stdout.readline().strip()
#     err = process.stderr.readline().strip()
#     print(output + err)

# import subprocess
# import threading


# def read_output(stream, output_type):
#     for line in stream:
#         print(f"Received {output_type}: {line.strip()}")


# def listen_for_output(process):
#     read_output(process.stdout, "stdout")


# def listen_for_error(process):
#     read_output(process.stderr, "stderr")


# def communicate_with_cpp():
#     process = subprocess.Popen(
#         ["./main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
#     )

#     # Start threads to listen for stdout and stderr
#     stdout_thread = threading.Thread(target=listen_for_output, args=(process,))
#     stderr_thread = threading.Thread(target=listen_for_error, args=(process,))
#     stdout_thread.start()
#     stderr_thread.start()

#     # Wait for the subprocess to complete
#     process.wait()


# # Example usage
# communicate_with_cpp()
import subprocess
import threading


def read_output(stream, output_type):
    for line in stream:
        print(f"Received {output_type}: {line.strip()}")


def listen_for_output(process):
    read_output(process.stdout, "stdout")


def listen_for_error(process):
    read_output(process.stderr, "stderr")


def communicate_with_cpp():
    process = subprocess.Popen(
        ["./main2"],
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
communicate_with_cpp()

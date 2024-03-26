while True:
            if "frozen" in self.output:  # Check if "frozen" is in the output
                self.process.stdin.write("r" + "\n")
                self.process.stdin.flush()
                break  # Break the loop once "frozen" is found
            time.sleep(0.3)  # Wait for a short duration before checking again

        # Loop until the "raw file" string is received
        while True:
            if "raw file" in self.output:  # Check if "raw file" is in the output
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
import subprocess
import requests

class network_signal:
    def __init__(self):
        pass

    def check_connection(self):
        command = ["hostname", "-I"]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Communicate with the process (waits for it to terminate)
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            if stdout.strip()=='':
                print("No network connection.")
                return False
            else:
                print("Output:", stdout)
                return True
        else:
            print("Error:", stderr)
            return False


    def check_internet_connection(self,url='https://www.google.com/', timeout=5):
        """
        Checks if the system has network connectivity by attempting an HTTP GET request.
        """
        try:
            # Send a HEAD request to minimize data transfer
            requests.head(url, timeout=timeout) 
            return True
        except requests.ConnectionError:
            return False
        except requests.Timeout:
            return False

    



net=network_signal()
print(net.check_connection())
print(net.check_internet_connection())

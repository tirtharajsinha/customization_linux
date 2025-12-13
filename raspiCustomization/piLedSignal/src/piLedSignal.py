from pi5neo import Pi5Neo
import time
from math import cos
import multiprocessing
import subprocess
from netcheck import network_signal


# NEOPIXEL_PIN GPIO10 / Pin 19
LED_COUNT=1
TRAGET_LEDS=[0]

TRIGGER=True








class illumination():
    def __init__(self,LED_COUNT,TRAGET_LEDS=[0]):
        self.LED_COUNT=LED_COUNT
        self.TRAGET_LEDS=TRAGET_LEDS
        self.neo=Pi5Neo("/dev/spidev0.0", LED_COUNT, spi_speed_khz=800)
        self.colors = {
            "red": (100, 0, 0),
            "orange": (255, 127, 0),
            "yellow": (255, 255, 0),
            "green": (0, 125, 0),
            "blue": (0, 0, 100),
            "indigo": (75, 0, 130),
            "violet": (148, 0, 211),
            "white": (255, 255, 255)
        }
        self.colors_list = list(self.colors.values())

    def ON(self,color='white',color_code=None):
        if color is None and color_code is None:
            return
        if color_code is None:
            color_code=self.colors[color]
        for l in TRAGET_LEDS:
            self.neo.set_led_color(l, *color_code)
        self.neo.update_strip()

    def OFF(self):
        for l in TRAGET_LEDS:
            self.neo.set_led_color(l, 0,0,0)
        self.neo.update_strip()
    
    def blink(self,color='white',color_code=None):
        while True:
            self.ON(color,color_code)
            time.sleep(0.5)
            self.OFF()
            time.sleep(0.5)
    
    def fast_blink(self,color='white',color_code=None):
        while True:
            self.ON(color,color_code)
            time.sleep(0.01)
            self.OFF()
            time.sleep(0.01)

    def pulse(self,color='white',timeout=15,color_code=None):
        
        if color is None and color_code is None:
            return
        if color_code is None:
            color_code=self.colors[color]
        start = time.perf_counter()
        while True:
            t=time.time()
            for i in self.TRAGET_LEDS:
                r = int((cos(i * 0.8 + t) * 0.5 + .5) * color_code[0])
                g =  int((cos(i * 0.8 + t) * 0.5 + .5) * color_code[1])
                b = int((cos(i * 0.8 + t) * 0.5 + .5) * color_code[2])
                self.neo.set_led_color(i, r, g, b)
                self.neo.update_strip(sleep_duration=0.001)
            if time.perf_counter() - start > timeout:
                print('Standing by...')
                self.OFF()
                break

    def reset_strip(self):
        self.neo.clear_strip()
        self.neo.update_strip()



def check_network_status(queue,net):
    global TRIGGER
    """Check network status and send updates to the queue."""
    previous_status = None
    while True:
        if net.check_connection():  # Assuming this returns True/False for connectivity
            if net.check_internet_connection():
                status = "netconnected"
            else:
                status = "connected"
        else:
            status = "disconnected"

        if status != previous_status:
            queue.put(status)
            previous_status = status
            TRIGGER=True
        else:
            TRIGGER=False

        time.sleep(5)  # Check every 5 seconds

def handle_led_notifications(queue,noti):
    """Handle LED notifications based on network status."""
   
    current_process = None

    while True:
        status = queue.get()  # Wait for a status update

        # Kill the current LED process if running
        if TRIGGER and current_process and current_process.is_alive():
            current_process.terminate()
            noti.reset_strip()

        # Start a new LED process based on the status
        if status == "netconnected":
            current_process = multiprocessing.Process(target=noti.pulse, args=("green",))
        elif status == "connected":
            current_process = multiprocessing.Process(target=noti.blink, args=("blue",))
        elif status == "disconnected":
            current_process = multiprocessing.Process(target=noti.fast_blink, args=("red",))

        if current_process:
            current_process.start()








if __name__ == '__main__':
    status_queue = multiprocessing.Queue()
    net=network_signal()
    noti = illumination(LED_COUNT)

    # Start the network check process
    network_process = multiprocessing.Process(target=check_network_status, args=(status_queue,net,))
    network_process.start()

    # Start the LED notification handler process
    led_process = multiprocessing.Process(target=handle_led_notifications, args=(status_queue,noti,))
    led_process.start()

    # Wait for processes to complete (they won't, as they're infinite loops)
    network_process.join()
    led_process.join()







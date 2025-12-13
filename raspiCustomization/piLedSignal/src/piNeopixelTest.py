from pi5neo import Pi5Neo
import time
from math import cos
# NEOPIXEL_PIN GPIO10 / Pin 19
LED_COUNT=1

neo = Pi5Neo("/dev/spidev0.0", LED_COUNT, spi_speed_khz=800)

colors = [
    (255, 0, 0),  # Red
    (255, 127, 0),  # Orange
    (255, 255, 0),  # Yellow
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (75, 0, 130),  # Indigo
    (148, 0, 211)  # Violet
]

def rainbow_cycle(neo, delay=0.1):
    for _ in range(5):
        for color in colors:
            neo.fill_strip(*color)
            neo.update_strip()
            time.sleep(delay)

def loading_bar(neo):
    while True:
        for color in colors:
            for i in range(neo.num_leds):
                neo.set_led_color(i, *color)  # Green loading bar
                neo.update_strip()
                time.sleep(0.05)
        
def ripple(neo,  delay=0.1):
    center = neo.num_leds // 2  # Center of the strip
    while True:
        for color in colors:
            for radius in range(neo.num_leds // 2 + 1):
                neo.fill_strip(0, 0, 0)
                if center - radius >= 0:
                    neo.set_led_color(center - radius, *color)
                if center + radius < neo.num_leds:
                    neo.set_led_color(center + radius, *color)
                neo.update_strip()
                time.sleep(delay)    

def smooth_fade(neo):
    while True:
        t=time.time()
        for i in range(neo.num_leds):
            intensity = int((cos(i * 0.01 + t) * 0.5 + 0.5) * 255)
            neo.set_led_color(i, intensity, intensity, intensity)
        neo.update_strip(sleep_duration=0.01)

def pulse(neo, color_code=(255, 255, 255), step=0.1):
    """
    Creates a faster pulsing effect by increasing the rate of brightness changes.

    Args:
        neo: The Pi5Neo object controlling the LEDs.
        color_code: Tuple representing the RGB color to pulse.
        step: The rate at which brightness changes (larger values = faster transitions).
    """
    r, g, b = color_code
    brightness = 0.0  # Start with the lowest brightness
    increasing = True  # Flag to track whether brightness is increasing or decreasing

    while True:
        # Calculate the current brightness level
        current_r = int(r * brightness)
        current_g = int(g * brightness)
        current_b = int(b * brightness)

        # Set the LED color with the current brightness
        neo.set_led_color(0, current_r, current_g, current_b)
        neo.update_strip()

        # Adjust brightness
        if increasing:
            brightness += step
            if brightness >= 1.0:  # Reached maximum brightness
                brightness = 1.0
                increasing = False
        else:
            brightness -= step
            if brightness <= 0.0:  # Reached minimum brightness
                brightness = 0.0
                increasing = True

        time.sleep(0.03)  # Reduced delay for faster transitions

def reset_strip(neo):
    neo.clear_strip()
    neo.update_strip()



try:
    #rainbow_cycle(neo)
    #loading_bar(neo)
    #ripple(neo)
    # smooth_fade(neo)
    pulse(neo)
except KeyboardInterrupt:
    reset_strip(neo)
except Exception as e:
    print(e)

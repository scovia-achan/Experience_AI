import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define pin numbers for lights
green_pin = 17
red_pin = 22
yellow_pin = 23


# Set up pins as outputs and ensure they start OFF
GPIO.setup(red_pin, GPIO.OUT)
GPIO.setup(yellow_pin, GPIO.OUT)
GPIO.setup(green_pin, GPIO.OUT)

# Initialize all lights to OFF
GPIO.output(red_pin, GPIO.LOW)
GPIO.output(yellow_pin, GPIO.LOW)
GPIO.output(green_pin, GPIO.LOW)

def debug_print(message):
    """Helper function to print debug messages with timestamps"""
    print(f"{time.strftime('%H:%M:%S')}: {message}")

def traffic_light_sequence():
    try:
        while True:
            # Turn on red light
            debug_print("Red light ON: Pedestrians cross")
            GPIO.output(red_pin, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(red_pin, GPIO.LOW)
            debug_print("Red light OFF")
            
            # Turn on yellow light
            debug_print("Amber light ON")
            GPIO.output(yellow_pin, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(yellow_pin, GPIO.LOW)
            debug_print("Amber light OFF")
            
            # Turn on green light
            debug_print("Green light ON")
            GPIO.output(green_pin, GPIO.HIGH)
            time.sleep(4)
            GPIO.output(green_pin, GPIO.LOW)
            debug_print("Green light OFF")
                 
            
    except KeyboardInterrupt:
        debug_print("Program terminated by user")
        GPIO.cleanup()
    except Exception as e:
        debug_print(f"An error occurred: {str(e)}")
        GPIO.cleanup()

if __name__ == "__main__":
    debug_print("Starting traffic light sequence")
    # Ensure all lights are off before starting
    GPIO.output(red_pin, GPIO.LOW)
    GPIO.output(yellow_pin, GPIO.LOW)
    GPIO.output(green_pin, GPIO.LOW)
    traffic_light_sequence()
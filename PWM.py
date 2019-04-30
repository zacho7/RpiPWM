import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

led = 18
trig = 17
echo = 27
end = 0

GPIO.setup(led, GPIO.OUT)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
p = GPIO.PWM(18, 50)
p.start(0)

while True:
    
    GPIO.output(trig, True)
    time.sleep(0.001)
    GPIO.output(trig, False)
        
    while GPIO.input(echo) == False:
        start = time.time()
            
    while GPIO.input(echo) == True:
        end = time.time()
        
    dtime = end - start
        
    distance = dtime / 0.000058
    
    p.ChangeDutyCycle(100 / distance)

    print("Distance:")
    print(distance)
    
    




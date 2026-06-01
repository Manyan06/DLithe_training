import datetime
import time
import winsound

def alarm_clock():
  print("===Alarm_Clock===")
  alarm_time = input("Enter alarm time HH:MM:SS in 24-hour format: ")
  try:
    datetime.datetime.strptime(alarm_time, "%H:%M:%S")
  except ValueError:
    print("Invalid time format! Please use HH:MM:SS")
    return
  print(f"Alarm set for {alarm_time}... ")
  while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"\nCurrent Time: {current_time}", end="")
    if current_time == alarm_time:
      print("\n\nWake Up! Alarm Ringing...")
      for _ in range(10):
        winsound.Beep(1000,500)
      break
    time.sleep(1)
alarm_clock()

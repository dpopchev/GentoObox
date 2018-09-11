from datetime import datetime, timedelta

sleep_cycle = 90; fall_sleep = 15;
time_now = datetime.now();

wake_up = [ (time_now + timedelta(minutes=i*sleep_cycle) + timedelta(minutes=fall_sleep) ).strftime('%H:%M') for i in range(1,7) ];

for i in wake_up:
	print( i, end=' ')

print();
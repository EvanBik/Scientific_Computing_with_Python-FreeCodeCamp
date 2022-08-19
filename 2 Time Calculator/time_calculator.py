def add_time(start, duration, start_day=False):
	time_s, am_pm = start.split()
	hour_s, minutes_s = time_s.split(":")
	hour_d, minutes_d = duration.split(":")
	if am_pm == "PM":
		hour_s = int(hour_s)+12
		hour_s = str(hour_s)
	hour_new = int(hour_s)+int(hour_d)
	minutes_new = int(minutes_s)+int(minutes_d)
	if minutes_new >= 60:
		add_hour = minutes_new//60
		minutes_new -= add_hour * 60
		hour_new += add_hour
	numdays = 0
	if hour_new > 24:
		numdays = hour_new // 24
		hour_new -= numdays * 24
	if hour_new > 0 and hour_new < 12:
		am_pm = "AM"
	elif hour_new == 12:
		am_pm = "PM"
	elif hour_new > 12:
		am_pm = "PM"
		hour_new -= 12
	else:
		am_pm = "AM"
		hour_new += 12
	if minutes_new < 10:
		minutes_new = "0" + str(minutes_new)
	days = ""
	if numdays > 0:
		if numdays == 1:
			days = " (next day)"
		else:
			days = f" ({numdays} days later)"
	week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
	nameday = ""
	if start_day:
		i = 0
		while True:
			if week[i] == start_day.lower().capitalize():
				break
			i += 1
		weeks = numdays // 7
		x = i + (numdays - 7 * weeks)
		if x > 6:
			x -= 7
		nameday = ", " + week[x] 
	new_time = str(hour_new) + ":" + str(minutes_new) + " " + am_pm + nameday + days
	return new_time
def second_since_midnight(hour,minutes,second):
	hour_in_seconds = hour *60 * 60
	minute_in_seconds = (minutes * 60) + second

	result = hour_in_seconds + minute_in_seconds
	return result

print(second_since_midnight(13,30, 45))

	
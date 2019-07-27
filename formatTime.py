#this module formats time into seconds, minutes, hours and days
import datetime

def formatTime(startTime, endTime):
	elapsedTime = endTime - startTime

	days = round(elapsedTime.days,1)
	seconds = round(elapsedTime.seconds)
	hours = round(seconds/3600,1)
	minutes = round(seconds/60)

	if days >= 1:
		time = {
			'durationType': 'days',
			'duration': days
		}
	elif hours >= 1:
		time = {
			'durationType': 'hours',
			'duration': hours
		}
	elif minutes >= 1:
		time = {
			'durationType': 'minutes',
			'duration': minutes
		}
	else:
		time = {
			'durationType': 'seconds',
			'duration': seconds
		}
	return time




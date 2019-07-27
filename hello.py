import datetime

task = input("🎹 What am I doing now: ")
startDate = datetime.datetime.now()

print(f"⏱ you are working on {task}, starting from {startDate}")
endTrigger = input("🎹 type * when finished: ")

while endTrigger != "*":
	endTrigger = input("🎹 type * when finished: ")

endTime = datetime.datetime.now()
elapsedDate = endTime - startDate

def formatTime(elapsedDate):
	if elapsedDate.days >= 1:
		time = {
			'durationType': 'days',
			'duration': elapsedDate.days
		}
	else:
		time = {
			'durationType': 'seconds',
			'duration': elapsedDate.seconds
		}
	return time
# TODO add an if else for hours, and minutes

formattedTime = formatTime(elapsedDate)
print(f"🌈 elapsed time is {formattedTime.get('duration')} {formattedTime.get('durationType')}")


# TODOs
# format start time and endtime strings  with formatDate
# format elapsedDate to be human readible, nearest seconds, mins, etc,.

# save it to a place
	# can save to a file, plain txt then csv
		# look for csv library (will require setting up requirements.txt)
	# save to a google doc

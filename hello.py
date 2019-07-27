import datetime
import formatTime


task = input("🎹 What am I doing now: ")
startTime = datetime.datetime.now()

print(f"⏱ you are working on {task}, starting from {startTime}")
endTrigger = input("🎹 type * when finished: ")

while endTrigger != "*":
	endTrigger = input("🎹 type * when finished: ")

endTime = datetime.datetime.now()

formattedTime = formatTime.formatTime(startTime, endTime)
print(f"🌈 elapsed time is {formattedTime.get('duration')} {formattedTime.get('durationType')}")


# TODOs

# x turn formatTime() into a seperate module

# xformat start time and endtime strings  with formatDate
# xformat elapsedDate to be human readible, nearest seconds, mins, etc,.

# save it to a place
	# can save to a file, plain txt then csv
		# look for csv library (will require setting up requirements.txt)
	# save to a google doc

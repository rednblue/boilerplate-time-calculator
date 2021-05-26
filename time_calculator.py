# Version 0.1 of add_time function
# This version simply satisfies the unit tests without any improvement to code performance. 
# I might come back to tackle some of the shortcuts taken to make it work

def add_time(start, duration, *args):

  new_time = None
  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

  hourPart = start.index(":")
  minutePart = start.index(" ")
  
  sHour = int(start[:hourPart])
  sMinute = int(start[hourPart+1:minutePart])
  sAMPM = start[minutePart+1:]

  hourPart = duration.index(":")
  dHour = int(duration[:hourPart])
  dMinute = int(duration[hourPart+1:])

  day = None
  for argument in args:
    day = argument.lower()

  dint = 0
  for d in days:
    if d == day:
      break
    dint += 1

  nHour = sHour
  nMinute = sMinute

  if(sAMPM == "PM"):
    nHour += 12

  nMinute = sMinute + dMinute
  if(nMinute > 60):
    nMinute = nMinute - 60
    nHour += 1

  tHour = nHour + dHour
  nHour = tHour % 24
  
  dayAfter = int(tHour / 24)



  nAMPM = "AM"
  if(nHour > 12):
    nAMPM = "PM"
    nHour = nHour - 12

  nMinuteStr = str(nMinute)
  if(nMinute < 10):
    nMinuteStr = "0" + nMinuteStr

  nHourStr = str(nHour)
  
  if(nHour == 0 and nAMPM == "AM"):
    nHourStr = "12"

  if(nHour == 12 and nAMPM == "AM"):
    nAMPM = "PM"

  new_time = nHourStr + ":" + nMinuteStr + " " + nAMPM  

  if(day is not None):
    dint = dint + dayAfter
    d = days[dint%7]
    new_time += ", " + d.title()

  if(dayAfter == 1):
    new_time += " (next day)"
  elif(dayAfter > 1):
    new_time += " (" + str(dayAfter) + " days later)"

  return new_time
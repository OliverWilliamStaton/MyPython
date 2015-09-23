import sys
import os
import urllib2

# flight = "UAL3393"
flight = "ASQ4367/history/20150919/1448Z/KSDF/KORD"
output = ""


def append_str(str, element):
	str = str + element
	return str

def display_time(fill_time, empty_time):

	print("Time Passed:    " + fill_time)
	print("Time Remaining: " + empty_time)

def display_graph(fill_count, empty_count):

	output = "|"
	for x in range (0, fill_count):
		output = append_str(output, "*")
	for x in range (0, empty_count):
		output = append_str(output, "-")
	output = append_str(output, "|")

	print(output)
	print(output)
	print(output)

def main():

	content = urllib2.urlopen("https://flightaware.com/live/flight/" + flight).read()

	fill_content = content[
		content.find("track-panel-progress-fill")+41:
		content.find("track-panel-progress-fill")+80]
	empty_content = content[
		content.find("track-panel-progress-empty")+41:
		content.find("track-panel-progress-empty")+80]

	fill_time = fill_content[fill_content.find(">")+1:fill_content.find("<")]
	empty_time = empty_content[fill_content.find(">")+2:empty_content.find("<")]
	display_time(str(fill_time), str(empty_time))

	fill_count = int(fill_content[:fill_content.find("%")])
	empty_count = int(empty_content[:empty_content.find("%")])
	display_graph(fill_count, empty_count)

	# print(content)

if __name__ == "__main__":
    main()
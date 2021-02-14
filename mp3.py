
from selenium import webdriver
import argparse
import json
import re
import time
import os


# ------------------------------------------------------------------------------------------
# GLOBAL VARS
# ------------------------------------------------------------------------------------------


JS_GET_YOUTUBE_DATA_VARIABLE = 'return window["ytInitialData"]'

URL_YOUTUBE_BASE = 'https://www.youtube.com'
URL_PLAYLISTS_ROOT = "/playlists"
URL_VIDEOS_ROOT = "/videos"

PLAYLIST_VALUES_KEY = 'playlistId'
PLAYLIST_URL_PARAMETER = '/playlist?list='
VIDEO_VALUES_KEY = 'videoId'
VIDEO_URL_PARAMETER = '/watch?v='

VIEW_TYPE_PLAYLISTS = "VIEW_TYPE_PLAYLISTS"
VIEW_TYPE_VIDEOS = "VIEW_TYPE_VIDEOS"

url_youtube_channel = ''
collected_ids = []
args = None
browser = None


# ------------------------------------------------------------------------------------------
#  GENERAL HELPER FUNCTIONS
# ------------------------------------------------------------------------------------------


def setup_arguments():
	global args
	parser = argparse.ArgumentParser()
	parser.add_argument('url', type=str)
	args = parser.parse_args()


def remove_duplicates_from_list(param_values):
	output = []
	seen = set()
	for value in param_values:
		# If value has not been encountered yet add it to both list and set.
		if value not in seen:
			output.append(value)
			seen.add(value)
	return output


def find_values_in_json(param_value_id, param_json_repr):
	results = []

	def _decode_dict(a_dict):
		try:
			results.append(a_dict[param_value_id])
		except KeyError:
			pass
		return a_dict
	json.loads(param_json_repr, object_hook=_decode_dict)  # Return value ignored.
	return results


def save_urls_to_file():
	print("Saving URLs to file.")
	with open('urls.txt', 'w') as f:
		for item in collected_ids:
			f.write("%s\n" % item)


# ------------------------------------------------------------------------------------------
# BROWSER
# ------------------------------------------------------------------------------------------


def initiate_browser():
	print("Initiating browser.")
	global browser

	# Change this to use a different browser.
	# Don't forget to get the right webdriver to go along with it.
	browser = webdriver.Firefox()

	if browser:
		# Change this to the biggest size you can get away with for less scrolling.
		browser.set_window_size(1024, 10000)
		print("Browser active.")


def scroll_down_to_load_additional_content():
	# Youtube only loads additional videos/playlists once you've scrolled to the bottom of the page.
	# That's what we're doing in the following function.

	print("Scroll to load additional content.")

	js_get_page_height = ("return Math.max(document.body.scrollHeight," +
												"document.body.offsetHeight," +
												"document.documentElement.clientHeight," +
												"document.documentElement.scrollHeight," +
												"document.documentElement.offsetHeight );")

	# I didn't bother looking for a clean way to determine when youtube
	# has finished pulling new content, so I just wait 4 seconds. Seems to work fine so far.
	scroll_pause_time = 4

	current_page_height = browser.execute_script(js_get_page_height)

	while True:
		browser.execute_script("window.scrollTo(0,"+str(current_page_height)+");")
		time.sleep(scroll_pause_time)
		new_page_height = browser.execute_script(js_get_page_height)
		if new_page_height == current_page_height:
			break
		current_page_height = new_page_height


def close_browser():
	print("Closing browser.")
	browser.quit()


# ------------------------------------------------------------------------------------------
# SCRAPING
# ------------------------------------------------------------------------------------------


def open_tab(param_root):
	print("\nOpen tab: "+param_root)
	print('Waiting for page to be fully loaded.')

	final_url = URL_YOUTUBE_BASE + url_youtube_channel + param_root
	browser.get(final_url)

	data = browser.execute_script(JS_GET_YOUTUBE_DATA_VARIABLE)
	all_urls_temp = find_values_in_json('url', json.dumps(data))
	views = []
	for url in all_urls_temp:
		if "view=" in url:
			view_id = re.search("(?<=view=)(\d+)", url).group(0)
			views.append(url_youtube_channel+param_root+'?view='+view_id+'&flow=grid')
	views = remove_duplicates_from_list(views)
	return views


def parse_views(param_view_url_list, param_view_type):
	for view in param_view_url_list:
		open_view(view, param_view_type)


def open_view(param_view_url_list, param_view_type):
	global collected_ids

	url_parameter = ""
	find_values_key = ""

	if param_view_type == VIEW_TYPE_PLAYLISTS:
		find_values_key = PLAYLIST_VALUES_KEY
		url_parameter = PLAYLIST_URL_PARAMETER
	elif param_view_type == VIEW_TYPE_VIDEOS:
		find_values_key = VIDEO_VALUES_KEY
		url_parameter = VIDEO_URL_PARAMETER

	url = URL_YOUTUBE_BASE+param_view_url_list
	print("Opening view: "+url)
	browser.get(url)

	scroll_down_to_load_additional_content()

	data = browser.execute_script(JS_GET_YOUTUBE_DATA_VARIABLE)
	all_ids = find_values_in_json(find_values_key, json.dumps(data))
	all_ids = remove_duplicates_from_list(all_ids)

	for found_id in all_ids:
		collected_ids.append(URL_YOUTUBE_BASE + url_parameter + found_id)


def clean_channel_url():
	global url_youtube_channel
	url_youtube_channel = re.search('/(user|channel)/[^/]*', args.url).group(0)


def para_youtube_dl():
	print("Run youtube-dl.")
	os.system('parallel -j0 youtube-dl -f m4a $(youtube-dl --get-url) :::: urls.txt')

def mp3():
	print("Run m4a to mp3.")
	os.system('find -name "*.m4a" | parallel ffmpeg -i {} -acodec libmp3lame {.}.mp3')

def rm():
	print("remove m4a")
	os.system('rm *.m4a & rm *.txt')
	
def move():
	os.system('mv *.mp3 mp3')

# ------------------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------------------


if __name__ == "__main__":
	setup_arguments()
	clean_channel_url()
	initiate_browser()

	# Collect URLs from the videos tab.
	parse_views(open_tab(URL_VIDEOS_ROOT), VIEW_TYPE_VIDEOS)

	# Collect URLs from the playlists tab.
	parse_views(open_tab(URL_PLAYLISTS_ROOT), VIEW_TYPE_PLAYLISTS)

	# The browser is no longer needed now.
	close_browser()

	collected_ids = remove_duplicates_from_list(collected_ids)

	print("\n" + str(len(collected_ids)) + " URLs collected:\n" + str(collected_ids) + '\n')

	save_urls_to_file()

	para_youtube_dl()
	
	mp3()
	
	rm()
	
	move()



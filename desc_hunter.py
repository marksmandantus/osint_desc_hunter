import requests    
import re

channel_id = input("Enter channel id: ")
url_part_1 = "https://youtube.googleapis.com/youtube/v3/search?part=snippet&channelId="
url_part_2 = "&maxResults=50&key=AIzaSyD6xmCCs6zcZlQSILK1MN9oTsnGLIJ8mC8&alt=json"
next_page_token = ""

unparsing_url = url_part_1 + channel_id + url_part_2

res = requests.get(unparsing_url)
data = res.json()

links = []
for item in data["items"]:
    video_desc = item["snippet"]["description"]
    links += re.findall(r'(https?://[-\w./:]+)', video_desc)
    if "nextPageToken" in data:
        next_page_token = data["nextPageToken"]
    else:
        break
    
for i, link in enumerate(links):
    print(f"{i+1}. {link}")
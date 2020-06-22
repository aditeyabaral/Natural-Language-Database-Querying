import csv
import os

import videoLookup

root_path = os.path.join(os.path.dirname(os.getcwd()), "Database", "Video")
video_list = os.listdir(root_path)
with open("videoTags.csv", "w") as tags_file:
    writer = csv.writer(tags_file)
    for idx, path in enumerate(video_list):
        # path = "vid1.mp4"
        tags = videoLookup.getFilteredTags(path)
        print(tags)
        writer.writerow([path] + tags)
        if idx == 1:
            break

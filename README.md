# trawl-SAD

This was initally a method of extracting data from Subtle Asian Dating to later perform data analysis.

FB_trawl.py extracts the links for individual posts and stores them in links.txt.
parse_data.py takes each individual links, stores the post's data in a txt file labeled with the timestamp of the post. It also stores the number of pictures, number of comments, and number of likes as values in a dictionary with the timestamp as the key. The dictionary is stored in output_dict.csv.

However, this program is extendable for extracting data from posts in other Facebook groups.

Uses Selenium and Python.

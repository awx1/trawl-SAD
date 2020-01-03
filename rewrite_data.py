with open('rewrite_links.txt', 'w') as links:
	with open('links.txt', 'r') as f:
		for url in f:
			if len(url) == 76:
				links.write("%s" % url)
f.close()
links.close()
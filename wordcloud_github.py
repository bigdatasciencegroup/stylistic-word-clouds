import numpy as np
import csv
import random
from PIL import Image
from wordcloud import WordCloud, STOPWORDS

def grey_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(10, 50)

csv_path = "github_words.csv"
fa_path = "/Users/maxwoolf/Downloads/exported2048/"
font_path = "/Users/maxwoolf/Fonts/mplus-1m-regular.ttf"

icon = "github"

words_array = []
with open(csv_path, 'rb') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['word'] not in STOPWORDS:
			words_array.append((row['word'].upper(), float(row['num_words'])))

# http://stackoverflow.com/questions/7911451/pil-convert-png-or-gif-with-transparency-to-jpg-without
icon_path = fa_path + "%s.png" % icon
icon = Image.open(icon_path)
mask = Image.new("RGB", icon.size, (255,255,255))
mask.paste(icon,icon)
mask = np.array(mask)

wc = WordCloud(font_path=font_path, background_color="white", max_words=2000, mask=mask,
               max_font_size=300)
               
# generate word cloud
wc.generate_from_frequencies(words_array)
wc.recolor(color_func=grey_color_func)
wc.to_file("github_wordcloud.png")
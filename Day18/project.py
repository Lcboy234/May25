###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

list = []

colors = colorgram.extract('image.jpg', 30)

for every_single_color in colors:
    list.append(every_single_color.rgb)

print(list)
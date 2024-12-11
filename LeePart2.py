# I used this matplot guide to make the grouped column chart for this data
# The link to the code is here: https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html

import re
import matplotlib.pyplot as plt
import numpy as np

# returns letter based on number entered
def getSide(num: int):
    if num == 0:
        return 'A'
    elif num == 1:
        return 'B'
    else:
        return 'C'

def main():
    # open xml file with save data
    xml = open('main.xml', 'r')
    text = xml.readlines()
    xml.close()

    chapters = []
    # each subgroup is the key in the dictionary, and each chapter will have 1 entry in the array per key
    # this part is based on the matplot reference listed at the top
    deaths = {'A': [], 'B': [], 'C': []}

    side = 0

    for line in text:
        if '<AreaStats ID=' in line: # tag at the start of a chapter
            pat = re.compile('<AreaStats ID="\\d*" Cassette=".*" SID="Celeste/(\\d*-)*(.*)">')
            match = pat.findall(line)[0]

            chapName = match[1]

            # use regex to find the start of each word (2 words max)
            pat = re.compile('([A-Z][a-z]*)([A-Z][a-z]*)*')
            match = pat.findall(chapName)[0]

            # if there's two words, add a space, else just use the first word
            if match[1] != '':
                chapters.append(match[0] + ' ' + match[1])
            else:
                chapters.append(match[0])            

        # start of sub-chapter stats
        if '<AreaModeStats' in line:
            # regex for sub-chapter tag and attributes
            pat = re.compile('Deaths="(\\d+)"')
            match = pat.findall(line)[0]
            deaths[getSide(side)].append(int(match))

            if side != 2:
                side += 1
            else: # if we reach c side, return to a side for next chapter
                side = 0

    # Below this point more heavily references the matplot bar chart guide linked here https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html


    x = np.arange(len(chapters))  # set the label locations based on num of chapters
    width = 0.25  # the width had to be .25 otherwise it broke?
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained', figsize=(14,6))

    # changing the colors to match celeste theming! for extra fun
    colors = ['royalblue', 'mediumvioletred', 'gold']
    colorIndex = 0

    for side, deaths in deaths.items():
        offset = width * multiplier
        # variable to add color found on matplot site https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_colors.html
        rects = ax.bar(x + offset, deaths, width, label=side, color=colors[colorIndex])
        ax.bar_label(rects, padding=3)
        multiplier += 1
        
        # advance color by one for each column added
        if colorIndex < 3:
            colorIndex += 1
        else: # once last color reached, return to first
            colorIndex = 0
        
    # Labels! Title! Legend!
    ax.set_ylabel('# of Deaths')
    ax.set_title('Lee\'s Number of Deaths Per Celeste Chapter')
    ax.set_xticks(x + width, chapters)
    ax.legend(loc='upper left', ncols=3)

    # show matplot
    plt.show()

main()
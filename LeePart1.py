import re 

# open xml file with save data
xml = open('main.xml', 'r')
text = xml.readlines()
xml.close()

# open html for output
html = open('celeste.html', 'w')
# html header with css style sheet linked
html.write('<html>\n<head>\n<link rel="stylesheet" href="style.css">\n</head>\n<body>\n<h1>Lee\'s Celeste History!</h1>\n')

# celeste has three game "sides," which determine the difficulty of the level
# this is a counter so I can write which side is being outputed
side = 0

for line in text:
    if '<AreaStats ID=' in line: # tag at the start of a chapter
        pat = re.compile('<AreaStats ID="(\\d*)" Cassette="(.*)" SID="Celeste/(\\d*-)*(.*)">')
        match = pat.findall(line)[0]

        # pull out info from matched regex
        chapNum = match[0]
        hasCass = match[1]
        chapName = match[3]

        # change bool to text
        if hasCass:
            hasCass = 'Yes!'
        else:
            hasCass = 'No...'

        # use regex to find the start of each word (2 words max)
        pat = re.compile('([A-Z][a-z]*)([A-Z][a-z]*)*')
        match = pat.findall(chapName)[0]

        # if there's two words, add a space, else just use the first word
        if match[1] != '':
            chapName = match[0] + ' ' + match[1]
        else:
            chapName = match[0]      

        # write header for each chapter
        html.write(f'<div>\n<h2>Chapter {chapNum}: {chapName}</h2>\n')
        if chapNum == '8':
            # comment since no stats will be output later
            html.write('This chapter has no gameplay!\n')

    # start of sub-chapter stats
    if '<AreaModeStats' in line:
        # regex for sub-chapter tag and attributes
        pat = re.compile('TotalStrawberries="(\\d*)" Completed=".*" SingleRunCompleted=".*" FullClear=".*" Deaths="(\\d*)" TimePlayed="(\\d*)"')
        match = pat.findall(line)[0]

        strawberries = match[0]
        deaths = match[1]
        playTime = match[2]

        # if play time is 0, then there is either no gameplay or no b/c sides, so it is skipped
        if int(playTime) != 0: 
            # save data writes time in .1 milliseconds, so I'm converting to seconds
            playMin = int(playTime) / 10000000
            totalMin = round(playMin // 60)
            totalSec = round(playMin % 60)

            # write a/b/c side subheaders
            if side == 0:
                html.write(f'<h3 class="a">A-Side</h3>\n')
            elif side == 1:
                html.write(f'<h3 class="b">B-Side</h3>\n')
            else:
                html.write(f'<h3 class="c">C-Side</h3>\n')
            
            # write stats to html
            html.write(f'<ul>\n<li>Got Cassette? {hasCass}</li>\n<li># of Strawberries Collected: {strawberries}</li>\n<li># of Deaths: {deaths}</li>\n<li>Total Play Time: {totalMin} minutes, {totalSec} seconds</li>\n</ul>\n')

            
            if side != 2:
                side += 1
            else: # if we reach c side, return to a side for next chapter
                side = 0
                html.write('</div>\n')

        else: # skip to a side since there is no b/c
            side = 0
            html.write('</div>\n')

# closing tags
html.write('</body>\n</html>')
html.close()
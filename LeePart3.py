import re
import time

def main():
    # open xml file with save data
    xml = open('main.xml', 'r')
    text = xml.readlines()
    xml.close()

    # lists to store chapter names and strawberry counts
    chapters = []
    strawberries = []

    side = 0

    # iterate through the lines to find number of strawberries
    for line in text:
        if '<AreaStats ID=' in line: # tag at the start of a chapter
            pat = re.compile('<AreaStats ID="(\\d*)" Cassette="(.*)" SID="Celeste/(\\d*-)*(.*)">')
            match = pat.findall(line)[0]

            chapName = match[3]

            # use regex to find the start of each word (2 words max)
            pat = re.compile('([A-Z][a-z]*)([A-Z][a-z]*)*')
            match = pat.findall(chapName)[0]

            # if there's two words, add a space, else just use the first word
            if match[1] != '':
                chapName = match[0] + ' ' + match[1]
            else:
                chapName = match[0]    

            # add an item for each section of the chapter
            chapters.append(chapName + ' A')
            chapters.append(chapName + ' B')
            chapters.append(chapName + ' C')

        # start of sub-chapter stats
        if '<AreaModeStats' in line:
            # regex for sub-chapter tag and attributes
            pat = re.compile('TotalStrawberries="(\\d*)"')
            match = pat.findall(line)[0]

            strawberry = match
            strawberries.append(int(strawberry)) # append as an int
        
            if side != 2:
                side += 1
            else: # if we reach c side, return to a side for next chapter
                side = 0

    # Celeste game stats obtained from the game itself and the Celeste wiki https://celestegame.fandom.com/wiki/Collectibles
    totalStrawberries = 202
    totalStrawByChap = [0, 0, 0, 20, 0, 0, 18, 0, 0, 25, 0, 0, 29, 0, 0, 31, 0, 0, 0, 0, 0, 47, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0]

    print('Welcome to Lee\'s Celeste Gameplay Analysis!')
    time.sleep(1.5)
    print(f'In Celeste, there are {totalStrawberries} total collectable strawberries across all of the chapters of the game.')
    time.sleep(1.5)
    print(f'In the A-sides, there are {sum(totalStrawByChap)} strawberries.')
    time.sleep(1.5)
    print(f'Additionally, every chapter has a Golden Strawberry, which can be collected by completing the chapter without dying.')
    time.sleep(1.5)
    print(f'I have collected all of the standard berries, as seen below:\n')
    time.sleep(1.5)

    # iterate by 3 to skip b/c sides since they have no normal berries
    for i in range(0, len(totalStrawByChap), 3):
        straw = strawberries[i]

        if strawberries[i] >= totalStrawByChap[i]: # if the berries I have is > total, that means I have a golden berry, which I'm not talking about now
            straw = totalStrawByChap[i]

        print(f'{chapters[i]}: {straw}/{totalStrawByChap[i]}')

    time.sleep(3)
    print('\nAdditionally, I\'ve collected a few Golden berries.\n')
    time.sleep(1.5)

    chapterGolden = {}
    goldenStraw = 0

    for i, value in enumerate(totalStrawByChap):
        # subtract number of strawberries collected from total to find bonus golden berries        
        straw = strawberries[i] - totalStrawByChap[i]
        
        print(f'{chapters[i]}: {straw}/1')

        # seperate a/b/c from chapter name
        chapName = chapters[i].split(' ')
        chapName.pop()
        chapName = ' '.join(chapName)

        # add golden berries to dictionary
        chapterGolden[chapName] = chapterGolden.get(chapName, 0) + straw
        # add to total golden berries
        goldenStraw += straw

    # key with max value code references from here: https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
    # I couldn't figure out how to get the key, only the value before this
    time.sleep(5)
    print(f'\nI have a total of {goldenStraw} Golden Strawberries. I have the most Golden Strawberries in {max(chapterGolden, key=chapterGolden.get)} ({max(chapterGolden.values())} Strawberries).')
    time.sleep(1.5)
    print(f'\nIn total, I have collected {sum(strawberries)}/{totalStrawberries} strawberries in the game Celeste!')

main()
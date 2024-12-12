# Interoperability Final Project

For this project, I chose to analyze my save data from the video game [Celeste](https://www.celestegame.com). This project is split into 3 parts.

### Part 1: [Converting XML to HTML](LeePart1.py)
Taking my first Celeste save data file, which was stored in XML, I pulled out relevant data using regular expressions, and outputted the data into an HTML file. I styled this data using a CSS file, to make the website a little more interesting to look at. The site includes some of the basic game stats from my save, including how many strawberries I got in the chapter, if I got the cassette collectable, and the total time I spent playing the chapter.

### Part 2: [Creating a Matplotlib Grouped Bar Chart](LeePart2.py)
Using the number of deaths per chapter, I used a grouped bar chart to display the information in an easy-to-understand format. Each chapter has an A, B, and C-side, which increase the difficulty of the chapter. B-sides are the longest, which contributes to the number of deaths in the chapter. C-sides are the most difficult, but only consist of 3 rooms each. I color-coded the groups, to make them fit the CSS theming from Part 1, and displayed the number of deaths above each bar.

### Part 3: [Commond Line Analysis of Strawberries](LeePart3.py)
I then looked at the number of strawberries I got based on chapter. A-sides contain most of the strawberries in the game, but each in chapter and side you can earn a Golden Strawberry by completing the chapter deathless. Using regex to get all of the strawberry stats, I printed out the interesting information in the command line, and commented on my best and worst chapters.

This project was completed for CS 214: Data Interoperability

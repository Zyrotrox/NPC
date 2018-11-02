import xml.etree.ElementTree as Et
import customParseLib as Pars

#the final script which the javaapp executes

#toDo: CNN, Kotaku, Guardian

articleNumber = 20

tree = Et.parse('G:\gitnpc\src\InfoGathering\pythonParsing\ArticleSources.xml')
root = tree.getroot()

testList = ['BuzzFeedNews', 'WallStreetJournal', 'Polygon', 'HuffingtonPost', 'DailyBeast']

articleFile = open('./Articles.csv', 'w')


for child in root:
    if child.attrib['Name'] in testList:   #to just test specific newssites
        paper = Pars.createPaper(child, articleNumber)
        for data in paper.articles:
            articleFile.write(child.attrib['Name'] + "," + data.replace("\n", '') + "," + paper.articles[data] + "\n")


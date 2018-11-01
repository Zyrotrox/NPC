import xml.etree.ElementTree as Et
import customParseLib as Pars

#the final script which the javaapp executes

articleNumber = 3

tree = Et.parse('ArticleSources.xml')
root = tree.getroot()

articleFile = open('./Articles.csv', 'w')

for child in root:
    print("fuckthis")

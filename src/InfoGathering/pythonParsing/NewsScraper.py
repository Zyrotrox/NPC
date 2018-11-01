import xml.etree.ElementTree as Et
import customParseLib as Pars

articleNumber = 3

tree = Et.parse('ArticleSources.xml')
root = tree.getroot()

articleFile = open('./Articles.csv', 'w')

for child in root:
    print("fuckthis")

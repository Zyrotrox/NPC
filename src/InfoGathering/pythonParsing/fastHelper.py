import xml.etree.ElementTree as Et
import customParseLib as Pars
articleNumber = 3

tree = Et.parse('ArticleSources.xml')
root = tree.getroot()

articleFile = open('./dict.txt', 'w')

for child in root:
    articleFile.write("def " + child.attrib['Name'] + "(self):\n\n\treturn self\n\n")


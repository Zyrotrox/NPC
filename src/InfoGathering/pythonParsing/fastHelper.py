import xml.etree.ElementTree as Et
import customParseLib as Pars
articleNumber = 3

#i made myself a new branch btw. so i dont fuck up anything ^^


#to write functionbodies for copy-pasting

tree = Et.parse('ArticleSources.xml')
root = tree.getroot()

articleFile = open('./dict.txt', 'w')

for child in root:
    articleFile.write("def " + child.attrib['Name'] + "(self):\n\n\treturn self\n\n")


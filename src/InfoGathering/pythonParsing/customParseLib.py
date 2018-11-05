
import xml.etree.ElementTree as Et
from bs4 import BeautifulSoup
import requests


#the library that should do all the work


def createPaper(xmlnode,articleNumber):

    paper = Paper(xmlnode.attrib['Name'], xmlnode.attrib['url'])
    switcher = {
        'BuzzFeedNews': paper.BuzzFeedNews(articleNumber),
        'WallStreetJournal': paper.WallStreetJournal(articleNumber),
        'Kotaku': paper.Kotaku(articleNumber),
        'Polygon': paper.Polygon(articleNumber),
        'CNN': paper.CNN(articleNumber),
        'HuffingtonPost': paper.HuffingtonPost(articleNumber),
        'DailyBeast': paper.DailyBeast(articleNumber),
        'TheGuardian': paper.TheGuardian(articleNumber),
        'TheWashingtonPost': paper.TheWashingtonPost(articleNumber),
        'NPR': paper.NPR(articleNumber),
        'Vox': paper.Vox(articleNumber),
        'BlackLivesMatter': paper.BlackLivesMatter(articleNumber),
        'BBC': paper.BBC(articleNumber),
        'NewYorkTimes': paper.NewYorkTimes(articleNumber),
        'MSNBC': paper.MSNBC(articleNumber),
        'TheDailyDot': paper.TheDailyDot(articleNumber),
        'Salon': paper.Salon(articleNumber),
        'MotherJones': paper.MotherJones(articleNumber),
        'Vice': paper.Vice(articleNumber),
        'ABC': paper.ABC(articleNumber)
    }

    return switcher[xmlnode.attrib['Name']]


class Paper:

    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.articles = {}

    def BuzzFeedNews(self, artno):
        if self.name != 'BuzzFeedNews':
            return None
        soup = getSoup(self)

        articles = soup.find_all('article')
        j = 0
        while j < artno:
            self.articles[articles[j].h2.a.string] = articles[j].a['href']
            j += 1

        return self

    def WallStreetJournal(self, artno):

        if self.name != 'WallStreetJournal':
            return None

        soup = getSoup(self)

        articles = soup.find_all('h3')

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].a.string] = articles[j].a['href']
            j += 1

        return self

    def Kotaku(self, artno):

        #if self.name != 'Kotaku':
        #    return None

        #soup = getSoup(self)

        #articles = soup.find_all('article')

        #j = 0
        #while j < artno and j < len(articles):
        #   self.articles[articles[j].a.string] = articles[j].a['href']
        #    j += 1

        # fuck kotaku for now

        return None

    def Polygon(self, artno):

        if self.name != 'Polygon':
            return None

        soup = getSoup(self)

        articles = soup.find_all('div', 'c-compact-river__entry')

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].h2.a.string] = articles[j].h2.a['href']
            j += 1

        return self

    def CNN(self, artno):


        #not working rn. but not far off i guess.


        if self.name != 'CNN':
            return None

        soup = getSoup(self)

        articles = soup.find_all('div')

        print(len(articles))

        j = 0
        while j < artno and j < len(articles):
            print(articles[j])

            j += 1

        return self

    def HuffingtonPost(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        soup = getSoup(self)

        articles = soup.find_all('div', 'card__headline')

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].a.div.string] = ("https://www.huffingtonpost.com" + articles[j].a['href'])
            j += 1

        return self

    def DailyBeast(self, artno):

        if self.name != 'DailyBeast':
            return None

        soup = getSoup(self)

        articles = soup.find_all('article', 'LatestCard')


        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].h2.string] = articles[j].a['href']
            j += 1

        return self

    def TheGuardian(self, artno):

        #should work but i can't test it on the uni servers :/

        if self.name != 'TheGuardian':
            return None

        soup = getSoup(self)

        articles = soup.select(".fc-item__title")

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].a.select(".js-headline-text").string] = articles[j].a['href']
            j += 1

        return self

    def TheWashingtonPost(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def NPR(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def Vox(self, artno):

        #same thing as guardian. stupid uni

        if self.name != 'Vox':
            return None

        soup = getSoup(self)

        articles = soup.find_all("div", "c-compact-river__entry")

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].h2.a.string] = articles[j].h2.a['href']
            j += 1

        return self

    def BlackLivesMatter(self, artno):

        #can't test this  :/

        if self.name != 'BlackLivesMatter':
            return None

        soup = getSoup(self)

        articles = soup.find_all("div", "col-sm-4")

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].h3.a.string] = articles[j].h3.a['href']
            j += 1

        return self

    def BBC(self, artno):

        #still at uni :/ btw, why the fuck do i feel the need to comment this shit
        #i literally have not a single useful comment in this code -.-

        if self.name != 'BBC':
            return None

        soup = getSoup(self)

        articles = soup.find_all("h3")

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].string] = articles[j].parent['href']
            j += 1

        return self

    def NewYorkTimes(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def MSNBC(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def TheDailyDot(self, artno):

        #these comments get kinda boring now

        if self.name != 'TheDailyDot':
            return None

        soup = getSoup(self)

        articles = soup.find_all("a", "dd-card-headline")

        j = 0
        while j < artno and j < len(articles):
            self.articles[articles[j].string] = articles[j]['href']
            j += 1

        return self

    def Salon(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def MotherJones(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def Vice(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self

    def ABC(self, artno):

        if self.name != 'HuffingtonPost':
            return None

        return self


def getSoup(paper):
    resp = requests.get(paper.url)
    html = resp.text
    soup = liquify(html);
    return soup

def liquify(html):
	return BeautifulSoup(html,'lxml') #this function is completly useless but i like this name better xD

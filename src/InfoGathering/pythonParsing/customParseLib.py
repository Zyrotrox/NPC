
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
        print('startet the shit')
        resp = requests.get(self.url)
        html = resp.text
        soup = BeautifulSoup(html, 'lxml')

        articles = soup.find_all('article')
        j = 0
        while j < artno:
            self.articles[articles[j].h2.a.string] = articles[j].a['href']
            j += 1

        return self

    def WallStreetJournal(self, artno):
        return self

    def Kotaku(self, artno):
        return self

    def Polygon(self, artno):
        return self

    def CNN(self, artno):
        return self

    def HuffingtonPost(self, artno):
        return self

    def DailyBeast(self, artno):
        return self

    def TheGuardian(self, artno):
        return self

    def TheWashingtonPost(self, artno):
        return self

    def NPR(self, artno):
        return self

    def Vox(self, artno):
        return self

    def BlackLivesMatter(self, artno):
        return self

    def BBC(self, artno):
        return self

    def NewYorkTimes(self, artno):
        return self

    def MSNBC(self, artno):
        return self

    def TheDailyDot(self, artno):
        return self

    def Salon(self, artno):
        return self

    def MotherJones(self, artno):
        return self

    def Vice(self, artno):
        return self

    def ABC(self, artno):
        return self



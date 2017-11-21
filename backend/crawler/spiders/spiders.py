import scrapy
import networkx as networkx
from networkx.readwrite import json_graph

class ArticleSpider(scrapy.Spider):
    name = "articles"

    def start_requests(self):
        urls = ["https://www.usatoday.com/picture-gallery/news/nation-now/2017/11/13/fraternity-hazing-deaths-2017/107665120/",
            "http://www.fark.com/comments/9801717/Nuke-Penn-State-From-Orbit-Fraternity-Hazing-Edition",
            "https://www.nbcnews.com/storyline/hazing-in-america/penn-state-fraternity-suspended-after-student-hospitalized-n807546",
            "http://www.startribune.com/penn-state-fraternity-faces-underage-drinking-charges/451237293/",
            "https://www.yahoo.com/news/another-12-students-charged-death-192021844.html",
            "http://www.ktvb.com/news/nation-world/more-charges-in-penn-state-hazing-death/491468071",
            "http://www.king5.com/news/nation-world/more-charges-in-penn-state-hazing-death/491468045",
            "http://abcnews.go.com/US/oath-silence-secret-world-fraternity-pledging-contributes-hazing/story?id=49877076",
            "http://www.khou.com/news/nation-world/more-charges-in-penn-state-hazing-death/491467696",
            "http://www.apnewsarchive.com/2017/Penn-State-says-it-has-meted-out-discipline-in-connection-with-the-death-of-a-fraternity-pledg",
            "http://www.startribune.com/penn-state-says-it-punished-7-in-penn-state-frat-death/455917033/",
            "http://www.philly.com/philly/education/penn-state-frat-charges-refiled-piazza-death-20171027.html",
            "https://www.businessinsider.com/interfraternity-ceo-doesnt-know-scope-of-hazing-2017-10",
            "https://finance.yahoo.com/news/charges-filed-horrifying-apos-gauntlet-190834073.html",
            "http://www.mycentraljersey.com/story/news/crime/2017/11/13/more-charges-piazza-hazing-death-penn-state-fraternity/858797001/",
            "http://www.dailymail.co.uk/wires/ap/article-5078871/The-Latest-Parents-condemn-Penn-State-frat-sons-death.html",
            "http://www.apnewsarchive.com/2017/A-fraternity-at-Pennsylvania-State-University-is-facing-charges-of-furnishing-liquor-to-minors",
            "http://www.charlotteobserver.com/news/article179237696.html",
            "http://www.newsobserver.com/news/article179237696.html",
            "https://www.seattletimes.com/nation-world/penn-state-fraternity-faces-underage-drinking-charges/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        body = response.css('body')
        paragraphs = body.css('p.story-body-text a::attr(href)')
        links = paragraphs.extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse)

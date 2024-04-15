import pprint
import requests
from bs4 import BeautifulSoup

url = f"https://news.ycombinator.com/"
res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")
stories = soup.select(".titleline")
subtext = soup.select(".subtext")


def sort_stories_by_votes(stories):
    # for story in stories:
    return sorted(stories, key=lambda k: k["votes"], reverse=True)


def filter_hn_posts(stories, subtext):
    hn_posts = []
    for idx, story in enumerate(stories):
        story_title = story.a.get_text()
        story_link = story.a.get("href", None)
        vote = subtext[idx].select(".score")
        if len(vote):
            points = int(vote[0].get_text().replace(" points", ""))
        if points > 99:
            hn_posts.append({"title": story_title, "link": story_link, "votes": points})
    return sort_stories_by_votes(hn_posts)


pprint.pprint(filter_hn_posts(stories, subtext))

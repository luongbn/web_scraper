from bs4 import BeautifulSoup
import requests
# import lxml

URL = "https://web.archive.org/web/20200518055830/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
ranking = []

films = soup.select(selector=".title")

# Option 1
for film in films[10::]:
    ranking.append(film.getText())

r_ranking = ranking
print(ranking[::-1])

# Option 2
movie_titles = [movie.getText() for movie in films[10::]]
ordered_movie_titles = movie_titles[::-1]
print(ordered_movie_titles)

# Write to file
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in ordered_movie_titles:
        file.write(f"{movie}\n")

# Learning Stuff
# response = requests.get("https://news.ycombinator.com/news")
# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, "html.parser")
#
# article_texts = []
# article_links = []

## find
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.getText()
# # article_link = article_tag.find(name="a").get("href")
# article_link = article_tag.select_one(selector="a").get("href")
# article_upvote = soup.find(name="span", class_="score").getText()
# # article_upvote = soup.select(selector="#score_34802858")[0].text
#
# print(article_tag)
# print(article_text)
# print(article_link)
# print(article_upvote)

##find all
# article_tag_all = soup.find_all(name="span", class_="titleline")
#
# for article in article_tag_all:
#     text = article.getText()
#     article_texts.append(text)
#     link = article.select_one(selector="a").get("href")
#     article_links.append(link)
#
# article_upvotes = [int(upvote.getText().split()[0]) for upvote in soup.find_all(name="span", class_="score")]
#
# print(article_texts)
# print(article_links)
# print(article_upvotes)
#
# max_value = max(article_upvotes)
# index = article_upvotes.index(max_value)
# print(index)
# print(article_texts[index])
# print(article_links[index])
# print(max_value)

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # soup = BeautifulSoup(contents, "lmxl")
# # print(soup.title)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
#
# # find all
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
# # find all alternative
# all_anchor_tags = soup.select_one(selector="a")
# print(all_anchor_tags)
# print(all_anchor_tags.get("href"))

#
# # find by attribute with id
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# # find by attribute with class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
# print(section_heading.string)
#
# # get first matching item by selector/nested tags
# company_url = soup.select_one(selector="p a")
# # print(company_url)
#
# # find by id
# name = soup.select_one(selector="#name")
# # print(name)
#
# # find by class
# headings = soup.select(".heading")
# # print(headings)
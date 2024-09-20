from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# article_tag = soup.find(name="span", class_="titleline")
# article_text = article_tag.get_text()
# article_link = article_tag.find(name="a").get("href")
# article_point = soup.find(name="span", class_="score")
# print(article_text)
# print(article_link)
# print(article_point.getText())
# to get all the article
articles = soup.find_all(name="span", class_="titleline")
article_text = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_text.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

article_point = [int(score.getText().split()[0]) for score in  soup.find_all(name="span", class_="score")]
# to get the article with the highest points.
max_point = max(article_point)
max_index = article_point.index(max_point)


print(article_text[max_index])
print(article_links[max_index])
print(article_point[max_index])






















# # import lxml
#
# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
# soup = BeautifulSoup (contents, "html.parser")
# all_anchor_tag = soup.find_all(name="a") #to get all the anchor tags or all pragram ...
# for tag in all_anchor_tag:
#     # print(tag.getText())
#     # print(tag.get("href"))              # to get all the links
#     pass
# # we can find my attribute
#
# heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_ = "heading")  # we can't use class here because class is a special
# # word in python
# print(section_heading)
#
# # we can get anchor tag that is inside in anchor tag
#
# company_url = soup.select_one(selector="p a")  # a anchor tag which is inside p anchor tag
# print(company_url)
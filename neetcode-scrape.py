from bs4 import BeautifulSoup
import json
import requests

def getProblemNumber(url):
  html = requests.get(url)
  soup = BeautifulSoup(html.content, "html.parser")
  span = soup.find("span", { "class" : "mr-2 text-lg font-medium text-label-1 dark:text-dark-label-1"})
  return span.text.split(".")[0] if span else "MANUALLY INPUT"

def parseMainHTML():
  with open("./neetcode.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

  lst = [] # [{problem, href, difficulty}, ...]

  for group in soup.find_all("app-pattern-table"):
    category = group.find("button").find("p").text.strip()
    
    for tr in group.find_all("tr", { "class": "ng-star-inserted" }):
      problem = tr.find("a").text.strip()
      link = tr.find("a")["href"]
      difficulty = tr.find("td", { "class": "diff-col" }).find("b").text.strip()

      problemID = getProblemNumber(link)

      lst.append({
        "problem_id": problemID,
        "problem": problem,
        "link": link,
        "difficulty": difficulty,
        "category": category
      })

  f = open("parsed.json", "w")
  f.write(json.dumps(lst))
  f.close()

print("Parsing...")
parseMainHTML()
print("HTML file succesfully parsed.")
from bs4 import BeautifulSoup
import json

with open("./neetcode.html") as fp:
  soup = BeautifulSoup(fp, "html.parser")

lst = [] # [{problem, href, difficulty}, ...]

for group in soup.find_all("app-pattern-table"):
  category = group.find("button").find("p").text.strip()
  
  for tr in group.find_all("tr", { "class": "ng-star-inserted" }):
    problem = tr.find("a").text.strip()
    link = tr.find("a")["href"]
    difficulty = tr.find("td", { "class": "diff-col" }).find("b").text.strip()
    lst.append({
      "problem": problem,
      "link": link,
      "difficulty": difficulty,
      "category": category
    })

f = open("parsed.json", "w")
f.write(json.dumps(lst))
f.close()

print("HTML file succesfully parsed.")
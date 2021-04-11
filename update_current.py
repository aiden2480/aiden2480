import os
import requests

# Read soup
with open("./README.md", encoding="utf-8") as fp:
    rawsoup = fp.read()

# Parse soup
start = "<!--START_SECTION:current-->"
end = "<!--END_SECTION:current-->"
commitmsg = "\N{POT OF FOOD} Updated soup flavour" # No double quotes

soup = rawsoup.split(start, 1)
soup += soup.pop(1).split(end, 1)
assert len(soup) == 3, "This error message is useless. Have some soup \N{POT OF FOOD}"
print("* Soup parsed successfully")

# Download cheese
data = requests.get("https://api.github.com/users/aiden2480/events").json()
commits = [e for e in data if e["type"] == "PushEvent"]
name = commits[0]["repo"]["name"]
cheese = f"[{name.split('/', 1)[1]}](https://github.com/{name})"

# Sprinkle cheese into the soup
spicy = soup[0] + start + cheese + end + soup[2]

if rawsoup == spicy:
    print(f"* These soups are the same flavour! {name} \N{POT OF FOOD}")
    exit(0)

with open("./README.md", "w", encoding="utf-8") as fp:
    spicy = soup[0] + start + cheese + end + soup[2]
    fp.write(spicy)
print("* Cheese merged successfully")

os.system("git add README.md")
os.system(f'git commit -m "{commitmsg}"')
os.system("git push origin main")
print(f"* Soup merged successfully! {name} \N{POT OF FOOD}")

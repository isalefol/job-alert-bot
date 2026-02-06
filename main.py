import json

with open("companies.json", "r", encoding="utf-8") as f:
    companies = json.load(f)

print("Companies loaded:")
for company in companies:
    print("-", company["name"], "|", company["url"])

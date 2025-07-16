import re
text ="The quick brown fox jumps over the lazy dog."

match = re.search("brown",text)
print(match)
if match:
    print("Match found")
    print("Start Index:",match.start())
    print("End Index:",match.end())

# Find all occurences of a pattern

matches = re.findall("the",text, re.IGNORECASE)
print("Matches:",matches)

new_text = re.sub("dog","cat",text)
print("New text:", new_text)

import json

with open('characters.json','r') as f:
    file = json.load(f)

with open('index.html','w') as f:
    f.write('''<style>
    body {
        font-family: Verdana
    }
</style>
''')

for character in file["characters"]:
    info = f'''
<h1>{character['name']}</h1>
<h2>{character['pronunciation']}</h2>
<li>{character['species']}
<li>{character['sex']}
<div>{character['description']}'''
    with open('index.html','a') as f:
        f.write(f'''<ul>{info}</ul>''')

# <h1>First Middle<sup>(optional)</sup> Last</h1>
# <h2>[first]-[middle(optional)]-[last]</h2>
# <li>Species
# <li>Sex
# <div>Description</div>
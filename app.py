import json

with open('characters.json','r') as f:
    file = json.load(f)

style = '''<style>
    body {
        font-size: 2rem;
        font-family: Verdana;
        padding: 2em;
    }
</style>'''
homePage = f'''{style}
'''
for character in file["characters"]:
    languages = []
    nameList = []
    for i in character['description']['languages']:
        languages.append(i)
    spokenLanguages = f''
    index = 0
    for i in languages:
        spokenLanguages += f'''<li>{languages[index]}</li>'''
        if index != len(languages)-1:
            spokenLanguages += '''
                '''
        index += 1
    info = f'''
<a href='../index.html'>
    <== Back</a>
        <h1>{character['full']}</h1>
        <h2>{character['pronunciation']}</h2>
        <ul>
            <li>Species: {character['species']}</li>
            <li>Sex: {character['sex']}</li>
            <li>Job: {character['description']['job']}</li>
            <li>Nationality: {character['description']['nationality']}</li>
            <li>Place of Birth: {character['description']['hometown']}</li>
            <li>Spoken Languages:</li>
            <ul>
                {spokenLanguages}
            </ul>
        </ul>'''
    nameList.append(character['name'])
    with open(f'characters/{character['full'].lower().replace(' ','')}.html','w') as f:
        f.write(f'''{style}
{info}''')
    
    homePage += f'''<li><a href='characters/{character['full'].lower().replace(' ','')}.html'>{character['full']}</a></li>
'''
    with open('index.html','w') as f:
        f.write(homePage)
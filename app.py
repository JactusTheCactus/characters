import json

with open('characters.json','r',encoding='utf-8') as f:
    file = json.load(f)

style = '''<!DOCTYPE html>
<style>
    body {
        font-size: 1.5rem;
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
        spokenLanguages += f'''<li><b>{languages[index]}</b></li>'''
        if index != len(languages)-1:
            spokenLanguages += '''
                '''
        index += 1
    info = f'''
<a href='../index.html'>
    <= Back</a>
        <h1>{character['full']}</h1>
        <h2>{character['pronunciation']}</h2>
        <ul>
            <li>Species: <b>{character['species']}</b></li>
            <li>Sex: <b>{character['sex']}</b></li>
            <li>Job: <b>{character['description']['job']}</b></li>
            <li>Place of Birth: <b>{character['description']['pob']}</b></li>
            <li>Spoken Languages</li>
            <ol>
                {spokenLanguages}
            </ol>
        </ul>
        <p>{character['description']['text']}</p>'''
    nameList.append(character['name'])
    with open(f'characters/{character['full'].lower().replace(' ','-')}.html','w',encoding='utf-8') as f:
        f.write(f'''{style}
{info}''')
    
    homePage += f'''<li><a href='characters/{character['full'].lower().replace(' ','-')}.html'>{character['full']}</a></li>
'''
    with open('index.html','w',encoding='utf-8') as f:
        f.write(homePage)

'''
{
    "name": "",
    "full": "",
    "pronunciation": "",
    "species": "",
    "sex": "",
    "description": {
        "job": "",
        "pob": "",
        "languages": [
            ""
        ],
        "text": ""
    }
}
'''
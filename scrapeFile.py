import re
import requests
import psycopg2


r = requests.get("https://en.wikipedia.org/wiki/Danish_Superliga").content

page_title = re.search(b'(<h1.*?>)(.*?)(</h1>)', r).group(2)

print("Football League: " + page_title.decode('utf-8'))

info_box = re.findall(b'(<tr.*?>)(.*?)(</tr>)', r)
for i in info_box:
    if 'Founded</th>'.encode() in i[1]:
        league_founded = re.search(b'(<td.*?>)(.*?)(</td>)', i[1]).group(2)
        print("League Founded: " + league_founded.decode('utf-8'))
    elif 'Country</th>'.encode() in i[1]:
        country = re.search(b'(<td.*?>)(.*?)(</td>)', i[1]).group(2)
        print("Country: " + country.decode('utf-8'))
    elif 'Number of teams</th>'.encode() in i[1]:
        number_teams = re.search(b'(<td.*?>)(.*?)(</td>)', i[1]).group(2)
        print("Number of teams: " + number_teams.decode('utf-8'))

split_page = r.split(b'Current teams', 1)[1]
teams_table = re.findall(b'(<table.*?>)(.*?)(</table>)', split_page, re.S)[0][1]
teams = re.findall(b'(<td.*?>)(.*?)(</td>)', teams_table, re.S)[::4]
teams_link = [(re.search(b'(<a href=\")(.*?)(\")', x[1]).group(2)).decode('utf-8') for x in teams]
teams_names = [re.sub(b'<.*?>', b'', x[1]).strip() for x in teams]
teams_list = []
for i in teams_names:
    teams_list.append(i.decode('utf-8'))


print("Teams: ")
print('\n'.join(teams_list))
print(teams_link)


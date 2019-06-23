import re
import requests

r = requests.get("https://en.wikipedia.org/wiki/Danish_Superliga").content

page_title = re.search(b'(<h1.*?>)(.*?)(</h1>)', r).group(2)

# infobox = re.findall('(<tr.*?>)(.*?)(</tr>)', r)
# for i in infobox:
#     if 'Founded</th>' in i[1]:
#         founded_eagles = re.search('(<td.*?>)(.*?)(</td>)', i[1]).group(2)
#         print(founded_eagles)
#     elif 'Number of teams</th>' in i[1]:
#         number_teams = re.search('(<td.*?>)(.*?)(</td>)', i[1]).group(2)
#         print(number_teams)

split_shit = r.split(b'Current teams', 1)[1]
teams_table = re.findall(b'(<table.*?>)(.*?)(</table>)', split_shit, re.S)[0][1]
teams = re.findall(b'(<td.*?>)(.*?)(</td>)', teams_table, re.S)[::4]
teams_names = [re.sub(b'<.*?>', b'', x[1]).strip() for x in teams]
print(b'\n'.join(teams_names).decode('utf-8'))





# from urllib.request import urlopen
# html = urlopen("https://ru.wikipedia.org/wiki/Python").read().decode('utf-8')
# s = str(html)
# ans = []
# state = 0
# for c in s:
#     if c == '<':
#         state = 1
#     if c == '>':
#         state = 0
#     elif state == 0:
#         ans.append(c)
# s = ''.join(ans)
# print(s.count('C++'))

# import re
# import requests
# text = requests.get('https://stepik.org/media/attachments/lesson/209719/2.html').text
# pattern = r'<code>(.*?)</code>'
# words = re.findall(pattern, text)
# d = {k: words.count(k) for k in words}
# # d = dict()
# # for k in re.findall(pattern, text):
# #     d[k] = d.get(k, 0) + 1
# s1 = sorted(d.items(), key=lambda x: x[1], reverse=True)
# s2 = sorted(d, key=lambda k: d[k], reverse=True)
# print(*s1)
# print(*s2)
# #v2
# import re
# from urllib.request import urlopen
# from collections import Counter
# html = urlopen('https://stepik.org/media/attachments/lesson/209719/2.html').read().decode('utf-8')
# pattern = r'<code>(.*?)</code>'
# s = sorted(re.findall(pattern, html))
# frequent = Counter(s).most_common(3)
# print(frequent)
# #v3
# import requests
# from bs4 import BeautifulSoup
# from collections import Counter
# r = requests.get("https://stepik.org/media/attachments/lesson/209719/2.html").text
# target = []
# soup = BeautifulSoup(r, features="html.parser")
# for i in soup.find_all('code'):
#     target.append(i.text)
# print(Counter(target))

# from urllib.request import urlopen, urlretrieve
# from bs4 import BeautifulSoup
# resp = urlopen('https://stepik.org/media/attachments/lesson/245130/6.html')
# html = resp.read().decode('utf8')
# soup = BeautifulSoup(html, 'html.parser')
# table = soup.find('table', attrs={'class': 'wikitable sortable'})
# cnt = 0
# for tr in soup.find_all('tr'):
#     cnt += 1
#     for td in tr.find_all(['td', 'th']):
#         cnt *= 2
# print(cnt)

# from bs4 import BeautifulSoup
# import requests
# page = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html')
# soup = BeautifulSoup(page.content, 'html.parser') # HTML.Parser - basic, easy | html5lib - for broken html | lxml - fast
# print(sum([int(i.get_text()) for i in soup.find_all('td')]))
# #v2
# import pandas as pd
# df = pd.read_html('https://stepik.org/media/attachments/lesson/209723/5.html')
# print(df[0].values.sum())


# import xlrd3
# import wget
# url = 'https://stepik.org/media/attachments/lesson/245266/tab.xlsx'
# wget.download(url)
# wb = xlrd3.open_workbook('tab.xlsx')
# sheet_names = wb.sheet_names()
# sh = wb.sheet_by_name(sheet_names[0])
# nmin = sh.row_values(6)[2]
# for rownum in range(7, 27):
#     temp = sh.row_values(rownum)
#     nmin = min(nmin, temp[2])
# print(nmin)
# #v2
# import pandas as pd
# wb = pd.read_excel('https://stepik.org/media/attachments/lesson/245266/tab.xlsx')
# print(min(wb.iloc[6, 2], wb.iloc[7:28, 2].min()))
# print(wb.iloc[6, 2]) # счет строк так же как и в эксель с 1 (с объединенинием)
# print(wb.iloc[7:28, 2]) # столбцы с 0 считаются


# import pandas as pd
# df = pd.read_excel('https://stepik.org/media/attachments/lesson/245267/salaries.xlsx', index_col=0)
# print(df.median(axis=1).idxmax(), df.mean(axis=0).idxmax())


# import pandas as pd
# df = pd.read_excel('https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx')
# df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True]) #сортируем по двум столбцам
# [print(e) for e in df_sorted['Unnamed: 0']]
# print(df_sorted['Unnamed: 0'].to_string(index=False, justify='left')) #justify not working
# #v2
# import pandas as pd
# data = pd.read_excel('https://stepik.org/media/attachments/lesson/245290/trekking1.xlsx')
# print(*data.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])['Unnamed: 0']
#       .to_list(), sep='\n')


# import pandas as pd
# url = 'https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx'
# df1 = pd.read_excel(url, sheet_name='Справочник').fillna(0)
# df2 = pd.read_excel(url, sheet_name='Раскладка').fillna(0)
# unt = pd.merge(df1, df2, left_on='Unnamed: 0', right_on='Продукт')
# # df1.rename(columns={'Unnamed: 0': 'Продукт'}, inplace=True)
# # unt = pd.merge(df2, df1, how='left')
# unt['calories'] = unt['Вес в граммах'] * unt['ККал на 100'] / 100
# unt['proteins'] = unt['Вес в граммах'] * unt['Б на 100'] / 100
# unt['fats'] = unt['Вес в граммах'] * unt['Ж на 100'] / 100
# unt['carbohydrates'] = unt['Вес в граммах'] * unt['У на 100'] / 100
# print(unt.sum()[-4:].astype(int))
# #v2
# df1, df2 = pd.read_excel('https://stepik.org/media/attachments/lesson/245290/trekking2.xlsx',
#                          sheet_name=["Справочник", "Раскладка"],
#                          index_col=0).values()
# data = df2.merge(df1, how="inner", left_index=True, right_index=True).fillna(0)
# print(*[int((data["Вес в граммах"]*data[name]/100).sum()) for name in data.columns[1:]])


# import pandas as pd
# pd.set_option('display.max_columns', None)
# url = 'https://stepik.org/media/attachments/lesson/245290/trekking3.xlsx'
# df1 = pd.read_excel(url, sheet_name='Справочник').fillna(0)
# df2 = pd.read_excel(url, sheet_name='Раскладка')
# df1 = df1.rename(columns={'Unnamed: 0': 'Product'})
# df2 = df2.rename(columns={'Продукт': 'Product'})
# unt = pd.merge(df1, df2, how='right', on='Product')
# data = unt.apply(lambda x: x['Вес в граммах']/100 * x[['ККал на 100', 'Б на 100', 'Ж на 100', 'У на 100']], axis=1)
# data['День'] = unt['День']
# list(map(lambda x: print(*x), data.groupby('День').sum().astype('int').to_numpy()))
# #v2
# unt['calories'] = unt['Вес в граммах'] * unt['ККал на 100'] / 100
# unt['proteins'] = unt['Вес в граммах'] * unt['Б на 100'] / 100
# unt['fats'] = unt['Вес в граммах'] * unt['Ж на 100'] / 100
# unt['carbohydrates'] = unt['Вес в граммах'] * unt['У на 100'] / 100
# print(unt.groupby('День').sum()[['calories', 'proteins', 'fats', 'carbohydrates']].astype(int).to_string(index=False))


# import zipfile as z
# import dload  # еще один способ скачивания архива
# import os
# import sys
# import xlrd3
# import pandas as pd
# url = "https://stepik.org/media/attachments/lesson/245299/rogaikopyta.zip"
# dload.save_unzip(url, "rogaikopyta.zip")
# with z.ZipFile("rogaikopyta.zip", "r") as zip_ref:
#     zip_ref.extractall("./extracted/")
# os.chdir("./extracted/")
# path = os.getcwd()
# dir_list = os.listdir(path)
# res = []
# for filename in dir_list:  # for root, dirs, files in os.walk("."): # for filename in files:
#     df = pd.read_excel(filename)
#     fio, salary = df.iloc[0, 1], df.iloc[0, 3]
#     res.append((fio, int(salary)))
#     # #v2
#     # res.append(xlrd3.open_workbook(filename).sheet_by_index(0).row_values(1))
# with open('output.txt', 'w', encoding='utf-8') as f:
#     sys.stdout = fhttps://stepik.org/media/attachments/lesson/245571/map1.osm
#     [f.write(f"{fio} {salary}\n") for fio, salary in sorted(res)]
#     # #v2
#     #[print(i[1], int(i[3]), file=f) for i in sorted(res, key=lambda x: x[1])]


# import requests
# import xmltodict
# url = 'https://stepik.org/media/attachments/lesson/245571/map1.osm'
# xml = requests.get(url).content
# parsedxml = xmltodict.parse(xml)
# print(parsedxml['osm']['node'][100]['@id'])


# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import math
# dpi = 80
# fig = plt.figure(dpi=dpi, figsize=(512/dpi, 384/dpi))
# mpl.rcParams.update({'font.size': 10})
# plt.axis([0, 10, -1.5, 1.5])
# plt.title('Sine & Cosine')
# plt.xlabel('x')
# plt.ylabel('F(x)')
# xs = []
# sin_vals = []
# cos_vals = []
# x = 0.0
# while x < 10.0:
#     sin_vals += [math.sin(3 * x)]
#     cos_vals += [math.cos(x)]
#     xs += [x]
#     x += 0.1
# plt.plot(xs, sin_vals, color='blue', linestyle='solid', label='sin(3x)')
# plt.plot(xs, cos_vals, color='red', linestyle='dashed', label='cos(x)')
# plt.legend(loc='lower left')
# plt.grid(True)
# fig.savefig('trigan.png')
# plt.show()


# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates
# import datetime as dt
# import csv
# data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'waste_disposal',
#               'atm', 'bench', 'parking', 'restaurant',
#               'place_of_worship']
# data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277,
#                5092, 3629]
# dpi = 80
# fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
# mpl.rcParams.update({'font.size': 10})
# plt.title('OpenStreetMap Point Types')
# ax = plt.axes()
# ax.yaxis.grid(True, zorder = 1)
# xs = range(len(data_names))
# plt.bar([x + 0.05 for x in xs], [ d * 0.9 for d in data_values],
#         width = 0.2, color = 'red', alpha = 0.7, label = '2016',
#         zorder = 2)
# plt.bar([x + 0.3 for x in xs], data_values,
#         width = 0.2, color = 'blue', alpha = 0.7, label = '2017',
#         zorder = 2)
# plt.xticks(xs, data_names)
# fig.autofmt_xdate(rotation = 25)
# plt.legend(loc='upper right')
# fig.savefig('bars.png')
# plt.show()


# from http.server import HTTPServer, CGIHTTPRequestHandler
# server_address = ('', 8000)
# httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# httpd.serve_forever()
# # python -mwebbrowser http://localhost:8000/cgi-bin/form.py




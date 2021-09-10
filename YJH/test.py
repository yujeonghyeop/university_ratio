# -*- coding: utf-8 -*- 

from bs4 import BeautifulSoup as bs
import requests
import time
now = time.localtime()
html1 = requests.get('http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11040241.html')
soup_1 = bs(html1.text,'html.parser')
data_ajou1 = soup_1.find('div',{'id':'SelType402'})
data_ajou2 = data_ajou1.findAll('td',{'class':'rate4'})
ajou = data_ajou2[0].text
print("현시간 : {0}-{1}-{2} {3}시{4}분".format(now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min))
print("아주대학교 Ace전형 기계공학과 모집인원 : 35, 현시간 경쟁률 - {}".format(ajou))

html = requests.get('http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11040241.html')
soup = bs(html.text,'html.parser')
data_ajou3 = soup.find('div',{'id':'SelType406'})
data_ajou4 = data_ajou3.findAll('td',{'class':'rate4'})
ajou1 = data_ajou4[0].text
print("아주대학교 고른기회2전형 기계공학과 모집인원 : 5.  현시간 경쟁률 - {}".format(ajou1))

html2 = requests.get('http://ratio.uwayapply.com/Sl5KMDpXJkpmJSY6JkpmZlRm')
soup_2 = bs(html2.text,'html.parser')
data_sct1 = soup_2.find('div',{'id':'Div_0001'})
data_sct2 = data_sct1.findAll('td')
sct=data_sct2[4].text
print("서울과학기술대학교 학교생활우수자전형 기계시스템디자인공학과 모집인원 : 33, 현시간 경쟁률 - {}".format(sct))

html3 = requests.get('http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11650381.html')
soup_3 = bs(html3.text,'html.parser')
data_hy1 = soup_3.find('div',{'id':'SelType4B'})
data_hy2 = data_hy1.findAll('td',{'class':'rate4'})
hy=data_hy2[8].text
print("한양대학교(ERICA) 학생부종합전형 로봇공학과 모집인원 : 22, 현시간 경쟁률 - {}".format(hy))

html4 = requests.get('http://addon.jinhakapply.com/RatioV1/RatioH/Ratio11400231.html')
soup_4 = bs(html4.text,'html.parser')
data_cn1 = soup_4.find('div',{'id':'SelType413'})
data_cn2 = data_cn1.findAll('td',{'class':'rate4'})
cn=data_cn2[42].text
print("충남대학교 PRISM전형 기계공학과 모집인원 : 16, 현시간 경쟁률 - {}".format(cn))
  
html5 = requests.get('http://ratio.uwayapply.com/Sl5KMCYlckpeJSY6JkpmZlRm')
soup_5 = bs(html5.text,'html.parser')
data_gist1 = soup_5.find('div',{'id':'table'})
data_gist2 = data_gist1.findAll('td')
gist=data_gist2[3].text
print("gist 일반전형 모집인원 : 110, 현시간 경쟁률 - {}".format(gist))

html6 = requests.get('http://ratio.uwayapply.com/Sl5KMCYlclZKXiUmOiZKZmZUZg==')
soup_6 = bs(html6.text,'html.parser')
data_dgist1 = soup_6.find('div',{'id':'table'})
data_dgist2 = data_dgist1.findAll('td')
dgist=data_dgist2[3].text
print("dgist 일반전형 모집인원 : {}, 현시간 경쟁률 - {}".format(data_dgist2[1].text,gist))

html8 = requests.get('http://ratio.uwayapply.com/Sl5KfExgMDhgfWE5SmYlJjomSmZmVGY=')
soup_8 = bs(html8.text,'html.parser')
data_hsc1 = soup_8.find('div',{'id':'Div_0012'})
data_hsc2 = data_hsc1.findAll('td')
hsc=data_hsc2[3].text
print("한국기술교육대학교 일반전형 모집인원 : 14, 현시간 경쟁률 - {}".format(hsc))

# html7 = requests.get('http://ratio.uwayapply.com/Sl5KMCYlVzpKXiUmOiZKZmZUZg==')
# soup_7 = bs(html7.text,'html.parser')
# data_unist1 = soup_7.find('div',{'id':'table'})
# data_unist2 = data_unist1.findAll('td')
# unist=data_unist2[3].text
# print("unist 일반전형 모집인원 : 280, 현시간 경쟁률 - {}".format(unist).rjust(100))
from bs4 import BeautifulSoup as bs
import urllib.request  
import re
import ssl
import pygal.maps.world
import time


# 多维列表：【国家全称，该国GP排行页面网址，国家简称（供地图使用），GP排名】
countryurls = [['United-states','https://appfigures.com/top-apps/google-play/united-states/top-overall','us',0],
    ['United-kingdom','https://appfigures.com/top-apps/google-play/united-kingdom/top-overall','gb',0],
    ['Canada','https://appfigures.com/top-apps/google-play/canada/top-overall','ca',0],
    ['Germany','https://appfigures.com/top-apps/google-play/germany/top-overall','de',0],
    ['Japan','https://appfigures.com/top-apps/google-play/japan/top-overall','jp',0],
    ['France','https://appfigures.com/top-apps/google-play/france/top-overall','fr',0],
    ['Italy','https://appfigures.com/top-apps/google-play/italy/top-overall','it',0],
    ['Australia','https://appfigures.com/top-apps/google-play/australia/top-overall','au',0],
    ['Algeria','https://appfigures.com/top-apps/google-play/algeria/top-overall','dz',0],
    ['Angola','https://appfigures.com/top-apps/google-play/angola/top-overall','ao',0],
               
#    ['Anguilla','https://appfigures.com/top-apps/google-play/anguilla/top-overall','',0],
#    ['Antigua-and-barbuda','https://appfigures.com/top-apps/google-play/antigua-and-barbuda/top-overall',''],

    ['Argentina','https://appfigures.com/top-apps/google-play/argentina/top-overall','ar',0],
    ['Armenia','https://appfigures.com/top-apps/google-play/armenia/top-overall','am',0],
    ['Austria','https://appfigures.com/top-apps/google-play/austria/top-overall','at',0],
    ['Azerbaijan','https://appfigures.com/top-apps/google-play/azerbaijan/top-overall','az',0],
#    ['Bahamas','https://appfigures.com/top-apps/google-play/bahamas/top-overall',''],
    ['Bahrain','https://appfigures.com/top-apps/google-play/bahrain/top-overall','bh',0],
#    ['Barbados','https://appfigures.com/top-apps/google-play/barbados/top-overall'],
    ['Belarus','https://appfigures.com/top-apps/google-play/belarus/top-overall','by',0],
    ['Belgium','https://appfigures.com/top-apps/google-play/belgium/top-overall','be',0],
    ['Belize','https://appfigures.com/top-apps/google-play/belize/top-overall','bz',0],
    ['benin','https://appfigures.com/top-apps/google-play/benin/top-overall','bj',0],
    ['bolivia','https://appfigures.com/top-apps/google-play/bolivia/top-overall','bo',0],
    ['botswana','https://appfigures.com/top-apps/google-play/botswana/top-overall','bw',0],
    ['brazil','https://appfigures.com/top-apps/google-play/brazil/top-overall','br',0],
    ['bulgaria','https://appfigures.com/top-apps/google-play/bulgaria/top-overall','bg',0],
    ['burkina-faso','https://appfigures.com/top-apps/google-play/burkina-faso/top-overall','bf',0],
    ['cambodia','https://appfigures.com/top-apps/google-play/cambodia/top-overall','kh',0],
    ['cape-verde','https://appfigures.com/top-apps/google-play/cape-verde/top-overall','cv',0],
    ['chile','https://appfigures.com/top-apps/google-play/chile/top-overall','cl',0],
    ['colombia','https://appfigures.com/top-apps/google-play/colombia/top-overall','co',0],
    ['costa-rica','https://appfigures.com/top-apps/google-play/costa-rica/top-overall','cr',0],
    ['croatia','https://appfigures.com/top-apps/google-play/croatia/top-overall','hr',0],
    ['cyprus','https://appfigures.com/top-apps/google-play/cyprus/top-overall','cy',0],
    ['czech-republic','https://appfigures.com/top-apps/google-play/czech-republic/top-overall','cz',0],
    ['denmark','https://appfigures.com/top-apps/google-play/denmark/top-overall','dk',0],
    ['dominican-republic','https://appfigures.com/top-apps/google-play/dominican-republic/top-overall','do',0],
    ['ecuador','https://appfigures.com/top-apps/google-play/ecuador/top-overall','ec',0],
    ['egypt','https://appfigures.com/top-apps/google-play/egypt/top-overall','eg',0],
    ['el-salvador','https://appfigures.com/top-apps/google-play/el-salvador/top-overall','sv',0]]
               
'''
    ['estonia','https://appfigures.com/top-apps/google-play/estonia/top-overall'],
    ['fiji','https://appfigures.com/top-apps/google-play/fiji/top-overall'],
    ['finland','https://appfigures.com/top-apps/google-play/finland/top-overall'],
    ['ghana','https://appfigures.com/top-apps/google-play/ghana/top-overall'],
    ['greece','https://appfigures.com/top-apps/google-play/greece/top-overall'],
    ['guatemala','https://appfigures.com/top-apps/google-play/guatemala/top-overall'],
    ['honduras','https://appfigures.com/top-apps/google-play/honduras/top-overall'],
    ['hongkongSAR','https://appfigures.com/top-apps/google-play/hong-kong/top-overall'],
    ['hungary','https://appfigures.com/top-apps/google-play/hungary/top-overall'],
    ['iceland','https://appfigures.com/top-apps/google-play/iceland/top-overall'],
    ['india','https://appfigures.com/top-apps/google-play/india/top-overall'],
    ['indonesia','https://appfigures.com/top-apps/google-play/indonesia/top-overall'],
    ['ireland','https://appfigures.com/top-apps/google-play/ireland/top-overall'],
    ['israel','https://appfigures.com/top-apps/google-play/israel/top-overall'],
    ['jamaica','https://appfigures.com/top-apps/google-play/jamaica/top-overall'],
    ['jordan','https://appfigures.com/top-apps/google-play/jordan/top-overall'],
    ['kazakhstan','https://appfigures.com/top-apps/google-play/kazakhstan/top-overall'],
    ['kenya','https://appfigures.com/top-apps/google-play/kenya/top-overall'],
    ['kuwait','https://appfigures.com/top-apps/google-play/kuwait/top-overall'],
    ['kyrgyzstan','https://appfigures.com/top-apps/google-play/kyrgyzstan/top-overall'],
    ['laos','https://appfigures.com/top-apps/google-play/laos/top-overall'],
    ['latvia','https://appfigures.com/top-apps/google-play/latvia/top-overall'],
    ['lebanon','https://appfigures.com/top-apps/google-play/lebanon/top-overall'],
    ['luxembourg','https://appfigures.com/top-apps/google-play/luxembourg/top-overall'],
    ['macedonia-fyrom','https://appfigures.com/top-apps/google-play/macedonia-fyrom/top-overall'],
    ['malaysia','https://appfigures.com/top-apps/google-play/malaysia/top-overall'],
    ['mali','https://appfigures.com/top-apps/google-play/mali/top-overall'],
    ['malta','https://appfigures.com/top-apps/google-play/malta/top-overall'],
    ['mauritius','https://appfigures.com/top-apps/google-play/mauritius/top-overall'],
    ['mexico','https://appfigures.com/top-apps/google-play/mexico/top-overall'],
    ['moldova','https://appfigures.com/top-apps/google-play/moldova/top-overall'],
    ['mozambique','https://appfigures.com/top-apps/google-play/mozambique/top-overall'],
    ['namibia','https://appfigures.com/top-apps/google-play/namibia/top-overall'],
    ['nepal','https://appfigures.com/top-apps/google-play/nepal/top-overall'],
    ['netherlands','https://appfigures.com/top-apps/google-play/netherlands/top-overall'],
    ['new-zealand','https://appfigures.com/top-apps/google-play/new-zealand/top-overall'],
    ['nicaragua','https://appfigures.com/top-apps/google-play/nicaragua/top-overall'],
    ['niger','https://appfigures.com/top-apps/google-play/niger/top-overall'],
    ['nigeria','https://appfigures.com/top-apps/google-play/nigeria/top-overall'],
    ['norway','https://appfigures.com/top-apps/google-play/norway/top-overall'],
    ['oman','https://appfigures.com/top-apps/google-play/oman/top-overall'],
    ['pakistan','https://appfigures.com/top-apps/google-play/pakistan/top-overall'],
    ['panama','https://appfigures.com/top-apps/google-play/panama/top-overall'],
    ['papua-new-guinea','https://appfigures.com/top-apps/google-play/papua-new-guinea/top-overall'],
    ['paraguay','https://appfigures.com/top-apps/google-play/paraguay/top-overall'],
    ['peru','https://appfigures.com/top-apps/google-play/peru/top-overall'],
    ['philippines','https://appfigures.com/top-apps/google-play/philippines/top-overall'],
    ['poland','https://appfigures.com/top-apps/google-play/poland/top-overall'],
    ['portugal','https://appfigures.com/top-apps/google-play/portugal/top-overall'],
    ['qatar','https://appfigures.com/top-apps/google-play/qatar/top-overall'],
    ['romania','https://appfigures.com/top-apps/google-play/romania/top-overall'],
    ['russia','https://appfigures.com/top-apps/google-play/russia/top-overall'],
    ['saudi-arabia','https://appfigures.com/top-apps/google-play/saudi-arabia/top-overall'],
    ['senegal','https://appfigures.com/top-apps/google-play/senegal/top-overall'],
    ['singapore','https://appfigures.com/top-apps/google-play/singapore/top-overall'],
    ['slovakia','https://appfigures.com/top-apps/google-play/slovakia/top-overall'],
    ['slovenia','https://appfigures.com/top-apps/google-play/slovenia/top-overall'],
    ['south-africa','https://appfigures.com/top-apps/google-play/south-africa/top-overall'],
    ['south-korea','https://appfigures.com/top-apps/google-play/south-korea/top-overall'],
    ['sri-lanka','https://appfigures.com/top-apps/google-play/sri-lanka/top-overall'],
    ['sweden','https://appfigures.com/top-apps/google-play/sweden/top-overall'],
    ['switzerland','https://appfigures.com/top-apps/google-play/switzerland/top-overall'],
    ['tajikistan','https://appfigures.com/top-apps/google-play/tajikistan/top-overall'],
    ['tanzania','https://appfigures.com/top-apps/google-play/tanzania/top-overall'],
    ['thailand','https://appfigures.com/top-apps/google-play/thailand/top-overall'],
    ['trinidad-and-tobago','https://appfigures.com/top-apps/google-play/trinidad-and-tobago/top-overall'],
    ['tunisia','https://appfigures.com/top-apps/google-play/tunisia/top-overall'],
    ['turkey','https://appfigures.com/top-apps/google-play/turkey/top-overall'],
    ['turkmenistan','https://appfigures.com/top-apps/google-play/turkmenistan/top-overall'],
    ['uae','https://appfigures.com/top-apps/google-play/uae/top-overall'],
    ['uganda','https://appfigures.com/top-apps/google-play/uganda/top-overall'],
    ['ukraine','https://appfigures.com/top-apps/google-play/ukraine/top-overall'],
    ['uruguay','https://appfigures.com/top-apps/google-play/uruguay/top-overall'],
    ['uzbekistan','https://appfigures.com/top-apps/google-play/uzbekistan/top-overall'],
    ['venezuela','https://appfigures.com/top-apps/google-play/venezuela/top-overall'],
    ['vietnam','https://appfigures.com/top-apps/google-play/vietnam/top-overall'],
    ['yemen','https://appfigures.com/top-apps/google-play/yemen/top-overall'],
    ['zimbabwe','https://appfigures.com/top-apps/google-play/zimbabwe/top-overall','zw',0]]


'''

ssl._create_default_https_context = ssl._create_unverified_context #全局取消证书验证

counlen = len(countryurls) #列表的长度

for index in range(counlen):
    country = countryurls[index][0] #国家全称
    url = countryurls[index][1] #url地址
    response = urllib.request.urlopen(url) #访问url页面
    if response.status == 200: #访问成功
        print('%d.\tGP Rank of %s read OK' %(index+1 , country))
    else: #访问失败
        print('%d.\tGP Rank of %s read error' %(index+1,country))
    
    soup = bs(response,"html.parser") #HTML解析
    restr = re.compile("TikTok\w*") #从HTML页面的标题titile中，寻找带TikTok开头的字符串
    ttag = soup.find( title = restr) #寻找符合条件的title
    if ttag == None: #没找到
        print('\tTikTok Rank Not found in TOP200 or website error!')
        countryurls[index][3] = -1 #记录在列表中，-1代表无效
    else :
        place = ttag.text.find('.') #寻找符号.
        num = int(ttag.text[0:place]) #符号.前面的数字 = GP排名 
        print('\tTikTok Rank at: %d' %num)
        countryurls[index][3] = num #把GP排名记录在列表中

#画世界地图

localtime = time.asctime(time.localtime(time.time()) )
worldmap_chart = pygal.maps.world.World() #世界地图初始化
worldmap_chart.title = 'TikTok\'s Rank in GooglePlay Top Free Apps' + '   [BJ time: ' + localtime + ']'#标题 

for index in range(counlen):
    if countryurls[index][3] != -1: #判断是否是有效数据
        worldmap_chart.add(countryurls[index][0], {
            countryurls[index][2]:countryurls[index][3]  #加入地图
    
    })
 
worldmap_chart.render_to_file('TikTokRanksAtGP.svg')        
print('Finished successfully!')



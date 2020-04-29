from bs4 import BeautifulSoup as bs
import urllib.request  
import re
import ssl


countryurls = [['United-states','https://appfigures.com/top-apps/google-play/united-states/top-overall'],
    ['United-kingdom','https://appfigures.com/top-apps/google-play/united-kingdom/top-overall'],
    ['Canada','https://appfigures.com/top-apps/google-play/canada/top-overall'],
    ['Germany','https://appfigures.com/top-apps/google-play/germany/top-overall'],
    ['Japan','https://appfigures.com/top-apps/google-play/japan/top-overall'],
    ['France','https://appfigures.com/top-apps/google-play/france/top-overall'],
    ['Italy','https://appfigures.com/top-apps/google-play/italy/top-overall'],
    ['Australia','https://appfigures.com/top-apps/google-play/australia/top-overall'],
    ['Algeria','https://appfigures.com/top-apps/google-play/algeria/top-overall'],
    ['Angola','https://appfigures.com/top-apps/google-play/angola/top-overall'],
    ['Anguilla','https://appfigures.com/top-apps/google-play/anguilla/top-overall'],
    ['Antigua-and-barbuda','https://appfigures.com/top-apps/google-play/antigua-and-barbuda/top-overall'],
    ['Argentina','https://appfigures.com/top-apps/google-play/argentina/top-overall'],
    ['Armenia','https://appfigures.com/top-apps/google-play/armenia/top-overall'],
    ['Austria','https://appfigures.com/top-apps/google-play/austria/top-overall'],
    ['Azerbaijan','https://appfigures.com/top-apps/google-play/azerbaijan/top-overall'],
    ['Bahamas','https://appfigures.com/top-apps/google-play/bahamas/top-overall'],
    ['Bahrain','https://appfigures.com/top-apps/google-play/bahrain/top-overall'],
    ['Barbados','https://appfigures.com/top-apps/google-play/barbados/top-overall'],
    ['Belarus','https://appfigures.com/top-apps/google-play/belarus/top-overall'],
    ['Belgium','https://appfigures.com/top-apps/google-play/belgium/top-overall'],
    ['Belize','https://appfigures.com/top-apps/google-play/belize/top-overall'],
    ['benin','https://appfigures.com/top-apps/google-play/benin/top-overall'],
    ['bolivia','https://appfigures.com/top-apps/google-play/bolivia/top-overall'],
    ['botswana','https://appfigures.com/top-apps/google-play/botswana/top-overall'],
    ['brazil','https://appfigures.com/top-apps/google-play/brazil/top-overall'],
    ['bulgaria','https://appfigures.com/top-apps/google-play/bulgaria/top-overall'],
    ['burkina-faso','https://appfigures.com/top-apps/google-play/burkina-faso/top-overall'],
    ['cambodia','https://appfigures.com/top-apps/google-play/cambodia/top-overall'],
    ['cape-verde','https://appfigures.com/top-apps/google-play/cape-verde/top-overall'],
    ['chile','https://appfigures.com/top-apps/google-play/chile/top-overall'],
    ['colombia','https://appfigures.com/top-apps/google-play/colombia/top-overall'],
    ['costa-rica','https://appfigures.com/top-apps/google-play/costa-rica/top-overall'],
    ['croatia','https://appfigures.com/top-apps/google-play/croatia/top-overall'],
    ['cyprus','https://appfigures.com/top-apps/google-play/cyprus/top-overall'],
    ['czech-republic','https://appfigures.com/top-apps/google-play/czech-republic/top-overall'],
    ['denmark','https://appfigures.com/top-apps/google-play/denmark/top-overall'],
    ['dominican-republic','https://appfigures.com/top-apps/google-play/dominican-republic/top-overall'],
    ['ecuador','https://appfigures.com/top-apps/google-play/ecuador/top-overall'],
    ['egypt','https://appfigures.com/top-apps/google-play/egypt/top-overall'],
    ['el-salvador','https://appfigures.com/top-apps/google-play/el-salvador/top-overall'],
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
    ['zimbabwe','https://appfigures.com/top-apps/google-play/zimbabwe/top-overall']]



ssl._create_default_https_context = ssl._create_unverified_context #全局取消证书验证

counlen = len(countryurls)

for index in range(counlen):
    country = countryurls[index][0]
    url = countryurls[index][1]
    response = urllib.request.urlopen(url)
    if response.status == 200:
        print('%d.\tGP Rank of %s read OK' %(index+1 , country))
    else:
        print('%d.\tGP Rank of %s read error' %(index+1,country))
    
    soup = bs(response,"html.parser")
    restr = re.compile("TikTok\w*")
    ttag = soup.find( title = restr)
    if ttag == None:
        print('\tTikTok Rank Not found in TOP200 or website error!')
    else :
        place = ttag.text.find('.')
        num = int(ttag.text[0:place])
        print('\tTikTok Rank at: %d' %num)
    
print('Finished successfully!')

import requests,time,openpyxl
from bs4 import BeautifulSoup

url = "https://www.iproperty.com.my/rent/all-residential/?sortBy=price-asc&q=Endah%20&page=1"
res_html = requests.get(url).text
soup = BeautifulSoup(res_html,"html.parser")
ul_target_tag = soup.find("ul",class_="listing-list ListingsListstyle__ListingsListContainer-cNRhPr hqtMPr") 
li_tag_list = ul_target_tag.find_all('li')
for li in li_tag_list:
    #agent_tag = li.find('h2',class_="BaseCardstyle__SecondaryStandardCardDescriptionHeadingContentMain-dfUtVF bfdugQ").text
    #提取中介信息
    post_date_tag = li.find('div',class_="BaseCardstyle__SecondaryStandardCardDescriptionHeadingContentSub-ckvTXs intlUx").text
    #提取发布日期
    price_tag = li.find('ul',class_="listing-primary-price ListingPrice__Wrapper-FYsEL cpaEEX").text
    #提取房租信息
    location_tag = li.find('p',class_="BaseCardstyle__SecondaryStandardCardTitleContent-fkLDZE fRrciN").text
    #提取地点信息
    type_tag = li.find('div',class_="BaseCardstyle__SecondaryStandardCardPropertyType-hnTcYt JQhFY").text
    #提取住宅类型信息 
    #提取额外信息，但是额外信息可能不存在
    if li.find('ul',class_="attributes-price-per-unit-size ListingAttrsPricePerUnitSizestyle__Wrapper-cLUNbG htlWnU") != None:
        addition_infor = li.find('ul',class_="attributes-price-per-unit-size ListingAttrsPricePerUnitSizestyle__Wrapper-cLUNbG htlWnU").text
        print(post_date_tag + '\n' + price_tag + '\n' + location_tag + '\n' + type_tag + '\n' + addition_infor + '\n')
    else:
        print(post_date_tag + '\n' + price_tag + '\n' + location_tag + '\n' + type_tag + '\n')

    





from lxml import html
import requests

LEBONCOIN_URL_TEMPLATE = 'https://www.leboncoin.fr/utilitaires/offres/?o=1&pe=11&rs=2010'

PAGE = requests.get(LEBONCOIN_URL_TEMPLATE)
TREE = html.fromstring(PAGE.content)

#This will create a list of buyers:
TITLES = TREE.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h2[@class="item_title"]/text()')
#This will create a list of prices
PRICES = TREE.xpath('//*[@id="listingAds"]/section/section/ul/li/a/section[@class="item_infos"]/h3[@class="item_price"]/text()')

print TITLES[2]
print PRICES[2]

# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

 
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
import scraperwiki
import requests
from bs4 import BeautifulSoup
import csv

# Download list of properties

lacey_properties = requests.get("https://pogodata.org/Html/Lacey_Twp-Ocean_County-(1513).html").text

data = []

soup = BeautifulSoup(lacey_properties,'html.parser')

table = soup.find_all('table')[0]
table_body = table.find('tbody')

rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])
    
# Select each field from the list of lists

parcels = [row[0] for row in data]
owner_name = [row[1] for row in data]
addresses = [row[2] for row in data]

# Convert to rows

csv_rows = zip(parcels, owner_name, addresses)

with open('data.csv', "w") as f:
    writer = csv.writer(f)
    for row in csv_rows:
        writer.writerow(row)

import urllib
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import urlencode
import xml.dom.minidom
from xml.dom.minidom import parseString

#finds apis from the sets I want & writes the list of urls to be queried into queries.txt
#the file here is the argument; I used diss_sets.txt
def apibuilder(file):
    queryfile = open(file, "r")
    #pulls the set ids from the record and splits into a list
    ids = queryfile.read()
    idlist = ids.split("\n")
    #builds OAI-MPH queries via the url below
    outputfile = open ("queries.txt",'w')
    for id in idlist:
        oiaquery = (f"https://academicworks.cuny.edu/do/oai/?verb=ListRecords&from=2015-01-01&until=2016-12-31&metadataPrefix=oai_dc&set={id}\n")
        outputfile.write(oiaquery)
    outputfile.close()
    queryfile.close()

#writes urls from the OAI doc into a queryresults document
def sourcelist(sourceurls):
    #opens list of urls, gets data, splits into urls
    source = open(sourceurls,"r")
    queries = source.read()
    querylist = queries.split("\n")
    #cycles through queries, reading each one
    startnumber = 0
    for query in querylist:
        print(f"Now analyzing {query}.")
        querynumber = str(startnumber + 1)
        #ports to dcscraper & creates a file with the urls
        dcscraper(query, querynumber)
        startnumber = startnumber + 1
    print("Done!")

#gets a list of the urls where the dissertations are located
#takes arguments from sourcelist
def dcscraper(query, querynumber):
    print(f"Now analyzing {query}.")
    #reads out the queries (the urls generated in sourcelist) and turns them to URLs
    file = urllib.request.urlopen(query)
    data = file.read()
    dom = parseString(data)
    print("String parsed.")
    #now, a file for our urls:
    outfile = open(f"queryresults{querynumber}.txt",'w')
    n = 0
    for line in data:
        try:
            url = dom.getElementsByTagName('dc:identifier')[n].firstChild.nodeValue
            if "cgi/" in url:
                print(f"Getting {url}")
                outfile.write(url)
                outfile.write("\n")
            else:
                pass
            n = n + 1
        #in case the pdf isn't available due to embargo:
        except:
            break
    file.close()
    outfile.close()
    print(f"Analysis of {query} complete.")


apibuilder("diss_sets.txt")
sourcelist("queries.txt")
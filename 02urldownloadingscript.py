import urllib
from urllib.request import urlopen
import glob
import os

#the previous main function which was really cool & if I knew what I were doing maybe I'd activate it again
#def main():
 #   urls = geturl()
 #   download_files(urls)

#pulls urls from the queryresults lists, breaks them into a list, and passes to download_files for downloading
#before I wrote this glob part, it just accepted a filename as an argument for this function
#This version downloads based on first digit: 1, 10, 11, 12, etc, then 2, 20 and so forth (when using folder{folder_number}). If you don't like that, use the commented-out version of folder_number below.
def geturl():
    #glob finds every file in the folder with the specified name
    for fname in glob.glob('queryresults*.txt'):
        folder_number = 1
        print(fname)
        #opens the file with the urls & splits them into a list
        queryfile = open(fname, "r")
        urls = queryfile.read()
        urls = urls.split("\n")
        print(urls)
        #folder_number = fname[12:]
        #opens a folder so I can have a different folder for each query
        os.mkdir(f"folder{folder_number}")
        print(f"Now opening folder {folder_number}")
        download_files(urls, folder_number)
        folder_number = folder_number + 1

#actually downloads the files
def download_files(urls, folder_number):
    #this is going to set the number for the document file
    #maybe we can find another way to name the files, but previous attempts to use the url failed
    start_number = 0
    #urls comes from the operation above where they were extracted from the query results files
    for download_url in urls:
        print(download_url)
        file_number = str(start_number + 1)
        #using try in order to avoid crashing when the embargoed urls come
        try:
            #opens the url online
            response = urlopen(download_url)
            print("Opened.")
            #opens the filename. Uses a direct path because I'm writing to the new folder defined above
            infile = open(f"\\Users\\nfoasberg\\Desktop\\projects\\citationextraction\\folder{folder_number}\\document{file_number}.pdf", 'wb')
            infile.write(response.read())
            print(f"Wrote document {file_number}")
            infile.close()
            start_number = start_number + 1
        except:
            print("Embargoed.")
            pass
    print("Completed")

geturl()

#if __name__ == "__main__":
#    main()
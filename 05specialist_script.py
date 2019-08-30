import PyPDF2

#This is for cases where bibstrip doesn't get the bibliography, either because it didn't use the keywords designated or because the script mistakenly identified the middle of the paper as the beginning of the bibliography
#This script extracts content from a specific document starting with a page you have identified manually
#Based on scripts in Automate the Boring Stuff with Python

#prints out the selected content so you can make sure you got the right part
def readfile():
    #use the document name for the relevant pdf (in this case, document 82)
    pdfFileObj = open("document82.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    #use the page number where the bibliography begins (in this case, page 195)
    for pageNum in range(195, pdfReader.numPages):
        print(pageNum)
        pageObj = pdfReader.getPage(pageNum)
        print("got page object.")
        text = pageObj.extractText().encode('utf-8')
        print("Text extracted.")
        string_text = str(text)
        print("Now it's a string.")
        list_text = string_text.split("\\n")
        print("list")
        for item in list_text:
            print(item)

#writes the relevant content to a text file
def writefile():
    pdfFileObj = open("document82.pdf", "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    textfile = open("document82pdfbib.txt","w")
    for pageNum in range(195, pdfReader.numPages):
        print("Extracting page.")
        pageObj = pdfReader.getPage(pageNum)
        text = pageObj.extractText().encode('utf-8')
        print("And here's the text.")
        newpage = str(text)
        print("Writing to the new file.")
        textfile.write(newpage)

    textfile.close()

readfile()
writefile()
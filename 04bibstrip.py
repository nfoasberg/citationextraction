import PyPDF2

#this is a script to extract the bibliographies from the pdfs and put them into text files.

#catches the documents that used a keyword more than once
def multibib():
    multibib_list = open("bib_2.txt", "r")
    docnames = []
    for title in multibib_list:
        listable_title = title.strip("\n")
        docnames.append(listable_title)
    for fname in docnames:
        print(fname)
        times_run = 0
        pdfFileObj = open(fname, "rb")
        textfile = open(f"{fname}bib.txt", "w")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        search_word_1 = "Works Cited"
        search_word_2 = "WORKS CITED"
        search_word_3 = "Bibliography"
        search_word_4 = "BIBLIOGRAPHY"
        search_word_5 = "References"
        search_word_6 = "REFERENCES"
        #this part identifies the beginning of the bibliography
        #in some cases, this may identify a use of the term "bibliography" that isn't the beginning of the bibliography, but it mostly works
        for pageNum in range(0, pdfReader.numPages):
            print(pageNum)
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText().encode('utf-8')
            string_text = str(text)
            list_text = string_text.split("\\n")
            print(f"{pageNum} is split.")
            #again, this could more efficiently be written as a function
            for paragraph in list_text:
                if search_word_2 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()
                elif search_word_1 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()
                elif search_word_3 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()
                elif search_word_4 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()
                elif search_word_5 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()
                elif search_word_6 in paragraph:
                    times_run = times_run + 1
                    if times_run == 2:
                        print("Found it twice.")
                        startpage = pageNum
                        print(startpage)
                        for pageNum in range(startpage, pdfReader.numPages):
                            print("Extracting page.")
                            pageObj = pdfReader.getPage(pageNum)
                            text = pageObj.extractText().encode('utf-8')
                            print("And here's the text.")
                            newpage = str(text)
                            print("Writing to the new file.")
                            textfile.write(newpage)
                        textfile.close()

#the same thing, but for docuements that only use the term "bibliography" once (most likely at the beginning of the bibliography)
def singlebib():
    singlebib_list = open("bib_1.txt", "r")
    docnames = []
    for title in singlebib_list:
        listable_title = title.strip("\n")
        docnames.append(listable_title)
    for fname in docnames:
        print(fname)
        pdfFileObj = open(fname, "rb")
        textfile = open(f"{fname}bib.txt", "w")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        search_word_1 = "Works Cited"
        search_word_2 = "WORKS CITED"
        search_word_3 = "Bibliography"
        search_word_4 = "BIBLIOGRAPHY"
        search_word_5 = "References"
        search_word_6 = "REFERENCES"
        for pageNum in range(0, pdfReader.numPages):
            print(pageNum)
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText().encode('utf-8')
            string_text = str(text)
            list_text = string_text.split("\\n")
            print(f"{pageNum} is split.")
            for paragraph in list_text:
                if search_word_1 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()
                elif search_word_2 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()
                elif search_word_3 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()
                elif search_word_4 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()
                elif search_word_5 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()
                elif search_word_6 in paragraph:
                    print("Found it.")
                    startpage = pageNum
                    print(startpage)
                    for pageNum in range(startpage, pdfReader.numPages):
                        print("Extracting page.")
                        pageObj = pdfReader.getPage(pageNum)
                        text = pageObj.extractText().encode('utf-8')
                        print("And here's the text.")
                        newpage = str(text)
                        print("Writing to the new file.")
                        textfile.write(newpage)
                    textfile.close()

multibib()
singlebib()
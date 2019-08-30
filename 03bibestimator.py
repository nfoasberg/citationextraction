import glob
import PyPDF2

#this is a function to find the page number on which the bibliography starts and extract it into a .txt file
#many dissertations will reference the bibliography once in their table of contents, and later where the bibliography is, so this function accounts for that
def bibpages():
    #creates a list of files that use "bibliography" or a similar word once (probably at the head of the bibliography), a list of files that use it twice, and a list of bibliographies that use some word I haven't guessed or don't have a bibliography
    bib_once = []
    bib_twice = []
    no_bib = []
    for fname in glob.glob('document*.pdf'):
        print(fname)
        times_run = 0
        pdfFileObj = open(fname, "rb")
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
        search_word_1 = "Bibliography"
        search_word_2 = "BIBLIOGRAPHY"
        search_word_3 = "References"
        search_word_4 = "REFERENCES"
        search_word_5 = "Works Cited"
        search_word_6 = "WORKS CITED"
        #finds the documents that mention one of these words at least twice and lists them 
        for pageNum in range(0, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            text = pageObj.extractText().encode('utf-8')
            string_text = str(text)
            search_text = string_text.split("\n")
            for paragraph in search_text:
                #note to self, write a function for this
                if search_word_1 in paragraph:
                    times_run = times_run + 1
                    print(pageNum)
                    print(search_word_1)
                    if times_run == 2:
                        bib_twice.append(fname)
                elif search_word_2 in paragraph:
                    times_run = times_run +1
                    print(pageNum)
                    print(search_word_2)
                    if times_run == 2:
                        bib_twice.append(fname)
                elif search_word_3 in paragraph:
                    times_run = times_run + 1
                    print(pageNum)
                    print(search_word_3)
                    if times_run == 2:
                        bib_twice.append(fname)
                elif search_word_4 in paragraph:
                    times_run = times_run + 1
                    print(pageNum)
                    print(search_word_4)
                    if times_run == 2:
                        bib_twice.append(fname)
                elif search_word_5 in paragraph:
                    times_run = times_run + 1
                    print(pageNum)
                    print(search_word_5)
                    if times_run == 2:
                        bib_twice.append(fname)
                elif search_word_6 in paragraph:
                    times_run = times_run + 1
                    print(pageNum)
                    print(search_word_6)
                    if times_run == 2:
                        bib_twice.append(fname)
        #finds the other bibliographies and lists them 
        if times_run == 1:
            bib_once.append(fname)
        if times_run == 0:
            no_bib.append(fname)

    #separates the lists into documents that can be referred to in scripts used later
    print(f"The following documents use the term 'Bibliography' or a similar term at least twice: {bib_twice}")
    print(f"The following documents use the term 'Bibliography' or a similar term only once: {bib_once}")
    print(f"The word 'Bibliography' was not found in the following documents, nor were similar terms: {no_bib}")
    textfile_bib_1 = open("bib_1.txt","w")
    for item in bib_once:
        textfile_bib_1.write(f"{item}\n")
    textfile_bib_1.close()
    textfile_bib_2 = open("bib_2.txt", "w")
    for item in bib_twice:
        textfile_bib_2.write(f"{item}\n")
    textfile_bib_2.close()
    textfile_no_bib = open("no_bib.txt","w")
    for item in no_bib:
        textfile_no_bib.write(f"{item}\n")
    textfile_no_bib.close()

bibpages()
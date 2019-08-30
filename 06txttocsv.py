import glob
import re

#pulls the journal titles into a csv
#an earlier version of this script accidentally created multiple copies of each newlines doc

#many documents included excessive newlines as an artifact of the processes by which they were created
#this script removes them all
#perhaps a more selective way of doing this would help by leaving the ones that are useful markers of new lines, but I couldn't think of a good way to do that
def remove_newlines():
    for fname in glob.glob("document*.txt"):
        infile = open(fname, "r")
        outfile = open(f'{fname}_no_newlines.txt', 'w')
        contents = infile.read()
        new_contents = contents.replace('\\n', '')
        outfile.write(new_contents)
        infile.close()
        outfile.close()

def make_csvs():
    output_bib = open("journal_citations.csv","w")
    for fname in glob.glob("*no_newlines.txt"):
        input_bib = open(fname, "r")
        input_text = input_bib.read()

        journal_citations = []

        listed_bibliography = re.compile(r'\d+\.').split(input_text)

        for element in listed_bibliography:
            #adds commas at the ends of words to split the cels in the csv file
            comma_separated_element = re.sub('\w\w\.', ',', element)
            journal_citations.append(comma_separated_element)
            journal_citations.append("\n")
    
        print(journal_citations)

        for item in journal_citations:
            output_bib.write(item)
        
        output_bib.write(f"end of {fname}")

    input_bib.close()
    output_bib.close()

def addlines(line, journal_citations, fname):
    comma_separated_element = re.sub('\w\w\.', ',', line)
    journal_citations.append(comma_separated_element)
    journal_citations.append (fname)
    journal_citations.append("\n")

def journal_csvs():
    output_bib = open("only_journal_citations.csv","w")
    for fname in glob.glob("*no_newlines.txt"):
        input_bib = open(fname, "r")
        input_text = input_bib.read()

        journal_citations = []

        #uses regular expressions to split into a list of entries ending with dates
        listed_bibliography = re.compile(r'\d\d\d\d\.').split(input_text)

        for line in listed_bibliography:
            
            #these conditions are an attempt to identify journal articles specifically
            #m finds numbers followed by a space and then a parenthesis (likely volume or issue numbers followed by a date)
            p = re.compile(r'\d+\s\(')
            m = p.findall(line)
            if m:
                addlines(line, journal_citations, fname)
            elif "no." in line:
                addlines(line, journal_citations, fname)
            elif "vol." in line:
                addlines(line, journal_citations, fname)    
            elif "No." in line:
                addlines(line, journal_citations, fname)
            elif "Vol." in line:
                addlines(line, journal_citations, fname)
            elif "olume" in line:
                addlines(line, journal_citations, fname)  
            else:
                #finds parenthesis followed by a colon, common in journal citations
                q = re.compile(r'\): ')
                n = q.findall(line)
                if n:
                    addlines(line, journal_citations, fname)         
            
        print(journal_citations)
        
        for item in journal_citations:
            output_bib.write(item)
        
        output_bib.write(f"end of {fname}")

    output_bib.close()

#if you run this script multiple times, remember to deactivate remove_newlines or you'll get multiple copies of each bibliography
remove_newlines()
journal_csvs()
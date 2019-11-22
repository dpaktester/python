import PyPDF2
import sys

# creating a pdf file object
pdfFileObj = open('F:\\Data_Collection\\Oscar California Standard 4 Tier Formulary_09012019_09112019.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print("Number of Pages in PDf is::",pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)
pageObj = pdfReader.getPage(180)
#for i in range(1, pdfReader. ):
    #pdfReader.getPage()


# extracting text from page
print(pageObj.extractText(),file=open("F:\\Data_Collection\\PdfExtract.txt", "a"))

print("Hello stackoverflow!", file=open("output.txt", "a"))
print("I have a question.", file=open("output.txt", "a"))


###stdoutOrigin=sys.stdout
###sys.stdout = open("F:\\Data_Collection\\PdfExtract.txt", "w")
###sys.stdout.close()
###sys.stdout=stdoutOrigin

# closing the pdf file object
pdfFileObj.close()
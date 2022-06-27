# ----------------------------------------------------------------------------
# Using Third-Party Python Packages
# ----------------------------------------------------------------------------

# import the modules
import PyPDF2
import pyttsx3
import pdfplumber
from tkinter import filedialog

file_path = filedialog.askopenfilename(initialdir='Downloads', title='Choose your PDF File')

# open and read file
file = open(file_path, 'rb')

# create object for the pdf file
pdf_reader = PyPDF2.PdfFileReader(file)

# get the starting page
total_pages = pdf_reader.numPages

with pdfplumber.open(file_path) as pdf:
    # traverse each page one by one
    for i in range(total_pages):
        # get current page
        page = pdf.pages[i]

        # extract the text content from each page
        text_content = page.extract_text()

        # create audio output object
        speaker = pyttsx3.init()

        # give it the text content to read
        speaker.say(text_content)

        # run the audio object.
        speaker.runAndWait()

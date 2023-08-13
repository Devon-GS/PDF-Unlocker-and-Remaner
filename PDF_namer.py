import os
from os import path
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter
from decrypt import password

# Create folders
locked_files_folder = path.exists('locked_files')

if locked_files_folder == False:
    os.mkdir('locked_files')

# Get list of files
# file_list = os.listdir('files')







# # Decrypt PDF
# reader = PdfReader("Locked.pdf")
# writer = PdfWriter()

# if reader.is_encrypted:
#     reader.decrypt(password)

# # Add all pages to the writer
# for page in reader.pages:
#     writer.add_page(page)

# # Save the new PDF to a file
# with open("decrypted-pdf.pdf", "wb") as f:
#     writer.write(f)


# # Look up Date of pdf and rename
# reader = PdfReader('Statement Unlocked.pdf')
# number_of_pages = len(reader.pages)
# page = reader.pages[0]
# text = page.extract_text()

# x = text.find('Statement period')
# # print(text[1302:1343])

# q = text[1302:1343]
# # print(q)

# w = q[18:28] + ' - ' + q[31:41]
# e = str(int(w[0:2]) + 1) 
# r = e + w[2:]
# print(r)
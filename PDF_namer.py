import os
from os import path
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter
from decrypt import password

# Create folders
locked_files_folder = path.exists('lockedFiles')
# processed_files = path.exists('processed_files')

if locked_files_folder == False:
    os.mkdir('lockedFiles')
# if processed_files == False:
#     os.mkdir('processed_files')

# Get list of files
file_list = os.listdir('lockedFiles')
# print(file_list)

# Decrypt PDF
for filename in file_list:
    file = f'lockedFiles/{filename}'
    
    # Open files with reader
    reader = PdfReader(file)
    writer = PdfWriter()
    
    # Check if encrypted
    if reader.is_encrypted:
        reader.decrypt(password)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open(file, "wb") as f:
        writer.write(f)

# Regid to find date
# Statement Period (\d{2}\/\d{2}\/\d{4} - \d{2}\/\d{2}\/\d{4})


# Get list of files
file_list_unlocked = os.listdir('lockedFiles')

# Look up Date of pdf and rename
for filename in file_list_unlocked:
    file = f"lockedFiles/{filename}"

    # Read in file and extract text
    reader = PdfReader(file)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()

    # Find Statement date
    find_date_beg = text.find('Statementperiod')
    find_date_end = find_date_beg + 41

    # Get full date
    full_date = text[find_date_beg:find_date_end]
    
    # Get date portion of string
    date_min = full_date[17:27] + ' - ' + full_date[30:40]

    # Check if begging date is less that 10
    if int(date_min[0:2]) < 10:
        date_min_str = str(int(date_min[0:2]) + 1)
        date_min_str = '0' + date_min_str
    else:
        date_min_str = str(int(date_min[0:2]) + 1)

    # Date to print to file 
    date_full = date_min_str + date_min[2:]
    date = date_full.replace("/",".")

    old = f"lockedFiles/{filename}"
    new = f"lockedFiles/{date + '.pdf'}"
    
    os.rename(old, new)
    
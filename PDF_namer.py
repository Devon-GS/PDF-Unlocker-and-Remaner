import os
from os import path
import re
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter
from decrypt import password

# Create folders
locked_files_folder = path.exists('locked_files')
processed_files = path.exists('processed_files')

if locked_files_folder == False:
    os.mkdir('locked_files')
if processed_files == False:
    os.mkdir('processed_files')

# Get list of files
file_list = os.listdir('locked_files')

#############################################################################
# DECRYPT PDF FILES AND RENAME THEM
#############################################################################

# Decrypt PDF
for filename in file_list:
    file = f'locked_files/{filename}'
    output_path = 'processed_files/'
    
    # Open files with reader
    reader = PdfReader(file)
    writer = PdfWriter()
    
    # Check if encrypted
    if reader.is_encrypted:
        reader.decrypt(password)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Get page one from pdf
    page_one_text = writer.pages[0].extract_text()
    
    # Repalce all spaces with '-' to get rid of special character
    x = page_one_text.encode("ascii", "ignore")
    y = x.decode()
    new_data = y.replace(' ','-')
    
    # Match regex to date and replace '-' with '.'
    match = re.findall(r"\d{2}\/\d{2}\/\d{4}--\d{2}\/\d{2}\/\d{4}", new_data)
    new_file_name = match[0].replace('--',' - ').replace('/','.')

    # Save decrypted file with new name in ouput folder
    with open(f"{output_path}{new_file_name}.pdf", "wb") as f:
        writer.write(f)
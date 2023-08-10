from PyPDF2 import PdfReader

reader = PdfReader('Statement Unlocked.pdf')
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

x = text.find('Statement period')
# print(text[1302:1343])

q = text[1302:1343]
# print(q)

w = q[18:28] + ' - ' + q[31:41]
e = str(int(w[0:2]) + 1) 
r = e + w[2:]
print(r)
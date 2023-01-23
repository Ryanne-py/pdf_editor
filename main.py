import fitz

filename = 'testpdf.pdf'
search_term = 'Engenier'
pdf = fitz.open(filename)

for page in range(len(pdf)):
    page = pdf.loadPage(page)

    if page.searchFor(search_term):
        print(f'{search_term} in page {page}')


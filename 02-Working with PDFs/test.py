import PyPDF2

pdf_file = PyPDF2.PdfFileReader(open('merged_pdf.pdf','rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf','rb'))
output = PyPDF2.PdfFileWriter()

for i in range(pdf_file.getNumPages()):
    page = pdf_file.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('Watermarked_pdf.pdf', 'wb') as new_pdf:
    output.write(new_pdf)


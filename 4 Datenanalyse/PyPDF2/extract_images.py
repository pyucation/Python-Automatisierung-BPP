from PyPDF2 import PdfReader

reader = PdfReader("4 Datenanalyse/PyPDF2/kriminelle.pdf")

# nur auf der ersten Seite
page = reader.pages[0]
count = 0

for image_file_object in page.images:
    with open(str(count) + image_file_object.name, "wb") as fp:
        fp.write(image_file_object.data)
        count += 1
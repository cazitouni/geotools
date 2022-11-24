from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PageObject

# Ouverture du fichier
pdf1File = open(r'C:\Users\345567\Bureau (local)\test\test.pdf', 'rb')

# Lecture du PDF
pdf1Reader = PdfFileReader(pdf1File)

# Création de la liste de pages
pages = []
for pageNum in range(pdf1Reader.numPages):
    pageObj = pdf1Reader.getPage(pageNum)
    pages.append(pageObj)

# Calcul de la hauteur et de la largeur de la page finale
width = pages[1].mediaBox.getWidth()
height = pages[1].mediaBox.getHeight() * 3

# Cération d'une page blanche
merged_page = PageObject.createBlankPage(None, width, height)
writer = PdfFileWriter()

# Boucle dans la liste de page pour les regrouper par 3 au sein d'une page unique
y=0
for page in range(len(pages)):
    if y%3==0 and y<=page:
        if y!=0 :
            merged_page = PageObject.createBlankPage(None, width, height)
        writer.addPage(merged_page)
        merged_page.mergePage(pages[y])
        y+= 1
        try :
            x=float(pages[y].mediaBox.getHeight())
            merged_page.mergeScaledTranslatedPage(pages[y], 1, 0, x)
            y+=1
        except :
            continue
        try :
            merged_page.mergeScaledTranslatedPage(pages[y], 1, 0, x * 2)
            y+=1
        except : 
            continue
        print("Traitement de la page {}/{}".format(y, len(pages)))

# Écriture du fichier
print("Écriture du fichier...")
with open('out.pdf', 'wb') as f:
    writer.write(f)
print("Traitement terminé")
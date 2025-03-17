import PyPDF2
filepath=r"C:\Users\ram7v\Downloads\Big Data\Big Data\data-engg-with-databricks\data-engineering-with-databricks\DE 1 - Databricks Workspace\data\d1\Extract Data from Pdf\student.pdf"
Pdf_File = open(filepath,"rb")
Pdf_reader=PyPDF2.PdfReader(Pdf_File)
print(len(Pdf_reader.pages))
for page in Pdf_reader.pages:
    print(page.extract_text())

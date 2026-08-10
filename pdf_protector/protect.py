from pypdf import PdfReader, PdfWriter

reader = PdfReader("download.pdf")
writer = PdfWriter()

writer.append(reader)
writer.encrypt("12345")

with open("encrypted.pdf", "wb") as f:
    writer.write(f)
from pypdf import PdfWriter

writer = PdfWriter()

for file in [
	"part.pdf","part2.pdf","part3.pdf"
]:writer.append(file)

writer.write("merged.pdf")
writer.close()
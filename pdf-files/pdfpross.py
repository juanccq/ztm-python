import PyPDF2

with open( 'dummy.pdf', 'rb' ) as file:
	reader = PyPDF2.PdfFileReader(file)
	# read page numbers
	print(reader.numPages)

	# get page
	print(reader.getPage(0))

	# rotate page
	page = reader.getPage(0)
	page.rotateCounterClockwise(90)
	writer = PyPDF2.PdfFileWriter()
	writer.addPage(page)

	with open( 'dummy-rotated.pdf', 'wb' ) as new_file:
		writer.write( new_file )
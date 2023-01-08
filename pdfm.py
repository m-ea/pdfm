import pypdf
import argparse

parser = argparse.ArgumentParser(description='Merge PDF files')
parser.add_argument('filenames', nargs = '+')
args = parser.parse_args()

merger = pypdf.PdfWriter()

for pdf in args.filenames:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close
# pdfm
A dead-simple Python tool to merge PDF files. I got sick of using someone else's tool to do this.

Requires pypdf library
```pip install pypdf```

Usage
```python pdfm.py "pdf-example1.pdf" "pdf-example2.pdf"```

Takes as many files as it is provided in the order you specify. Outputs a file named "merged-pdf.pdf" in the working directory.

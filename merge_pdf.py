"""
@gitsil10
@version 1.0
@date 2024-03-24
@file merge_pdf.py
@brief merge pdfs in the in directory
@usage python merge_pdf.py <result-file>
@note result-file is optional

@dependencies
pypdf -> pdfwriter
pdfwriter -> append | write

os -> path | remove | exists
sys -> argv | exit

@details
This script merges all pdfs in the in directory
and writes the merged pdf to the out directory
with the name result.pdf or <result-file>.pdf
"""

#imports
from pypdf import PdfWriter
from sys import argv, exit
from os import path, remove, getcwd, listdir

#input
result:tuple[str] = (argv[1] if len(argv) == 2 else "result",)
result = result[0]

#files in dir
in_path, out_path = f"{getcwd()}/in", f"{getcwd()}/out/{result}.pdf"
files:list[str] = listdir(in_path)
pdfs:list[str] = None

if path.exists(in_path):
    pdfs = sorted([f for f in files if f.endswith(".pdf")])
    print(f"pdfs in dir to merge\n{pdfs}")

#delete existing file
if path.exists(out_path):
    remove(out_path)
    print(f"file {result}.pdf exists\noverwriting file...")
elif not pdfs:
    print("no pdfs to merge\nexiting...")
    exit(0)
else:
    print(f"file does not exist\ncreating new file as {result}.pdf...")

with PdfWriter() as writer:
    if len(pdfs) > 0 and pdfs:
        #start merging
        for pdf in pdfs:
            writer.append(f"{in_path}/{pdf}")
            
        #merger action
        writer.write(out_path)
    else:
        print("no pdfs to merge")
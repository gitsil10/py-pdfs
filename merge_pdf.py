from pypdf import PdfMerger
import os

#input
result:str = sys.argv[1] if len(sys.argv == 2) else "result"
#files in dir
files = os.listdir(os.getcwd())
pdfs = [f for f in files if f.endswith(".pdf")]
print(f"pdfs in dir to merge\n{pdfs}")
merger = PdfMerger()
#start merge
for pdf in pdfs:
    merger.append(pdf)
#write
merger.write(f"{result}.pdf")
merger.close()


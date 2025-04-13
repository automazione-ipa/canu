from PyPDF2 import PdfReader
reader = PdfReader("2023_SAS_Textbook_CT_chap_10_shortened_v4.pdf")

num_pagine = len(reader.pages)
print(f"Numero di pagine: {num_pagine}")

for page in reader.pages:
    print(page.extract_text())
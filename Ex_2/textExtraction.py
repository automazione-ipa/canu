from PyPDF2 import PdfReader

# Funzione per estrarre il testo da un PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()  # Estrai il testo da ogni pagina
    return text

def find_information_in_text(text, keyword):
    # Cerca la chiave nel testo
    keyword_position = text.find(keyword)
    
    if keyword_position == -1:
        return "Chiave non trovata nel documento."
    
    start = keyword_position + len(keyword)
    end = text.find("\n", start)  # Trova la fine della riga o della sezione
    
    if end == -1:
        end = len(text)
    
    # Restituisce la porzione di testo associata alla chiave
    return text[start:end].strip()

# Funzione principale
def main(pdf_path, keyword):
    text = extract_text_from_pdf(pdf_path)  
    result = find_information_in_text(text, keyword)  # Trova l'informazione associata
    return result

if __name__ == "__main__":
    pdf_path = "2023_SAS_Textbook_CT_chap_10_shortened_v4.pdf"  
    keyword = "LTI"  
    result = main(pdf_path, keyword)
    print("Informazione trovata:", result)

def agente_cocktail():
    while True:
        messaggio = input("Che ti sbrodoli oggi tra questi?:\n- Mojito\n- Negroni\n- PinaColada\n").lower()
        
        if messaggio == "mojito":
            print("\nAgente\nOttima scelta: Rum bianco, Zucchero, Succo di lime, Menta, Soda\n\n")
        elif messaggio == "negroni":
            print("\nAgente\nOttima scelta: Gin, Vermouth rosso, Campari\n\n")
        elif messaggio == "pinacolada":
            print("\nAgente\nOttima scelta: Rum bianco, Succo d'ananas, Latte di cocco\n\n")
            break
        else:
            print("\nAgente: Non ho questa bevanda\n\n")

# Avvia l'agente
agente_cocktail()
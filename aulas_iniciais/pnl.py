def reflexao_emocional():
    na_bad = True

    while na_bad:
        print("Estou me sentindo triste...")

        acao = input("Posso fazer algo a respeito? (sim ou nao): ")

        if acao.lower() == "sim":
            print("Paro de sofrer e resolvo da forma que da.")
            break 
        
        elif acao.lower() == "não":
            print("Paro de sofrer do mesmo jeito porque se nao tem nada que eu possa fazer entao nao eh problema meu.")
            break

reflexao_emocional()

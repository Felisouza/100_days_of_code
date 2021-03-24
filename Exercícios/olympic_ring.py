def olympic_ring(string):
    #your code here
    pontuacao = 0
    for i in string:
        if i == 'a':
            pontuacao += 1
        if i == 'A':
            pontuacao += 1
        if i == 'b':
            pontuacao += 1
        if i == 'B':
            pontuacao += 2
        if i == 'd':
            pontuacao += 1
        if i == 'D':
            pontuacao += 1
        if i == 'e':
            pontuacao += 1
        if i == 'g':
            pontuacao += 1
        if i == 'o':
            pontuacao += 1 
        if i == 'O':
            pontuacao += 1 
        if i == 'p':
            pontuacao += 1 
        if i == 'P':
            pontuacao += 1 
        if i == 'q':
            pontuacao += 1  
        if i == 'R':
            pontuacao += 1     
            
            
        #print(pontuacao)
    pontuacao = pontuacao/2
    #print(pontuacao)
    if pontuacao <= 1:
        return 'Not even a medal!'
    elif pontuacao > 1 and pontuacao <= 2:
        return 'Bronze!'
    elif pontuacao > 2 and pontuacao <=3:
        return 'Silver!'
    elif pontuacao > 3:
        return 'Gold!'
# coding=UTF-8
from operator import itemgetter
from graphics import *
import random

window = GraphWin("Main Window", 1000, 600)

# MENU INICIAL

def inicio(x):
    p = Point(500, 300)
    p_jogar = Point(500, 200)
    p_sair = Point(500, 300)
    p_nome = Point(500, 60)
    nome = Image(p_nome, "imagens/nome_jogo.png")
    jogar = Image(p_jogar, "imagens/jogar.png")
    sair = Image(p_sair, "imagens/sair.png")
    inicio = Image(p, "imagens/menu.png")
    inicio.draw(window)
    jogar.draw(window)
    sair.draw(window)
    nome.draw(window)
    flag = False
    x.sort(key=itemgetter(0))  # ORDENA A LISTA DE PONTUAÇÃO
    x.reverse()

    placar = Rectangle(Point(100, 100), Point(300, 500))
    placar.setFill("White")
    placar.draw(window)
    nomes = Text(Point(195, 140), "Placar \n Level / Nome")
    nomes.setSize(23)
    nomes.draw(window)
    y = 200

    for o in x[0:12]:
        messege = Text(Point(175, y), o)
        messege.draw(window)
        y = y + 20
    while (flag != True):
        mouse = window.getMouse()
        px_mouse = mouse.getX()
        py_mouse = mouse.getY()
        if (px_mouse >= 382 and px_mouse <= 618 and py_mouse >= 157 and py_mouse <= 243):
            jogar.undraw()
            jogar = Image(p_jogar, "imagens/jogar_click.png")
            jogar.draw(window)
            time.sleep(0.15)
            flag = True
            return True
        if (px_mouse >= 415 and px_mouse <= 585 and py_mouse >= 267 and py_mouse <= 343):
            sair.undraw()
            sair = Image(p_sair, "imagens/sair_click.png")
            sair.draw(window)
            time.sleep(0.15)
            flag = True
            return False


# TELAS QUE INDICAM O NIVEL DO JOGO

def telalevel(pontos):
    ponto_retangulo = Point(0, 0)
    ponto_retangulo2 = Point(1000, 600)
    retangulo_fundo = Rectangle(ponto_retangulo, ponto_retangulo2)
    retangulo_fundo.setFill("black")
    retangulo_fundo.setOutline('black')
    retangulo_fundo.draw(window)
    if (pontos == 0):
        ponto_nivel = Point(500, 300)
        string = " BOA SORTE!"
        nivel = Text(ponto_nivel, string)
        nivel.setTextColor("White")
        nivel.setSize(100)
        nivel.draw(window)
        time.sleep(1)
        nivel.undraw()
    else:
        ponto_parabens = Point(500, 100)
        ponto_nivel = Point(500, 300)
        ponto_sorte = Point(500, 500)
        string_parabens = "PARABÉNS!"
        string = " Sua pontuação: " + str(pontos)

        parabens = Text(ponto_parabens, string_parabens)
        parabens.setTextColor("White")
        parabens.setSize(100)
        parabens.draw(window)

        nivel = Text(ponto_nivel, string)
        nivel.setTextColor("White")
        nivel.setSize(100)
        nivel.draw(window)

        sorte = Text(ponto_sorte, string_sorte)
        sorte.setTextColor("White")
        sorte.setSize(100)
        sorte.draw(window)

        time.sleep(2)
        parabens.undraw()
        sorte.undraw()
        nivel.undraw()
        
# FUNÇÃO DA DERROTA

def perdeu():
	ponto_nivel = Point(500,300)
	string = "GAME OVER!\nNome para salvar sua pontuação"
	perdeu = Text(ponto_nivel, string)
	perdeu.setTextColor("White")
	perdeu.setSize(36)
	perdeu.draw(window)
	time.sleep(1)
	ponto_entry= Point(500,400)
	input_box = Entry(ponto_entry , 10)
	input_box.draw(window)
	tecla = window.checkKey()
	while(tecla != 'Return'):
		tecla = window.checkKey()
	inputstr = input_box.getText()
	if(len(inputstr)<15):
		inputstr = inputstr +(15-len(inputstr))*' '
	if(len(inputstr)>15):
		inputstr = inputstr[0:15]
	if(inputstr == ''):
		inputstr = "Sem nome"
	input_box.undraw()
	return inputstr
    
#COLISAO

def colisao(x1, y1, x2, y2, lar1, alt1, lar2, alt2):
	#Pontos superior esquesdo e inferior direito Objeto 1
	a1=x1-(lar1/2)
	b1=y1-(alt1/2)
	c1=x1+(lar1/2)
	d1=y1+(alt1/2)
	#Pontos superior esquesdo e inferior direito Objeto 2
	a2=x2-(lar2/2)
	b2=y2-(alt2/2)
	c2=x2+(lar2/2)
	d2=y2+(alt2/2)
	if((a1 >= a2 and a1 <= c2 and b1 >= b2 and b1 <= d2) or (c1 <= c2 and a2 <= c1 and d1 >= b2 and d1 <= d2)):
		return True
	else:
		return False 

# PRINCIPAL FUNCAO DO JOGO

def game():
    
    #CRIACAO DO UNIVERSO ESTRELADO
    pnt_central_univer = Point(900, 0)
    tela_universo1 = Image(pnt_central_univer, "imagens/ceu1.png")
    tela_universo1.draw(window)

    #CRIACAO DA TELA DE CONSULTA DE PONTUÇÕES

    pnt_central_consul = Point(50, 300)
    tela_consulta = Image(pnt_central_consul, "imagens/consulta.png")
    tela_consulta.draw(window)

    #CRIANDO A NAVE
    pnt_central_nave = Point(500, 535)
    nave = Image(pnt_central_nave, "imagens/nave.png")
    nave.draw(window)
    
    #VARIAVEIS INICILIZADAS
    veloc_ast = 0
    velocidade_nave_hor = 15
    velocidade_nave_ver = 15
    flag_vert_dow = False
    flag_vert_up = True
    flag_hor_esq = False
    flag_hor_dir = False
    flag_tiro = False
    atirou = False
    tiro_fora = True
    flag_ast = False
    flag_ast2 = False
    flag_ast3 = False
    flag_ast4 = False
    flag_ast5 = False
    flag_ast6 = False
    flag_ast7 = False
    flag_ast8 = False
    flag_ast9 = False
    flag_ast10 = False
    
    #INFORMAÇÕES AO LADO ESQUERDO DO JOGO
    global flag_acabou
    global pontos
    pontos = 0
    
    text_ast1 = Image(Point(50, 230), "imagens/nave.png")
    text_ast1.draw(window)
    
    text_pnto = Text(Point(50, 100), "PONTOS")
    text_pnto.setTextColor("red")
    text_pnto.setSize(17)
    text_pnto.draw(window)
    
    
    text_pnt = Text(Point(50, 150), str(pontos))
    text_pnt.setTextColor("red")
    text_pnt.setSize(50)
    text_pnt.draw(window)
    
    text_ast1 = Image(Point(50, 420), "imagens/ast1.png")
    text_ast1.draw(window)
    
    text_ast2 = Image(Point(50, 470), "imagens/ast2.png")
    text_ast2.draw(window)
    
    text_ast3 = Image(Point(50, 550), "imagens/ast3.png")
    text_ast3.draw(window)
    
    text_pnt1 = Text(Point(50, 420), "*5P*")
    text_pnt1.setTextColor("black")
    text_pnt1.setSize(12)
    text_pnt1.draw(window)
    
    text_pnt2 = Text(Point(50, 470), "*3P*")
    text_pnt2.setTextColor("black")
    text_pnt2.setSize(15)
    text_pnt2.draw(window)
    
    text_pnt3 = Text(Point(50, 550), "*1P*")
    text_pnt3.setTextColor("black")
    text_pnt3.setSize(20)
    text_pnt3.draw(window)
    
    while True:
        
        #ASTEROIDES
        
        #AST_1
        if flag_ast == False:
            pnt_ast = Point(random.randint(120,980), random.randint(-40,-30))
            ast = Image(pnt_ast, "imagens/ast3.png")
            ast.draw(window)
            flag_ast = True
        ast.move(0, 3)
        ast_x = ast.getAnchor().getX()
        ast_y = ast.getAnchor().getY()
        if ast_y >= 630:
            flag_ast = False
            ast.undraw()
        #AST_2
        if flag_ast2 == False:
            pnt_ast2 = Point(random.randint(500,980), random.randint(-40,-30))
            ast2 = Image(pnt_ast2, "imagens/ast3.png")
            ast2.draw(window)
            flag_ast2 = True
        ast2.move(-2, 3 + veloc_ast)
        ast_x2 = ast2.getAnchor().getX()
        ast_y2 = ast2.getAnchor().getY()
        if ast_y2 >= 630:
            flag_ast2 = False
            ast2.undraw()
        #AST_3
        if flag_ast3 == False:
            pnt_ast3 = Point(random.randint(120,500), random.randint(-45,-20))
            ast3 = Image(pnt_ast3, "imagens/ast2.png")
            ast3.draw(window)
            flag_ast3 = True
        ast3.move(2, 2)
        ast_x3 = ast3.getAnchor().getX()
        ast_y3 = ast3.getAnchor().getY()
        if ast_y3 >= 630:
            flag_ast3 = False
            ast3.undraw()
        #AST_4
        if flag_ast4 == False:
            pnt_ast4 = Point(random.randint(500,980), random.randint(-70,-20))
            ast4 = Image(pnt_ast4, "imagens/ast1.png")
            ast4.draw(window)
            flag_ast4 = True
        ast4.move(-2, 2.5 + veloc_ast)
        ast_x4 = ast4.getAnchor().getX()
        ast_y4 = ast4.getAnchor().getY()
        if ast_y4 >= 630:
            flag_ast4 = False
            ast4.undraw()   
        #AST_5    
        if flag_ast5 == False:
            pnt_ast5 = Point(random.randint(120,500), random.randint(-80,-20))
            ast5 = Image(pnt_ast5, "imagens/ast1.png")
            ast5.draw(window)
            flag_ast5 = True
        ast5.move(2, 2.5 + veloc_ast)
        ast_x5 = ast5.getAnchor().getX()
        ast_y5 = ast5.getAnchor().getY()
        if ast_y4 >= 630:
            flag_ast5 = False
            ast5.undraw() 
        #AST_6
        if flag_ast6 == False:
            pnt_ast6 = Point(random.randint(120,980), random.randint(-90,-30))
            ast6 = Image(pnt_ast6, "imagens/ast3.png")
            ast6.draw(window)
            flag_ast6 = True
        ast6.move(0, 1.5)
        ast_x6 = ast6.getAnchor().getX()
        ast_y6 = ast6.getAnchor().getY()
        if ast_y6 >= 630:
            flag_ast6 = False
            ast6.undraw()
        #AST_7
        if flag_ast7 == False:
            pnt_ast7 = Point(random.randint(500,980), random.randint(-110,-20))
            ast7 = Image(pnt_ast7, "imagens/ast2.png")
            ast7.draw(window)
            flag_ast7 = True
        ast7.move(-2, 2)
        ast_x7 = ast7.getAnchor().getX()
        ast_y7 = ast7.getAnchor().getY()
        if ast_y7 >= 630:
            flag_ast7 = False
            ast5.undraw()
        #AST_8
        if flag_ast8 == False:
            pnt_ast8 = Point(random.randint(120,980), random.randint(-120,-20))
            ast8 = Image(pnt_ast8, "imagens/ast2.png")
            ast8.draw(window)
            flag_ast8 = True
        ast8.move(0, 2)
        ast_x8 = ast8.getAnchor().getX()
        ast_y8 = ast8.getAnchor().getY()
        if ast_y8 >= 630:
            flag_ast8 = False
            ast8.undraw()
        #AST_9
        if flag_ast9 == False:
            pnt_ast9 = Point(random.randint(120,980), random.randint(-105,-20))
            ast9 = Image(pnt_ast9, "imagens/ast1.png")
            ast9.draw(window)
            flag_ast9 = True
        ast9.move(0, 2)
        ast_x9 = ast9.getAnchor().getX()
        ast_y9 = ast9.getAnchor().getY()
        if ast_y9 >= 630:
            flag_ast9 = False
            ast9.undraw()
        #AST_10
        if flag_ast10 == False:
            pnt_ast10 = Point(random.randint(120,980), random.randint(-200,-20))
            ast10 = Image(pnt_ast10, "imagens/ast1.png")
            ast10.draw(window)
            flag_ast10 = True
        ast10.move(0, 2)
        ast_x10 = ast10.getAnchor().getX()
        ast_y10 = ast10.getAnchor().getY()
        if ast_y10 >= 630:
            flag_ast10 = False
            ast10.undraw() 
            
        #PONTUÇÃO ATUALIZADA NA TELA
        text_pnt.undraw()
        text_pnt = Text(Point(50, 150), str(pontos))
        text_pnt.setTextColor("red")
        text_pnt.setSize(50)
        text_pnt.draw(window)  
            
        #MOVIMENTACAO DA TELA UNIVERSO
        tela_universo1.move(0, 10)
        
        #FINAL DE LEVEL
        cent_tela_uni = tela_universo1.getAnchor().getY() - 5440
        if (cent_tela_uni >= 0):
            tela_universo1.move(0, -8040)
            veloc_ast += 1
            

        # MOVIMENTAÇÃO DA NAVE NA VERTICAL E HORIZONTAL 
        tecla = window.checkKey()
        if (tecla == "w" or tecla == "Up") and flag_vert_up == True:
            nave.move(0, -(velocidade_nave_ver))
            flag_vert_dow = True
            
        if (tecla == "s" or tecla == "Down") and flag_vert_dow == True:
            nave.move(0, velocidade_nave_ver)
            
        if (tecla == "a" or tecla == "Left") and flag_hor_esq == False:
            nave.move(-(velocidade_nave_hor), 0)
            flag_hor_dir = False
            
            
        if (tecla == "d" or tecla == "Right") and flag_hor_dir == False:
            nave.move(velocidade_nave_hor, 0)
            flag_hor_esq = False

        # MOVIMENTAÇÃO DA NAVE NAS DIAGONAIS
        if tecla == "e" and flag_hor_dir == False:
            nave.move(velocidade_nave_ver, -(velocidade_nave_ver))
            flag_hor_esq = False
            flag_vert_dow = True
        elif tecla == "e" and flag_hor_dir == True:
            nave.move(0, -(velocidade_nave_ver))
            flag_hor_esq = False
            flag_vert_dow = True

        if tecla == "q" and flag_hor_esq == False:
            nave.move(-(velocidade_nave_ver), -(velocidade_nave_ver))
            flag_hor_dir = False
            flag_vert_dow = True
        elif tecla == "q" and flag_hor_esq == True:
            nave.move(0, -(velocidade_nave_ver))
            flag_hor_dir = False
            flag_vert_dow = True

        if tecla == "z" and flag_vert_dow == True and flag_hor_esq == False:
            nave.move(-(velocidade_nave_ver), velocidade_nave_ver)
            flag_hor_dir = False
        elif tecla == "z" and flag_vert_dow == False and flag_hor_esq == False:
            nave.move(-(velocidade_nave_ver), 0)
            flag_hor_dir = False

        if tecla == "x" and flag_vert_dow == True and flag_hor_dir == False:
            nave.move(velocidade_nave_ver, velocidade_nave_ver)
            flag_hor_esq = False
        elif tecla == "x" and flag_vert_dow == False and flag_hor_dir == False:
            nave.move(velocidade_nave_ver, 0)
            flag_hor_esq = False

        # LIMITAÇÃO DA NAVE NA TELA
        px_nave = nave.getAnchor().getX()
        py_nave = nave.getAnchor().getY()
        if (px_nave >= 965):
            flag_hor_dir = True
        if (px_nave <= 140):
            flag_hor_esq = True
        if (py_nave >= 535):
            flag_vert_dow = False
        if (py_nave <= 400):
            nave.move(0, 0.2)
        if (py_nave <= 40):
            flag_vert_up = False
        if (py_nave >= 65):    
            flag_vert_up = True
            
         #COLISÃO NAVE COM ASTEROIDES
       
        coli_nave1 = colisao(px_nave, py_nave, ast_x, ast_y, 85, 60, 80, 80)
        coli_nave2 = colisao(px_nave, py_nave, ast_x2, ast_y2, 85, 60, 80, 80)
        coli_nave3 = colisao(px_nave, py_nave, ast_x3, ast_y3, 85, 60, 50, 50)
        coli_nave4 = colisao(px_nave, py_nave, ast_x4, ast_y4, 85, 60, 30, 30)
        coli_nave5 = colisao(px_nave, py_nave, ast_x5, ast_y5, 85, 60, 30, 30)
        coli_nave6 = colisao(px_nave, py_nave, ast_x6, ast_y6, 85, 60, 80, 80)
        coli_nave7 = colisao(px_nave, py_nave, ast_x7, ast_y7, 85, 60, 50, 50)
        coli_nave8 = colisao(px_nave, py_nave, ast_x8, ast_y8, 85, 60, 50, 50)
        coli_nave9 = colisao(px_nave, py_nave, ast_x9, ast_y9, 85, 60, 30, 30) 
        coli_nave10 = colisao(px_nave, py_nave, ast_x10, ast_y10, 85, 60, 30, 30)
        
        if coli_nave1 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave2 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave3 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave4 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave5 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave6 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return Falseww  
        if coli_nave7 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave8 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave9 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        if coli_nave10 == True:
            exp = Image(Point(px_nave, py_nave), "imagens/exp.png")
            exp.draw(window)
            return False
        
       # ATAQUE COM LASER
        
        if (tecla == "space") and (tiro_fora == True):
            pnt_tiro1 = Point(px_nave, py_nave - 15)
            pnt_tiro2 = Point(px_nave, py_nave - 60)
            atirou = True
            tiro_fora = False
            tiro = Line(pnt_tiro1, pnt_tiro2)
            tiro.setFill("red")
            tiro.setWidth("5")
            tiro.draw(window)
          
        if (atirou == True):
            tiro.move(0, -50)
            px_tiro = tiro.getCenter().getX()
            py_tiro = tiro.getCenter().getY()
            
            #TESTE DE COLISÃO DO LAZER#
            coli_tiro1 = colisao(px_tiro, py_tiro, ast_x, ast_y, 5, 45, 80, 80)
            coli_tiro2 = colisao(px_tiro, py_tiro, ast_x2, ast_y2, 5, 45, 80, 80)
            coli_tiro3 = colisao(px_tiro, py_tiro, ast_x3, ast_y3, 5, 45, 50, 50)
            coli_tiro4 = colisao(px_tiro, py_tiro, ast_x4, ast_y4, 5, 45, 30, 30)
            coli_tiro5 = colisao(px_tiro, py_tiro, ast_x5, ast_y5, 5, 45, 30, 30)
            coli_tiro6 = colisao(px_tiro, py_tiro, ast_x6, ast_y6, 5, 45, 80, 80)
            coli_tiro7 = colisao(px_tiro, py_tiro, ast_x7, ast_y7, 5, 45, 50, 50)
            coli_tiro8 = colisao(px_tiro, py_tiro, ast_x8, ast_y8, 5, 45, 50, 50)
            coli_tiro9 = colisao(px_tiro, py_tiro, ast_x9, ast_y9, 5, 45, 30, 30)
            coli_tiro10 = colisao(px_tiro, py_tiro, ast_x10, ast_y10, 5, 45, 30, 30)
            
            if coli_tiro1 == True:
                flag_ast = False
                ast.undraw()
                tiro.move(0, -500)
                tiro.undraw()
                pontos += 1
            if coli_tiro2 == True:
                flag_ast2 = False
                tiro.move(0, -500)
                ast2.undraw()
                tiro.undraw()
                pontos += 1
            if coli_tiro3 == True:
                flag_ast3 = False
                tiro.move(0, -500)
                ast3.undraw()
                tiro.undraw()
                pontos += 3
            if coli_tiro4 == True:
                flag_ast4 = False
                tiro.move(0, -500)
                ast4.undraw()
                tiro.undraw()
                pontos += 5
            if coli_tiro5 == True:
                flag_ast5 = False
                tiro.move(0, -500)
                ast5.undraw()
                tiro.undraw()
                pontos += 5
            if coli_tiro6 == True:
                flag_ast6 = False
                tiro.move(0, -500)
                ast6.undraw()
                tiro.undraw()
                pontos += 1
            if coli_tiro7 == True:
                flag_ast7 = False
                tiro.move(0, -500)
                ast7.undraw()
                tiro.undraw()
                pontos += 3
            if coli_tiro8 == True:
                flag_ast8 = False
                tiro.move(0, -500)
                ast8.undraw()
                tiro.undraw()
                pontos += 3
            if coli_tiro9 == True:
                flag_ast9 = False
                tiro.move(0, -500)
                ast9.undraw()
                tiro.undraw()
                pontos += 5
            if coli_tiro10 == True:
                flag_ast10 = False
                tiro.move(0, -500)
                ast10.undraw()
                tiro.undraw()
                pontos += 5
                
            #ELIMINANDO O TIRO DA TELA    
            if (py_tiro <= 0):
                tiro.undraw()
                tiro_fora = True
                atirou = False
                      

# ABERTURA DO ARQUIVO QUE SALVA O LEVEL E NOME DOS JOGADORESs
arquivo = open('pontuacoes.txt', 'r')
x = arquivo.readlines()
arquivo = open('pontuacoes.txt', 'a')

################## ESTRUTURA PARA INICIALIZAR A JOGATINA ########################
pontos = 0
jogar = inicio(x)
ganhou = True

if(jogar == True):
	telalevel(pontos)
	while(ganhou == True):
		ganhou = game()
		if(ganhou == False):
			nome = perdeu()
			x.append(str(pontos) + ' ' + nome +' \n')
			arquivo.writelines([str(pontos) + ' ' +nome +' \n'])
			jogar = inicio(x)
			if(jogar == True):
				ganhou = True
			else:
				window.close()
		else:
			telalevel(pontos)
			
if(jogar == False):
	window.close()



print("---CALCULO DOS SALARIOS---\n")



#//INPUT DOS DADOS//
vendedor_1=float(input("Quanto Emily veendeu no mês:R$ "))

  
vendedor_2=float(input("Quanto Larissa vendeu no mês:R$ "))

  
vendedor_3=float(input("Quanto Rafael vendeu no mês:R$ "))


vendedor_4=float(input("Quanto Milena vendeu no mês:R$ "))

#//VARIAVEIS//
custo_operacao=6000

faturamento_total= (vendedor_1+vendedor_2+vendedor_3+vendedor_4)

#//CALCULO DE COMISSÃO DOS VENDEDORES//
comissao_1_emily=vendedor_1*1/100+1000
comissao_2_emily=vendedor_1*1.5/100+1000
comissao_3_emily=vendedor_1*2/100+1000

comissao_1_larissa=vendedor_2*1/100+1000
comissao_2_larissa=vendedor_2*1.5/100+1000
comissao_3_larissa=vendedor_2*2/100+1000

comissao_1_rafael=vendedor_3*1/100+1000
comissao_2_rafael=vendedor_3*1.5/100+1000
comissao_3_rafael=vendedor_3*2/100+1000

comissao_1_milena=vendedor_4*1/100+1000
comissao_2_milena=vendedor_4*1.5/100+1000
comissao_3_milena=vendedor_4*2/100+1000

#VARIAVEIS DOS SALAÁRIOS
salario_vendedor=1000
salario_gerente=2000+(faturamento_total*0.5)/100

#//salario total--USEI ESSA ESTRUTURA DE IF ELIF PARA PODER SETAR AS VARIAVEIS DE FORMA CORRETA PARA QUE NA LISTA, OS VALORES PUDESSEM SEREM SOMADOS JÁ CALCULADOS, COM OS DESCONTOS IMBUTIDOS
if vendedor_1<5000:
  vendedor_1=vendedor_1*0.1+1000
elif vendedor_1>=5000:  vendedor_1=vendedor_1*0.15+1000
elif vendedor_1>10000:  vendedor_1=vendedor_1*0.2+1000
if vendedor_2<5000:
  vendedor_2=vendedor_2*0.1+1000
elif vendedor_2>=5000:  vendedor_2=vendedor_2*0.15+1000
elif vendedor_2>10000:  vendedor_2=vendedor_2*0.2+1000
if vendedor_3<5000:
  vendedor_3=vendedor_3*0.1+1000
elif vendedor_3>=5000:  vendedor_3=vendedor_3*0.15+1000
elif vendedor_3>10000:  vendedor_3=vendedor_3*0.2+1000
if vendedor_4<5000:
  vendedor_4=vendedor_4*0.1+1000
elif vendedor_4>=5000:  vendedor_4=vendedor_4*0.15+1000
elif vendedor_4>10000:  vendedor_4=vendedor_4*0.2+1000
print("\n---SALARIOS---\n")
print("Faturamento_total....:R$",faturamento_total)


#//SALARIO EMILY
if vendedor_1<=5000:
  vendedor_1=comissao_1_emily
  print(".Emily....:R$",comissao_1_emily)
elif vendedor_1>=5000: 
  print(".Emily....:R$",comissao_2_emily)
elif vendedor_1<=10000:
  print(".Emily....:R$",comissao_2_emily)
elif vendedor_1>10000:
  print(".Emily....:R$",comissao_3_emily)
else:
  print(".Emily....:R$",salario_vendedor)
  
#//SALARIO LARISSA
if vendedor_2<=5000:
  vendedor_2=comissao_1_larissa 
  print(".Larissa....:R$",comissao_1_larissa)
elif vendedor_2>=5000: 
  print(".Larissa....:R$",comissao_2_larissa)
elif vendedor_2<=10000:
  print(".Larissa....:R$",comissao_2_larissa)
elif vendedor_2>10000:
  print(".Larissa....:R$",comissao_1_larissa)
else:
  print(".Larissa....:R$",salario_vendedor)
  
#//SALARIO RAFAEL
if vendedor_3<=5000:
  vendedor_3=comissao_1_rafael
  print(".Rafael....:R$",comissao_1_rafael)
elif vendedor_3>=5000: 
  print(".Rafael....:R$",comissao_2_rafael)
elif vendedor_3<=10000:
  print(".Rafael....:R$",comissao_2_rafael)
elif vendedor_3>10000:
  print(".Rafael....:R$",comissao_3_rafael)
else:
  print(".Rafael....:R$",salario_vendedor)
  
#//SALARIO MILENA
if vendedor_4<=5000:
  vendedor_4=comissao_1_milena
  print(".Milena....:R$",comissao_1_milena)
elif vendedor_4>=5000: 
  print(".Milena....:R$",comissao_2_milena)
elif vendedor_4<=10000:
  print(".Milena....:R$",comissao_2_milena)
elif vendedor_4>10000:
  print(".Milena....:R$",comissao_3_milena)
else:
  print(".Milena....:R$",salario_vendedor)
print("Gerente....:R$",salario_gerente)

salarios= [vendedor_1,vendedor_2,vendedor_3,vendedor_4,salario_gerente]
soma_dos_salarios=sum(salarios)
#print("salarios",salarios)
print("SALARIOS: ",soma_dos_salarios)

#/CUSTO DA OPERACAO
print("Custo de Operação....:R$",custo_operacao)
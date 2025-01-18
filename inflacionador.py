bruto=float(input('qual o salario desse mes?:'))
agua=float(input('quanto paga na agua?:'))
luz=float(input('e na luz?:'))
cartao=float(input('quanto paga no cartão?:'))
fundopessoal=float(input('quanto precisa para gastos pessoais?:'))
liquido=(bruto-agua-luz-cartao-fundopessoal)
rporcent=0.40
rfixa=(liquido*rporcent)
fporcent=0.30
fimobiliario=(liquido*fporcent)
acoesporcent=0.20
acoes=(liquido*acoesporcent)
reservaporcent=0.10
reservaoportu=(liquido*reservaporcent)
print('renda fixa: ',+rfixa, '\nfundos imobiliarios: ',+fimobiliario, '\nações: ',+acoes,'\nreserva de oportunidade: ',+reservaoportu)
print('valor total dos investimentos: ',+ liquido)
contas=(agua+luz+cartao+fundopessoal)
print("valor das contas",+contas)
input('pressione enter para sair')
expre = str(input('Digite uma expressão: '))
pilha = []
for simb in expre:
    if simb == '(':
      pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
           pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
   print('A expressão está válida!')   
else:
   print('A expressão está inválida!')   





















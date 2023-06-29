
# O DESAFIO DO DIA 02
# Faça um programa que leia o valor de uma conta corrente e o valor da gorjeta
# e calcule o valor total da conta com a gorjeta aplicada.

# EXEMPLO:
# Qual o valor total da conta? 124.56
# Quanta gorjeta você gostaria de dar? 10, 12 ou 15?
# Quantas pessoas para dividir a conta? 7
# Cada pessoa deve pagar: R$ 19.93
# O valor total da conta é: R$ 139.51
# O valor da gorjeta é: R$ 14.95
# O valor da gorjeta por pessoa é: R$ 2.14







# SOLUÇÃO

print("### Bem-vindo à calculadora de gorjetas! ### \n")
bill = float(input("Qual o valor total da conta? \n R$  "))
tip = int(input("Quanta gorjeta você gostaria de dar? 10%, 12% ou 15%? \n"))
people = int(input("Quantas pessoas para dividir a conta? \n"))



tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print("### Resultados ### \n")
print(f"Cada pessoa deve pagar: R$ {bill_per_person}")
print(f"O valor total da conta é: R$ {total_bill}")



print(f"Cada pessoa deve pagar: R$ {final_amount}")
print(f"O valor total da conta é: R$ {total_bill}")
print(f"O valor da gorjeta é: R$ {total_tip_amount}")
print(f"O valor da gorjeta por pessoa é: R$ {round(total_tip_amount / people, 2)}")


# EXPLICAÇÃO:

# 1. Imprimir uma saudação inicial
# 2. Pegar o valor total da conta
# 3. Quanta gorjeta você gostaria de dar? 10%, 12% ou 15%?
# 4. Quantas pessoas para dividir a conta?
# 5. Calcular a gorjeta
# 6. Calcular o valor total da conta
# 7. Calcular o valor da conta por pessoa
# 8. Imprimir o valor da conta por pessoa
# 9. Imprimir o valor total da conta
# 10. Imprimir o valor da gorjeta
# 11. Imprimir o valor da gorjeta por pessoa




#Projeto Desenvolvido por: jB Oliveira para o segundo dia dos #100DaysOfPython
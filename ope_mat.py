# Vamos solicitar como entrada dois numeros e depois vamos realizar uma operação 

num1= int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))

opreção= input("Digite a operação desejada (+, -, *, /): ")

if opreção == "+":
    resultado= num1 + num2
elif opreção == "-":
    resultado = abs(num1 - num2)
elif opreção == "*":
    resultado= num1 * num2
elif opreção == "/":
    resultado= num1 / num2
elif opreção == "%":
    resultado= num1 % num2
elif opreção == "**":
    resultado= num1 ** num2
elif opreção == "//":
    resultado= num1 // num2
else:
    resultado= "Operação inválida"
print(f"Resultado: {resultado}")
#
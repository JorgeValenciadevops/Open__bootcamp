
height = float(input('Enter your height in mtrs '))
weight = float(input('Enter your weight in kg '))

imc = round((weight / height**2), 2)

print('Your IMC is ', str(imc))

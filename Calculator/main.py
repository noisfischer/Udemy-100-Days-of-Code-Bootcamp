def add(n1, n2):
  """Adds and returns your two inputs"""
  return n1 + n2

def subtract(n1, n2):
  """Subtracts and returns your two inputs"""
  return n1 - n2

def multiply(n1, n2):
  """Multiplies and returns your two inputs"""
  return n1 * n2

def divide(n1, n2):
  """Divides and returns your two inputs"""
  return n1 / n2

  
# Create a dictionary that uses the symbols + - * / as keys and the names of the above functions as their values
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}


def calculator():
  num1 = float(input("What's the first number?: "))
  
  for x in operations:
      print(f"\n{x}")
  
  cont_calc = 'y'
  
  while cont_calc == 'y':
    
    operation_selection = input("\nPick an operation: ")
    num2 = float(input("\nWhat's the next number?: "))
    calculation_function = operations[operation_selection]
    answer = calculation_function(num1, num2)
    print(f"\n{num1} {operation_selection} {num2} = {answer}")
  
    num1 = answer
    
    cont_calc = input("Type 'y' to make another calculation or 'n' to start a new calculation: ")

    if cont_calc == 'n':
      calculator()

calculator()


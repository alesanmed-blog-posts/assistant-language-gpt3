# Assistant Language interpreter in Python

import re

def interpreter(code):
  # Split code into lines
  lines = code.split("\n")

  # Loop through lines of code
  for line in lines:
    # Parse line of code
    match = re.match(r"(\w+):?\s*(.*)", line)
    if match:
      keyword = match.group(1)
      value = match.group(2)

      # Execute line of code
      if keyword == "let":
        # Define variable
        name, _, val = value.partition("=")
        globals()[name.strip()] = eval(val.strip())
      elif keyword == "print":
        # Print value to screen
        print(eval(value))
      elif keyword == "if":
        # Evaluate condition
        cond, _, block = value.partition("{")
        if eval(cond.strip()):
          # Execute code block
          interpreter(block)
      elif keyword == "while":
        # Evaluate condition
        cond, _, block = value.partition("{")
        while eval(cond.strip()):
          # Execute code block
          interpreter(block)
      elif keyword == "function":
        # Define function
        name, _, block = value.partition("{")
        globals()[name.strip()] = lambda: interpreter(block)

# Example code
code = """
let myVariable = 10

function greet(name) {
  print: "Hello, " + name
}

if (myVariable > 5) {
  greet("Assistant")
}
"""

interpreter(code)

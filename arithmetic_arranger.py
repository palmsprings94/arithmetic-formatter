def arithmetic_arranger(pro, solve):
  
  x = ""
  y = ""
  line = ""
  z = ""
  
  for i in pro:
    
    if len(pro) > 5:
      return print("Error: Too many problems.")
      
    if "+" in i:
      opepos = i.find("+")
      oper = "+"
    elif "-" in i:
      opepos = i.find("-")
      oper = "-"
    elif "*" in i:
      return print("Error: Operator must be '+' or '-'.")
    elif "/" in i:
      return print("Error: Operator must be '+' or '-'.")

    a = i[0: opepos - 1]
    b = i[opepos + 2:]

    if len(a) > 4 or len(b) > 4:
      return print("Error: Numbers cannot be more than four digits.")
    if a.isdigit() is False or a.isdigit is False:
      return print("Error: Numbers must only contain digits.")

    aint = int(a)
    bint = int(b)

    if oper == "+":
      cint = aint + bint
    elif oper == "-":
      cint = aint - bint

    c = str(cint)
    secline = oper + b.rjust((max(len(a), len(b)) + 1), " ")
    x = x + a.rjust(len(secline), " ") + "    "
    y = y + secline + "    "
    line = line + "_" * len(secline) + "    "
    z = z + (c.rjust(len(secline), " ")) + "    "
  
  if solve is False:
    print(x)
    print(y)
    print(line)
  elif solve is True:
    print(x)
    print(y)
    print(line)
    print(z)

arithmetic_arranger(["32 + 8", "1 - 3201", "9999 + 9999", "523 - 49"], True)

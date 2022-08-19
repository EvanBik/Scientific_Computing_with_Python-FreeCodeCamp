def calculator(num1,num2,op):
	len1 = len(num1)
	len2 = len(num2)
	span = max(len1,len2) + 2	
	r1 = num1.rjust(span)
	r2 = op + num2.rjust(span-1)
	r3 = "-"*span
	if op == "+":
		calc = str(int(num1) + int(num2))
	else:
		calc = str(int(num1) - int(num2))
	r4 = calc.rjust(span)
	return r1,r2,r3,r4

def arithmetic_arranger(problems,res=False):
	if len(problems)>5:
		return "Error: Too many problems."
	oper1 = []
	oper2 = []
	operator = []
	for p in problems:
		parts = p.split()
		oper1.append(parts[0])
		oper2.append(parts[2])
		operator.append(parts[1])
	if "*" in operator or "/" in operator:
		return "Error: Operator must be '+' or '-'."
	for i in range(len(problems)):
		if not(oper1[i].isdigit() and oper2[i].isdigit()):
			return "Error: Numbers must only contain digits."
	for i in range(len(problems)):	
		if len(oper1[i])>4 or len(oper2[i])>4:
			return "Error: Numbers cannot be more than four digits."
	line1 = []
	line2 = []
	line3 = []
	line4 = []
	for i in range(len(problems)):
		x = calculator(oper1[i],oper2[i],operator[i])
		line1.append(x[0])
		line2.append(x[1])
		line3.append(x[2])
		line4.append(x[3])
	if res:
		arranged_problems = "    ".join(line1)+"\n"+"    ".join(line2)+"\n"+"    ".join(line3)+"\n"+"    ".join(line4)
	else:
		arranged_problems = "    ".join(line1)+"\n"+"    ".join(line2)+"\n"+"    ".join(line3)
	return arranged_problems
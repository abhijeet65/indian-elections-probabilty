pos_count=0
neg_count=0
no_of_lines=0
file=open("output.txt","r")
for line in file:
	line1=line.split()
	if "positive" in line1:
		pos_count=pos_count+1
	elif "negative" in line1:
		neg_count=neg_count+1
	no_of_lines=no_of_lines+1
print(no_of_lines)
print(pos_count)
print("Probability of victory: ",float(pos_count/no_of_lines))

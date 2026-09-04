new_lines=[]
with open("customer.txt","r") as file:
    for line in file:
        print(line)
        if "Customer support was helpful" in line:
            continue
        new_lines.append(line.strip())
print(new_lines)

with open("customer.txt","w") as file:
    file.writelines(new_lines)   
    
print("filtered data has written in file")
        
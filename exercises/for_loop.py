details =[{"name":"vikram","age":27},
          {"name":"ravi","age":25},
          {"name":"vikram","age":25}]

# print(details[0])
c_vik = 0;
c_other =0;
for i in range(len(details)):
    # print(details[i])
    if details[i]["name"] =="vikram":
         c_vik=c_vik+1;
    else:
        c_other=c_other+1;
print(f"count of vikram is {c_vik} \n and other is {c_other}")
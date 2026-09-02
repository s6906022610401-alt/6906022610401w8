import struct
num_r = int(input("how man records do you want to create ? "))
with open("records.bin","wb") as file:
    for _ in range(num_r):
        id_n = int(input("enter id : "))
        name = input("enter name : ")
        age = int(input("enter age : "))
        gpa = float(input("enter gpa : "))

        data = struct.pack('i20sif',id_n,name.encode(),age,gpa)
        file.write(data)
print(f"{num_r} records have been written to records.bin")
        
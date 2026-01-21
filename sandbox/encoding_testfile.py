demo_sting = 'hello_world'
bytes = demo_sting.encode(encoding='UTF-8')
print(bytes)
reg_bytes = bytes.decode("ASCII")
if reg_bytes == demo_sting:
    print(f"Decoded: {reg_bytes}")

else:
    print("Not encoded")   
    print(reg_bytes) 
    print(demo_sting)
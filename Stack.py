stack=[]
#Push elemen ke stack
stack.append(10)
stack.append(20)
stack.append(30)
print ("stack setelah push:",stack)

#Pop elemen dari stack
elemen = stack.pop()
print("Elemen yang di-pop:",elemen)
print ("Stelemen ack setelah pop:", stack )

#Peek elemen teratas
if stack:
    print("Elemen teratas:",stack[-1])
else:
    print ("Stack kosong")

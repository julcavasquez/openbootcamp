# Para los números entre 10 y 500, expresar en un diccionario el número y su respectivo 
# dígito más alto por el cuál es divisible. Por ejemplo para 328 es 8.

#solucion 1
# diccionario = {}
# for i in range(10,501):
#     divisores = []
#     for j in range(1,9):
#         if i % j == 0:
#             divisores.append(j)
#     diccionario[i]=max(divisores)
# print(diccionario)

#solucion 2
diccionario = {}
for num in range(10,50):    
    for i in str(num):
        print(i)
        print("*") 
        
print(diccionario)
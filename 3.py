#4 у кроликов  и 2 у гусей #
print("Всего лап 64")
print("Только Гуси: ",64/4)
print("Только Кролики: ",64/2)
print("Гуси и Кролики пополам все сочетания:")
c =0
for g in range(0,33):
    for k in range(0,33):
        if (2*g+4*k ==64):
            print(f"Гуси: {g}, Кролики: {k}")
            c+=1
print("Гуси и Кролики пополам все сочетания: ",c)           

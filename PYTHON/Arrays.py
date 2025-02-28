heros=['spider man','thor','hulk','iron man','captain america']
l=len(heros)
print("1. ",l)
heros.append("Black Panther")
print("2. ",heros)
heros.remove('Black Panther')
print(heros)
heros.insert(2,'BlackPanther')
print("3. ",heros)
heros[1:3]=['doctor strange']
print("4. ",heros)
heros.sort()
print("5. ",heros)
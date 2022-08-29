# Jack bought 400 hot dogs for the school picnic. If they were contained in packages of 8 hot dogs, how many
# total packages did he buy? Create a python program without using \ or % operator.

totalhd = int(input("No. of Hot Dogs bought: "))
hdperpackage = int(input("No. of Hot Dogs per package: "))
totalpackages = 0
while(totalhd >= hdperpackage):
    totalhd -= hdperpackage
    totalpackages += 1
    
print(f"Jack bought total {totalpackages} containers.")

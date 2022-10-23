import numpy as np

n_components = int(input("Enter number of components: "))
sposob = int(input( "Rations of values given by weight (enter 1), volume(enter 2) or by amount of substance in the mixture(enter 3): "))
mol_mass = np.empty(n_components, dtype = float)
part = np.empty(n_components, dtype = float)
part_m = np.empty(n_components, dtype = float)
for i in range(n_components):
    mol_mass[i] = input("Enter the molar mass of the mixture component: ")
    part[i] = input("Enter the fraction of the chosen value content in the mixture: ")
total = 0.00
mixt_molar = 0.00
if (sposob == 2) or (sposob == 3):
    for i in range(n_components):
        total += part[i]
    for i in range(n_components):
        mixt_molar += mol_mass[i]*part[i]/total

elif (sposob == 1):
    totalm = 0.00
    for i in range(n_components):
        part_m[i] = part[i]/mol_mass[i]
        totalm += part_m[i]
        #print(part_m[i])
        #print(totalm)

mixt_molar = 1/totalm
print("Molar mass of mixture is:\n", mixt_molar)
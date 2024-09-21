import numpy as np
import matplotlib.pyplot as plt

x_min = 0
x_max = 2
k_points = 1000
dx = (x_max - x_min)/k_points

def phi(psi, E, k):
    return psi[k]*(1+(1/6)*(dx**2)*E)

def integrate(psi, dx):
    res = 0
    for k in range(0, k_points -1):
        res += dx*(psi[k] + psi[k+1])/2
    return res

def numerov(E, dx):
    psi = [0,1]
    for k in range(2,k_points):
        psi.append(0)
        psi[k] = (2*phi(psi, E, k-1) - phi(psi,E,k-2) - 2*(dx**2)*E*phi(psi,E,k-1))/((1+(1/6)*(dx**2)*E))
    norm = np.sqrt(integrate([y*y for y in psi], dx))
    psi = psi/norm 
    return psi

init_step = 0.00001
max_shoot_iter = 1e+10

def shoot(E,dx):
    energies = []
    psi = []
    energies.append(E)
    psi.append(numerov(E,dx))

    if psi[0][k_points-1] > 0:
        energies.append(E-init_step)
        psi.append(numerov(E - init_step,dx))
        if psi[1][k_points-1] < psi[0][k_points-1]:
            for i in range(1, int(max_shoot_iter)):
                energies.append(energies[i]- init_step)
                psi.append(numerov(energies[i]- init_step, dx))
                if psi[i+1][k_points-1] < 0:
                    break
                else:
                    continue
        else:
            for i in range(1,int(max_shoot_iter)):
                energies.append(energies[i]+ init_step)
                psi.append(numerov(energies[i]+ init_step, dx))
                if psi[i+1][k_points-1] < 0:
                    break
                else:
                    continue

    else:
        energies.append(E-init_step)
        psi.append(numerov(E - init_step,dx))
        if psi[1][k_points-1] < psi[0][k_points-1]:
            for i in range(1,max_shoot_iter):
                energies.append(energies[i]+ init_step)
                psi.append(numerov(energies[i]+ init_step, dx))
                if psi[i+1][k_points-1] < 0:
                    break
                else:
                    continue
        else:
            for i in range(1,max_shoot_iter):
                energies.append(energies[i]- init_step)
                psi.append(numerov(energies[i]- init_step, dx))
                if psi[i+1][k_points-1] < 0:
                    break
                else:
                    continue
            
    return [psi, energies]

max_bysec_step = 1e+8
conv_bysec_thm = 1e-18

def bysection(a, b):
    up_ext = a
    down_ext = b
    psi = []
    energies = []
    for i in range(0,int(max_bysec_step)):
        mid = (up_ext+down_ext)/2
        energies.append(mid)
        psi.append(numerov(mid,dx))
        if (psi[i][k_points - 1] > 0):
            up_ext = mid
        else:
            down_ext = mid
        if (i > 0) and (abs(energies[i] - energies[i-1]) < conv_bysec_thm):
            break
    
    return [psi, energies]
        

E = 5
x_axis = np.linspace(x_min, x_max, k_points)
[Functions_app, Energies_app] = shoot(E,dx)
[Functions, Energies] = bysection(Energies_app[len(Energies_app) - 1], Energies_app[len(Energies_app)-2])
plot = plt.plot(x_axis, Functions[len(Functions) - 1])
plt.grid(True)
plt.savefig("Eigenfunction.pdf")
plt.close()
plot2 = plt.plot(range(0,len(Energies)), Energies)
plt.grid(True)
plt.savefig("Energy.pdf")
plt.close()
eigenfunction = open("Eigenfunction.txt", 'w')
k = 0
for val in Functions[len(Functions) - 1]:
    eigenfunction.write(str(k) + " " + str(val) + '\n')
    k += 1
eigenfunction.close()
energy = open("Energies.txt", 'w')
iter = 0
for val in Energies_app:
    energy.write(str(iter) + " " + str(val) + '\n')
    iter += 1
energy.write('\n' + "Starting bysection:" + '\n' + '\n')
for val in Energies:
    energy.write(str(iter) + " " + str(val) + '\n')
    iter += 1
energy.close()
        

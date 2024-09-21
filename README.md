# 1d_box_shooting
Program that computes and plots an eigenfunction and the relative eigenvalue for a quantum particle in a 1 dimensional box

command to execute: python3 1d_box_shooting

First, the program starts shooting energies and trying numerov for each energy until it reaches two opposite values of the wave function in the right wall of the box. Of course there is a criterium in this process, the shooting will surely converge. In the source you can change the step (step) for the initial shooting. The greater the step, the less accurate the reached point will be (I am referring to the point at the right extremum of the box, so the boundary condition. Less accurate means less close to zero). After the shooting, bysection begins. You can choose the energy convergence criterium (conv_thm).

The first energy value (E) is crucial. The shooting starts from this value, the reached value of energy after shooting and bysection will be an energy (hopefully) not too far from E. So choosing E means choosing the eigenvalue and eigenfunction you want to compute and plot. If you don't know more or less the eigenvalue you want to compute (so you don't know which value of E to choose), don't compute with the conv_thm and step in the source of this repository, try a bigger step and conv_thm, than compute, and finally use the obtained energy value as E for a new calculation with smaller step and conv_thm.

In the repository also an example of calculation of the second eigenvalue and eigenfunction.

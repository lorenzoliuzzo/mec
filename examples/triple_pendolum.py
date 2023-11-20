from src.surfaces import parametrization, triple_pendolum 
from src.potentials import potential_energy, gravity
from src.lagrangian import lagrangian, evolve_lagrangian
from src.plotting import animate_3D_trajectory 
import numpy as np
from time import time

# setting the initial conditions
nbodies = 3
ndim = 2
mass = np.random.random(nbodies)
q = np.random.random((nbodies, ndim))
q_t = np.random.random((nbodies, ndim))

print("q", q.shape, q)
print("q_t", q_t.shape, q_t)
print("mass", mass.shape, mass)

# setting the constraint parametrization
constraint = parametrization(triple_pendolum, l1=3.0, l2=1.0, l3=2.0)

# setting the potential energy
g_pot = potential_energy(gravity, g=9.81)   

# calling the lagrangian function
L, eom = lagrangian(q, q_t, mass, potentials=[g_pot], constraint=constraint)
print("L", L)
print("eom", eom)

# evolving the lagrangian
t0 = 0.0
tmax = 5. * np.pi
npoints = 500
tspan = np.linspace(t0, tmax, npoints)

start = time()
positions, _ = evolve_lagrangian(tspan, q, q_t, mass, potentials=[g_pot], constraint=constraint)
print(f"Evolution finished in {time() - start}")

animate_3D_trajectory(tspan, positions, constraint)
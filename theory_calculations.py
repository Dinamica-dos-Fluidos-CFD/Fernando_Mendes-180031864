import math

#defining constant values
volume_flow = 0.0001
tube_diam = 40/1000
tube_radius = tube_diam/2
tube_length = 1
density = 0.997*1000
dynamic_viscosity = 0.89/1000
f = 0.042

#eqautions
avg_velocity = 4*volume_flow/(math.pi*(tube_diam)*(tube_diam))
reynolds = density*avg_velocity*tube_diam/dynamic_viscosity
pressure_loss_laminar = 8*dynamic_viscosity*tube_length*avg_velocity/((tube_radius)**2)
pressure_loss = f*tube_length*density*avg_velocity*avg_velocity/(2*tube_diam)

#print
print("Velocidade = {0}".format(avg_velocity))
print("Re = {0}".format(reynolds))
print("Queda de pressão = {0}".format(pressure_loss))

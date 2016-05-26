#-*- coding: UTF-8 -*-
######### Workload Trace Generator ###########

from simulator import app, os
from sortedcontainers import SortedListWithKey, SortedList
from random import randrange 
from random import uniform
from os import listdir
from os.path import isfile, join
import numpy as np
import warnings

warnings.simplefilter("error")

###### Definición de la clase VM ########

#Se define la clase que guardará la información de las máquinas virtuales
class VM:
    def __init__(self, V__cpu, V__ram, V__net, R__, SLA__, t__init, t__end):
        self.V__cpu = V__cpu
        self.V__ram = V__ram
        self.V__net = V__net
        self.U__cpu = U__cpu
        self.U__ram = U__ram
        self.U__net = U__net
        self.R__ = R__
        self.SLA__ = SLA__
        self.t__init = t__init
        self.t__end = t__end

#Se define la clase que guardará la información de los tipos de distribuciones
class DISTRIBUTION:
    def __init__(self, dtype, l, mu, sigma, f, t):
        self.dtype = dtype
        self.l = l #valor de lambda
        self.mu = mu #valor de mu
        self.sigma = sigma #valor de sigma
        self.f = f #valor inicial uniforme
        self.t = t #valor final uniforme    

def uniform_value(desde, hasta): #Probabilidad = Random
    if (type(desde) == int and type(hasta) ==  int) == True:
        if desde == hasta and desde > 0:
            return desde
        else:
            return randrange(desde, hasta)
    else: #Si el valor a escoger con la fdp Uniforme es flotante
        return '%.3f'%(uniform(desde, hasta))

def fdp_poisson(l, x):
    s = np.random.poisson(l, x)
    print ("cadena poisson", s)
    return (s)

def fdp_uniform(desde, hasta, longitud, flotante):
    s = np.random.uniform(desde, hasta, longitud)
    if not flotante:
        l = s.astype(int)
        return l
    return s.astype(float)

def fdp_normal(mu, sigma, longitud, uso):
    s = np.random.normal(mu, sigma, longitud) #se genera la normal
    abs(mu - np.mean(s)) < 0.01 #verificar la media y la varianza
    abs(sigma - np.std(s, ddof=1)) < 0.01
    l = []
    count1 = 0 #inicializamos los contadores
    count2 = 0
    for x in s:
        count1 = count1+1 #se cuenta la cantidad de resultados
        if x >=0:
            count2 = count2+1 #se cuentan los resultados positivos
            l.append(x) #se cargan los resultados positivos en l
    count3 = count1 - count2 #se restan los resultados para obtener la cantidad de negativos
    if(longitud < 50): 
        s = np.random.normal(mu, sigma, longitud*10) #debido a que puede no haber la cant. de positivos suficientes
    else: s = np.random.normal(mu, sigma, longitud) #se genera por segunda vez la normal
    n = []
    for x in s:
        if (x >= 0 and len(n) < count3 and count3 != 0): #se filtran los nuevos positivos de la normal
            n.append(x) #se cargan los resultados positivos en n
        elif (len(n) == count3 and count3 == 0):
            break
    m = n+l #se concatenan los resultados positivos
    print(m)
    if uso == 0:
        p = np.array(m)
        p = p.astype(int)
    elif uso == 1:
        p = np.around(np.array(m), decimals=2)
    return p

def dynamic_vms_creation(var, vm_id, desde, hasta, total, itime_vector, dist): #Se crean los tiempos de las VMs según la fdp escogida
    if(vm_id == 0): #Se escoge la distribución para la creación de VMs al iniciar
        if dist.dtype[var] == 0: #Se elige el tipo de distribución para el tiempo
            itime_vector = fdp_uniform(int(desde), int(hasta), total, 0)
        elif dist.dtype[var] == 1:
            l = dist.l[var]
            itime_vector = fdp_poisson(l, total)
        elif dist.dtype[var] == 2:
            mu = dist.mu[var]
            sigma = dist.sigma[var]
            itime_vector = fdp_normal(mu, sigma, total, 0)
    t__init = itime_vector[vm_id] #Se cargan los tiempos iniciales
    if t__init == int(hasta) - 1: 
        t__end = int(hasta)
        duracion_vm = t__end - t__init + 1
    else:
        t__end = uniform_value(int(desde), int(hasta))
        duracion_vm = t__end - t__init + 1
        while(t__init >= t__end and duracion_vm <=1 ): #Se escoge el tiempo final de ejecución de la VM
            t__end = uniform_value(int(desde), int(hasta))
            duracion_vm = t__end - t__init + 1
    return t__init, t__end, itime_vector

def vms_creation(desde, hasta, total, fdp, var):
    normal_array = []
    poisson_array = []
    print("vms creation",fdp[var])
    if fdp[var][0] == 0:
       t__init = uniform_value(fdp[var][1], fdp[var][2])
       t__end  = uniform_value(int(desde), int(hasta))
    if fdp[var][0] == 1: #Se elige un unico valor para la fdp poisson
       t__init = fdp_poisson(fdp[var][1], 10)
       t__init = t__init[0]
       for i in range(1, 9): #Si el valor de ejecucion inicial de Poisson es mayor que el tiempo final
           if(t__init >= int(hasta)):
               t__init = poisson_array[i]
           else:
               break
    if fdp[var][0] == 2: #Se elige un valor de los 2 generados para la fdp normal, debido que la normal no puede generar un solo valor
       normal_array = fdp_normal(fdp[var][1], fdp[var][2], 10, 0)
       t__init = normal_array[0]
       for i in range(1, 9):
           if(t__init >= int(hasta)):
               t__init = normal_array[i]
           else:
               break
    if t__init == int(hasta) - 1:
        t__end = int(hasta)
        duracion_vm = t__end - t__init + 1
    else:
        t__end = uniform_value(int(desde), int(hasta))
        duracion_vm = t__end - t__init + 1
        while(t__init >= t__end and duracion_vm <=1 ): #Se escoge el tiempo final de ejecución de la VM
            t__end = uniform_value(int(desde), int(hasta))
            duracion_vm = t__end - t__init + 1
    return t__init, t__end

def convert2binary(scenario):
    binary = format(scenario, '04b')
    band = str(binary)
    # print(band)
    return int(band[0]), int(band[1]), int(band[2]), int(band[3])

def resource_allocation(var, desde, hasta, total, requirements, dist, fdp):
    normal_array = []
    if requirements:
        if dist.dtype[var] == 0: #Se escoge la distribución para los recursos
            dist_requirements = fdp_uniform(int(desde), int(hasta), total, 0)
            vert_elas = randrange(1, 3) 
        elif dist.dtype[var] == 1:
            l =  dist.l[var]
            dist_requirements = fdp_poisson(l, total)
        elif dist.dtype[var] == 2:
            mu = dist.mu[var]
            sigma = dist.sigma[var]
            dist_requirements = fdp_normal(mu, sigma, total, 1)
    else:
        if fdp[var][0] == 1:
            l = fdp[var][1]
            dist_requirements = fdp_poisson(l, 1)
            dist_requirements = dist_requirements[0] 
        elif fdp[var][0] == 2:
            mu = fdp[var][1]
            sigma = fdp[var][2]
            normal_array = fdp_normal(mu, sigma, 10, 0)
            dist_requirements = normal_array[0]
        else:
            dist_requirements = uniform_value(int(desde), int(hasta))   
    return dist_requirements

def utilization(var, total, utilization, dist):
    if utilization:
        if dist.dtype[var] == 0: #Si la distribucion escogida para la utilizazion es igual a Uniforme
            if dist.f[var] == 0 and dist.t[var] == 0: #Si no se escogio ningun valor, elegir de 0 a 100
                aux = fdp_uniform(0, 1, total, 1)
                dist_utilization = (aux*100).astype(int)
            else: #Si se escogio un rango
                aux = fdp_uniform(int(dist.f[var]), int(dist.t[var]), total, 1)
                dist_utilization = (aux).astype(int)
        elif dist.dtype[var] == 1: #Si la distribucion escogida para la utilizacion es igual a Poisson
            l =  dist.l[var]
            dist_utilization = fdp_poisson(l, total)
            dist_utilization[dist_utilization > 100] = 100

        elif dist.dtype[var] == 2 and total != 1: #Si la distribucion escogida para la utilizacion es igual a la Normal
            mu = dist.mu[var]
            sigma = dist.sigma[var]
            aux = fdp_normal(mu, sigma, total, 1)
            dist_utilization = aux.astype(int)
            dist_utilization[dist_utilization > 100] = 100
        elif dist.dtype[var] == 2 and total == 1:
            dist_utilization = dist.mu[var]
    else:
        dist_utilization = 100
    return dist_utilization

def desglosar(instancia, service_id, dc_id, vm_id, dist_vcpu, dist_vram, dist_vnet, dist_ucpu, dist_uram, dist_unet, requirements_serv, utilization_serv, utilization_net):
        vm_requirements = []
        vm_requirements_total = []
        j=0
        for i in range(instancia.t__init, instancia.t__end+1): #t__end +1 para se ejecute en el total de tiempo establecido
            if requirements_serv:
                instancia.V__cpu = dist_vcpu[j]
                instancia.V__ram = dist_vram[j]
                instancia.V__net = dist_vnet[j] 
            else:
                instancia.V__cpu = dist_vcpu
                instancia.V__ram = dist_vram
                instancia.V__net = dist_vnet 
            if utilization_serv:
                instancia.U__cpu = dist_ucpu[j]
                instancia.U__ram = dist_uram[j]
            else:
                instancia.U__cpu = dist_ucpu
                instancia.U__ram = dist_uram
            if utilization_net:
                instancia.U__net = dist_unet[j]
            else:
                instancia.U__net = dist_unet
            vm_requirements = [i, service_id, dc_id, vm_id, instancia.V__cpu, instancia.V__ram, instancia.V__net, instancia.U__cpu, instancia.U__ram, instancia.U__net,  instancia.R__, instancia.SLA__, instancia.t__init, instancia.t__end]
            vm_requirements_total.append(vm_requirements)
            j = j + 1
        return (vm_requirements_total)

def create_instance(lista, vm_id, service_id, dc_id, vm_total, itime_vector, scenario, dist, fdp):
    instancia = VM
    instancia.R__ = uniform_value(float(lista[8]), float(lista[9]))
    instancia.SLA__ = uniform_value(int(lista[10]), int(lista[11]))
    requirements_serv, number_vms, utilization_net, utilization_serv = convert2binary(scenario)
    if not number_vms and vm_id == 0: # Si vm estatica
        instancia.t__init, instancia.t__end = vms_creation(lista[0], lista[1], vm_total, fdp, 6)
        duracion_vm = instancia.t__end - instancia.t__init + 1
    elif number_vms: #Si vm es dinamica
        instancia.t__init, instancia.t__end, itime_vector = dynamic_vms_creation(6, vm_id, lista[0], lista[1], vm_total, itime_vector, dist)
    duracion_vm = instancia.t__end - instancia.t__init + 1
    dist_vcpu = resource_allocation(0, lista[2], lista[3], duracion_vm, requirements_serv, dist, fdp)
    dist_vram = resource_allocation(1, lista[4], lista[5], duracion_vm, requirements_serv, dist, fdp)
    dist_vnet = resource_allocation(2, lista[6], lista[7], duracion_vm, requirements_serv, dist, fdp) ##Reservado para cuando se utilice con fdp's
    dist_ucpu = utilization(3, duracion_vm, utilization_serv, dist)
    dist_uram = utilization(4, duracion_vm, utilization_serv, dist)
    dist_unet = utilization(5, duracion_vm, utilization_net, dist)
    vm_requirements_total = desglosar(instancia, service_id, dc_id, vm_id, dist_vcpu, dist_vram, dist_vnet, dist_ucpu, dist_uram, dist_unet, requirements_serv, utilization_serv, utilization_net)
    return vm_requirements_total, itime_vector

def choose_distribution(opt, dist, fdp):
    requirements_serv, number_vms, utilization_net, utilization_serv = convert2binary(opt)
    if requirements_serv:
        #Se elige la distribucion para la eslaticidad vertical
        vcpu = fdp[0][0]
        if vcpu == 0:
            dist.dtype[0] = 0
            dist.f[0] = fdp[0][1]
            dist.t[0] = fdp[0][2]
        elif vcpu == 1:
            dist.dtype[0] = 1
            dist.l[0] = fdp[0][1]
        elif vcpu == 2:
            dist.dtype[0] = 2
            dist.mu[0] = fdp[0][1]
            dist.sigma[0] = fdp[0][2]
        #Se elige la distribucion para la eslaticidad vertical
        vram = fdp[1][0]
        if vram == 0:
            dist.dtype[1] = 0
            dist.f[1]= fdp[1][1]
            dist.t[1] = fdp[1][2]
        elif vram == 1:
            dist.dtype[1] = 1
            dist.l[1] = fdp[1][1]
        elif vram == 2:
            dist.dtype[1] = 2
            dist.mu[1] = fdp[1][1]
            dist.sigma[1] = fdp[1][2]
    if utilization_serv:
        #Se elige la distribucion para utilizacion de cpu
        ucpu = fdp[3][0]
        if ucpu == 0:
            dist.dtype[3] = 0
            dist.f[3] = fdp[3][1]
            dist.t[3] = fdp[3][2]
        elif ucpu == 1:
            dist.dtype[3] = 1
            dist.l[3] = fdp[3][1]
        elif ucpu == 2:
            dist.dtype[3] = 2
            dist.mu[3] = fdp[3][1]
            dist.sigma[3] = fdp[3][2]
        #Se elige la distribucion para utilizacion de ram
        uram = fdp[4][0]
        if uram == 0:
            dist.dtype[4] = 0     
            dist.f[4] = fdp[4][1]
            dist.t[4] = fdp[4][2]
        elif uram == 1:
            dist.dtype[4] = 1
            dist.l[4] = fdp[4][1]
        elif uram == 2:
            dist.dtype[4] = 2
            dist.mu[4] = fdp[4][1]
            dist.sigma[4] = fdp[4][2]
    if utilization_net:
        #Se elige la distribucion para utilizacion de red
        unet = fdp[5][0]
        if unet == 0:
            dist.dtype[5] = 0
            dist.f[5] = fdp[5][1]
            dist.t[5] = fdp[5][2]
        elif unet == 1:
            dist.dtype[5] = 1
            dist.l[5] = fdp[5][1]
        elif unet == 2:
            dist.dtype[5] = 2
            dist.mu[5] = fdp[5][1]
            dist.sigma[5] = fdp[5][2]
    if number_vms:
        #Se elige la distribucion para la eslaticidad horizontal
        mVM = fdp[6][0] 
        if mVM == 0:
            dist.dtype[6] = 0
            dist.f[6] = fdp[6][1]
            dist.t[6] = fdp[6][2]
        elif mVM == 1:
            dist.dtype[6] = 1
            dist.l[6] = fdp[6][1]
        elif mVM == 2:
            dist.dtype[6] = 2
            dist.mu[6] = fdp[6][1]
            dist.sigma[6] = fdp[6][2]
    return dist

def convertir(x):
   if '.' in x:
      return float(x)
   else:
      return int(x)

def sort_list(scenario):
   l = SortedListWithKey(key=lambda item: item[0])

   #leemos el archivo con los resultados finales
   aux = []
   archivo = os.path.join(app.config['RESULTS'])
   with open(archivo, 'r') as f:
      data = f.readlines()
      for line in data:
         item = line.split(',')
         item = [convertir(x) for x in item]
         l.add(item)

   # Imprimimos al archivo en la salida final
   save_path = os.path.join(app.config['OUT'])
   file = open(save_path, "w")
   file.write('###################################################################\n')
   file.write('#                         Escenario {}                             #\n'.format(scenario))
   file.write('###################################################################\n\n')
   file.write('#t,Sb,DCc,Vj,Vcpu,Vram,Vnet,Ucpu,Uram,Unet,R,SLA,tinit,tend\n')
   file.write('\n')
   for item in l:
      cadena = ','.join(map(str, item))
      file.write(cadena)
      file.write('\n')
   file.close()

def read_file(filename):
    data_file = os.path.join(app.config['UPLOAD_FOLDER'] + filename)
    with open(data_file, 'r') as f:
        data = f.readlines()
        aux_line = []
        aux = []
        sce_fdp = []
        fdp = [[0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0], [0,0,0]]
        fdp_aux = []
        for line in data:
            aux_line = line.split(", ")
            aux.append(aux_line) 
        sce_fdp = aux[0]
        print("fdp", sce_fdp) #Se cargan los valores para todos los fdp
        lista = aux[1] #Se cargan los valores generales
        scenario = sce_fdp[0] #Se carga el escenario escogido 
        for i in range(1,4): #Se cargan los valores de Vcpu
            fdp_aux.append(sce_fdp[i])
        if fdp_aux[0] == '1':
            fdp[0] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[0] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
        fdp_aux = []
        for i in range(4,7): #Se cargan los valores de Vram
            fdp_aux.append(sce_fdp[i])
        if fdp_aux[0] == '1':
            fdp[1] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[1] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
        fdp_aux = []
        for i in range(10,13): #Se cargan los valores de Ucpu
            fdp_aux.append(sce_fdp[i])
        if fdp_aux[0] == '0':
            fdp[3] = [int(fdp_aux[0]), int(fdp_aux[1]), int(fdp_aux[2])]
        elif fdp_aux[0] == '1':
            fdp[3] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[3] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
        fdp_aux = []
        for i in range(13,16): #Se cargan los valores de Uram
            fdp_aux.append(sce_fdp[i])
        if fdp_aux[0] == '0':
            fdp[4] = [int(fdp_aux[0]), int(fdp_aux[1]), int(fdp_aux[2])]
        elif fdp_aux[0] == '1':
            fdp[4] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[4] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
        fdp_aux = []
        for i in range(16,19): #Se cargan los valores de Unet
            fdp_aux.append(sce_fdp[i])
        print("fdp Unet = ",fdp_aux )
        if fdp_aux[0] == '0':
            fdp[5] = [int(fdp_aux[0]), int(fdp_aux[1]), int(fdp_aux[2])]
        elif fdp_aux[0] == '1':
            fdp[5] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[5] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
        fdp_aux = []
        for i in range(19,22): #Se cargan los valores de VM
            fdp_aux.append(sce_fdp[i])
        if fdp_aux[0] == '0':
            fdp[6] = [int(fdp_aux[0]), int(fdp_aux[1]), int(fdp_aux[2])]
        elif fdp_aux[0] == '1':
            fdp[6] = [int(fdp_aux[0]), int(fdp_aux[1])]
        elif fdp_aux[0] == '2':
            fdp[6] = [int(fdp_aux[0]), float(fdp_aux[1]), float(fdp_aux[2])]
    return lista, fdp, scenario


def generate_env(scenario, inputList, fdp, filename):
    if inputList == 0:
        lista, fdp, scenario = read_file(filename)
        print("escenario =", scenario)
        print("fdp =", fdp)
        print("Valores =", lista)
    else:
        lista = inputList
    save_path = os.path.join(app.config['RESULTS'])
    file = open(save_path, "w")
    time_vector = []
    dist = DISTRIBUTION
    dist.dtype = [0, 0, 0, 0, 0, 0, 0]
    dist.l = [0, 0, 0, 0, 0, 0, 0]
    dist.mu = [0, 0, 0, 0, 0, 0, 0]
    dist.sigma = [0, 0, 0, 0, 0, 0, 0]
    dist.f = [0, 0, 0, 0, 0, 0, 0]
    dist.t = [0, 0, 0, 0, 0, 0, 0]
    x = 0
    scenario = int(scenario)
    if scenario: 
        dist = choose_distribution(scenario, dist, fdp)
    print("                                     ::::::::::::::: Escenario {} :::::::::::::: ".format(scenario))
    z = uniform_value(int(lista[16]), int(lista[17])) #Se elige la cantidad de Data Centers a ser generados.
    for k in range(z):
       print('\n              ----------------------------------------')
       print('                             Data Center {}              '.format(k))
       print('              ----------------------------------------')
       y = uniform_value(int(lista[14]), int(lista[15])) #Se elige la cantidad de Servicios a ser generados.
       for j in range(y): #Imprime los servicios
           print ("\n   __________________ Servicio {} __________________\n".format(j)) #El servicio comienza a imprimir desde 0
           while x == 0: #mientras la cantidad de VMs a ser generadas sea igual a NINGUNA, se repite (en caso x = 0)
               x = uniform_value(int(lista[12]), int(lista[13])) #Se elige la cantidad de VMs a ser generadas.
               print("cantidad de maquinas virtuales", x)
           while dist.dtype[6] == 2 and x == 1:
               x = uniform_value(int(lista[12]), int(lista[13])) #Se elige la cant de VMs distintas de 1 p/ la distribución normal
           for i in range(x): #Itera los índices de VMs
              print ("\n------------- VM {} -------------".format(i)) # Imprime la máquina Virtual
              vm_requirements_final, time_vector = create_instance(lista, i, j, k, x, time_vector, scenario, dist, fdp)
              print("t-Sb-DCc-Vj-Vcpu-Vram-Vnet-Ucpu%-Uram%-Unet%-R-SLA-tinit-tend")
              for d in vm_requirements_final:
                 cadena = ', '.join(map(str, d))
                 print(cadena)
                 s = str(cadena)
                 file.write(s)
                 file.write('\n')
           x = 0 #Cera la cantidad de maquinas virtuales generadas para que se elija de nuevo para el siguiente servicio
    file.close()
    sort_list(scenario)




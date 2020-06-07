import os
from datetime import datetime
import re

fmt = '%H:%M:%S.%f'

id_completa = [
    '1330', '3094', '3113', '3161', '3858', '3988', '3989', '3993', '3994', '3997', '3998', '4000', '4003', '4005', '4006', '4007', '4009', '4060', '4062', '4065', '4082', '4083', '4085', '4123', '4127', '4129', '4136', '4137', '4138', '4139', '4140', '4144', '4145', '4147', '4148', '4149', '4151', '4152', '4155', '4159', '4160', '4161', '4172', '4175', '4176', '4179', '4180', '4182', '4183', '4188', '4189', '4190', '4191', '4272', '4311', '4312', '4327', '4330', '4348', '4350', '4354', '4357', '4363', '4368', '4369', '4370', '4375', '4377', '4379', '4380', '4382', '4384', '4385', '4444', '4446', '4476', '4478', '4480', '4491', '4496', '4500']

id_traducao = [
    '1165', '2171', '3119', '3135', '3396', '3555', '3812', '3851', '3960', '3985', '3986', '3987', '3992', '3995', '3999', '4001', '4002', '4004', '4008', '4011', '4012', '4013', '4014', '4057', '4058', '4059', '4061', '4066', '4067', '4073', '4078', '4079', '4080', '4124', '4125', '4126', '4128', '4130', '4131', '4132', '4134', '4135', '4143', '4146', '4150', '4153', '4154', '4157', '4162', '4163', '4165', '4170', '4171', '4173', '4174', '4177', '4178', '4181', '4184', '4185', '4187', '4192', '4193', '4194', '4271', '4310', '4322', '4342', '4345', '4347', '4349', '4351', '4352', '4358', '4366', '4367', '4372', '4413', '4414', '4422', '4424', '4427', '4429', '4431', '4432', '4443', '4464', '4469', '4470', '4472', '4477', '4479', '4481', '4482', '4485', '4487', '4501',
]

lista_traducao = []
my_file = 'slic.txt'
time_soma_total = 0
lista_erros = []

with open(my_file, 'r') as f:
    for line in f:
        if(line.startswith("sequencia")):
            a = line.split()
            lista_traducao.append(a)

        elif (line.split(" ")[1] in id_traducao):

            if 'dica_open' in line:
                erro = line.split("#")[-1].strip()
                time_open = line.split('#')[0]
                time_open_certo = time_open.split(" ")[3]
                time_open_certo = datetime.strptime(time_open_certo, fmt)
                print(erro)
                print(time_open_certo)

            elif 'dica_close' in line:
                time_close = line.split('#')[0]
                time_close_certo = time_close.split(" ")[3]
                time_close_certo = datetime.strptime(time_close_certo, fmt)
                time_total_parcial = (time_close_certo -
                                      time_open_certo).total_seconds()
                print(time_close_certo)
                print("###", time_total_parcial)
                if(time_total_parcial > 0):
                    time_soma_total = time_soma_total + time_total_parcial
                print(time_soma_total)

            a = line.split()
            lista_traducao.append(a)

with open('saida_traducao.txt', 'w') as f2:
    for item in lista_traducao:
        f2.write("%s\n" % item)

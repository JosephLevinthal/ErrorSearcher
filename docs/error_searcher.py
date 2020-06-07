import os
from datetime import datetime
import re

fmt = '%H:%M:%S.%f'

id_completa = [  # 82 alunos
    '1330', '3094', '3113', '3161', '3858', '3988', '3989', '3993', '3994', '3997', '3998', '4000', '4003', '4005', '4006', '4007', '4009', '4060', '4062', '4065', '4082', '4083', '4085', '4123', '4127', '4129', '4136', '4137', '4138', '4139', '4140', '4144', '4145', '4147', '4148', '4149', '4151', '4152', '4155', '4159', '4160', '4161', '4172', '4175', '4176', '4179', '4180', '4182', '4183', '4188', '4189', '4190', '4191', '4272', '4311', '4312', '4327', '4330', '4348', '4350', '4354', '4357', '4363', '4368', '4369', '4370', '4375', '4377', '4379', '4380', '4382', '4384', '4385', '4444', '4446', '4476', '4478', '4480', '4491', '4496', '4500']

id_traducao = [  # 97 alunos
    '1165', '2171', '3119', '3135', '3396', '3555', '3812', '3851', '3960', '3985', '3986', '3987', '3992', '3995', '3999', '4001', '4002', '4004', '4008', '4011', '4012', '4013', '4014', '4057', '4058', '4059', '4061', '4066', '4067', '4073', '4078', '4079', '4080', '4124', '4125', '4126', '4128', '4130', '4131', '4132', '4134', '4135', '4143', '4146', '4150', '4153', '4154', '4157', '4162', '4163', '4165', '4170', '4171', '4173', '4174', '4177', '4178', '4181', '4184', '4185', '4187', '4192', '4193', '4194', '4271', '4310', '4322', '4342', '4345', '4347', '4349', '4351', '4352', '4358', '4366', '4367', '4372', '4413', '4414', '4422', '4424', '4427', '4429', '4431', '4432', '4443', '4464', '4469', '4470', '4472', '4477', '4479', '4481', '4482', '4485', '4487', '4501',
]

my_file = 'saida.txt'
time_final_da_dica = 0
time_soma_total = 0
quantidade_erros_TOTAL = 0
lista_traducao = []

# Creating variables for quantity and number of occurences of each error
# --------------------------------------
SyntaxErrorInvalid_quantidade = 0
SyntaxErrorInvalid_tempo = 0

NameError_quantidade = 0
NameError_tempo = 0

SyntaxErrorUnexpected_quantidade = 0
SyntaxErrorUnexpected_tempo = 0

IndentationErrorBlock_quantidade = 0
IndentationErrorBlock_tempo = 0

IndentationErrorUnexpected_quantidade = 0
IndentationErrorUnexpected_tempo = 0

IndentationErrorUnindent_quantidade = 0
IndentationErrorUnindent_tempo = 0

TabErrorInconsistent_quantidade = 0
TabErrorInconsistent_tempo = 0

ValueErrorInvalid_quantidade = 0
ValueErrorInvalid_tempo = 0

TypeErrorUnsuported_quantidade = 0
TypeErrorUnsuported_tempo = 0

TypeErrorCant_quantidade = 0
TypeErrorCant_tempo = 0

IndexErrorIndex_quantidade = 0
IndexErrorIndex_tempo = 0

ZeroDivisionErrorDivision_quantidade = 0
ZeroDivisionErrorDivision_tempo = 0

ZeroDivisionErrorFloat_quantidade = 0
ZeroDivisionErrorFloat_tempo = 0
# --------------------------------------
SyntaxErrorInvalid_quantidade_ERROS = 0
NameError_quantidade_ERROS = 0
SyntaxErrorUnexpected_quantidade_ERROS = 0
IndentationErrorBlock_quantidade_ERROS = 0
IndentationErrorUnexpected_quantidade_ERROS = 0
IndentationErrorUnindent_quantidade_ERROS = 0
TabErrorInconsistent_quantidade_ERROS = 0
ValueErrorInvalid_quantidade_ERROS = 0
TypeErrorUnsuported_quantidade_ERROS = 0
TypeErrorCant_quantidade_ERROS = 0
IndexErrorIndex_quantidade_ERROS = 0
ZeroDivisionErrorDivision_quantidade_ERROS = 0
ZeroDivisionErrorFloat_quantidade_ERROS = 0
# --------------------------------------

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

                if(time_final_da_dica > 0):
                    time_soma_total = time_soma_total + time_final_da_dica
                    print("Tempo de leitura dessa dica: ", time_final_da_dica)

                    if('SyntaxError: invalid syntax' in line):
                        SyntaxErrorInvalid_quantidade = SyntaxErrorInvalid_quantidade + 1
                        SyntaxErrorInvalid_tempo = SyntaxErrorInvalid_tempo + time_final_da_dica

                    elif('NameError: name' in line):
                        NameError_quantidade = NameError_quantidade + 1
                        NameError_tempo = NameError_tempo + time_final_da_dica

                    elif('SyntaxError: unexpected EOF while parsing' in line):
                        SyntaxErrorUnexpected_quantidade = SyntaxErrorUnexpected_quantidade + 1
                        SyntaxErrorUnexpected_tempo = SyntaxErrorUnexpected_tempo + time_final_da_dica

                    elif('IndentationError: expected an indented block' in line):
                        IndentationErrorBlock_quantidade = IndentationErrorBlock_quantidade + 1
                        IndentationErrorBlock_tempo = IndentationErrorBlock_tempo + time_final_da_dica

                    elif('IndentationError: unexpected indent' in line):
                        IndentationErrorUnexpected_quantidade = IndentationErrorUnexpected_quantidade + 1
                        IndentationErrorUnexpected_tempo = IndentationErrorUnexpected_tempo + time_final_da_dica

                    elif('IndentationError: unindent' in line):
                        IndentationErrorUnindent_quantidade = IndentationErrorUnindent_quantidade + 1
                        IndentationErrorUnindent_tempo = IndentationErrorUnindent_tempo + time_final_da_dica

                    elif('TabError: inconsistent use' in line):
                        TabErrorInconsistent_quantidade = TabErrorInconsistent_quantidade + 1
                        TabErrorInconsistent_tempo = TabErrorInconsistent_tempo + time_final_da_dica

                    elif('ValueError: invalid literal for int() with base 10' in line):
                        ValueErrorInvalid_quantidade = ValueErrorInvalid_quantidade + 1
                        ValueErrorInvalid_tempo = ValueErrorInvalid_tempo + time_final_da_dica

                    elif('TypeError: unsupported operand type' in line):
                        TypeErrorUnsuported_quantidade = TypeErrorUnsuported_quantidade + 1
                        TypeErrorUnsuported_tempo = TypeErrorUnsuported_tempo + time_final_da_dica

                    elif('TypeError: can' in line):
                        TypeErrorCant_quantidade = TypeErrorCant_quantidade + 1
                        TypeErrorCant_tempo = TypeErrorCant_tempo + time_final_da_dica

                    elif('IndexError: index' in line):
                        IndexErrorIndex_quantidade = IndexErrorIndex_quantidade + 1
                        IndexErrorIndex_tempo = IndexErrorIndex_tempo + time_final_da_dica

                    elif('ZeroDivisionError: division by zero' in line):
                        ZeroDivisionErrorDivision_quantidade = ZeroDivisionErrorDivision_quantidade + 1
                        ZeroDivisionErrorDivision_tempo = ZeroDivisionErrorDivision_tempo + time_final_da_dica

                    elif('ZeroDivisionError: float division by zero' in line):
                        ZeroDivisionErrorFloat_quantidade = ZeroDivisionErrorFloat_quantidade + 1
                        ZeroDivisionErrorFloat_tempo = ZeroDivisionErrorFloat_tempo + time_final_da_dica

                    time_final_da_dica = 0

            elif 'dica_close' in line:
                time_close = line.split('#')[0]
                time_close_certo = time_close.split(" ")[3]
                time_close_certo = datetime.strptime(time_close_certo, fmt)
                time_final_da_dica = (
                    time_close_certo - time_open_certo).total_seconds()

            elif 'saida_testar' in line:
                if('SyntaxError: invalid syntax' in line):
                    SyntaxErrorInvalid_quantidade_ERROS = SyntaxErrorInvalid_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('NameError: name' in line):
                    NameError_quantidade_ERROS = NameError_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('SyntaxError: unexpected EOF while parsing' in line):
                    SyntaxErrorUnexpected_quantidade_ERROS = SyntaxErrorUnexpected_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('IndentationError: expected an indented block' in line):
                    IndentationErrorBlock_quantidade_ERROS = IndentationErrorBlock_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('IndentationError: unexpected indent' in line):
                    IndentationErrorUnexpected_quantidade_ERROS = IndentationErrorUnexpected_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('IndentationError: unindent' in line):
                    IndentationErrorUnindent_quantidade_ERROS = IndentationErrorUnindent_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('TabError: inconsistent use' in line):
                    TabErrorInconsistent_quantidade_ERROS = TabErrorInconsistent_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('ValueError: invalid literal for int() with base 10' in line):
                    ValueErrorInvalid_quantidade_ERROS = ValueErrorInvalid_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('TypeError: unsupported operand type' in line):
                    TypeErrorUnsuported_quantidade_ERROS = TypeErrorUnsuported_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('TypeError: can' in line):
                    TypeErrorCant_quantidade_ERROS = TypeErrorCant_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('IndexError: index' in line):
                    IndexErrorIndex_quantidade_ERROS = IndexErrorIndex_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('ZeroDivisionError: division by zero' in line):
                    ZeroDivisionErrorDivision_quantidade_ERROS = ZeroDivisionErrorDivision_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

                elif('ZeroDivisionError: float division by zero' in line):
                    ZeroDivisionErrorFloat_quantidade_ERROS = ZeroDivisionErrorFloat_quantidade_ERROS + 1
                    quantidade_erros_TOTAL = quantidade_erros_TOTAL + 1

            a = line.split()
            lista_traducao.append(a)

    print('\n')
    print("Soma total do tempo das dicas(em segundos): ", time_soma_total)
    print("Quantidade total de erros do grupo controle: ", quantidade_erros_TOTAL)
    print("Quantidade de erros do grupo controle / número de alunos do grupo controle: ",
          (quantidade_erros_TOTAL/97))
    print('\n')

# Prints para o relatório final dos tempos
print('SyntaxErrorInvalid_quantidade_ERROS: ',
      SyntaxErrorInvalid_quantidade_ERROS)
print("Aberturas de dicas - SyntaxErrorInvalid: ",
      SyntaxErrorInvalid_quantidade)
print("SyntaxErrorInvalid_tempo: ",
      SyntaxErrorInvalid_tempo)
print('\n')

print("NameError_quantidade_ERROS: ", NameError_quantidade_ERROS)
print("Aberturas de dicas - NameError_quantidade: ", NameError_quantidade)
print("NameError_tempo: ", NameError_tempo)
print('\n')

print("SyntaxErrorUnexpected_quantidade_ERROS: ",
      SyntaxErrorUnexpected_quantidade_ERROS)
print("Aberturas de dicas - SyntaxErrorUnexpected: ",
      SyntaxErrorUnexpected_quantidade)
print("SyntaxErrorUnexpected_tempo: ", SyntaxErrorUnexpected_tempo)
print('\n')

print("IndentationErrorBlock_quantidade_ERROS: ",
      IndentationErrorBlock_quantidade_ERROS)
print("Aberturas de dicas - IndentationErrorBlock: ",
      IndentationErrorBlock_quantidade)
print("IndentationErrorBlock_tempo: ", IndentationErrorBlock_tempo)
print('\n')

print("IndentationErrorUnexpected_quantidade_ERROS: ",
      IndentationErrorUnexpected_quantidade_ERROS)
print("Aberturas de dicas - IndentationErrorUnexpected: ",
      IndentationErrorUnexpected_quantidade)
print("IndentationErrorUnexpected_tempo: ",
      IndentationErrorUnexpected_tempo)
print('\n')

print("IndentationErrorUnindent_quantidade_ERROS: ",
      IndentationErrorUnindent_quantidade_ERROS)
print("Aberturas de dicas - IndentationErrorUnindent: ",
      IndentationErrorUnindent_quantidade)
print("IndentationErrorUnindent_tempo: ", IndentationErrorUnindent_tempo)
print('\n')

print("TabErrorInconsistent_quantidade_ERROS: ",
      TabErrorInconsistent_quantidade_ERROS)
print("Aberturas de dicas - TabErrorInconsistent: ",
      TabErrorInconsistent_quantidade)
print("TabErrorInconsistent_tempo: ", TabErrorInconsistent_tempo)
print('\n')

print("ValueErrorInvalid_quantidade_ERROS: ",
      ValueErrorInvalid_quantidade_ERROS)
print("Aberturas de dicas - ValueErrorInvalid: ",
      ValueErrorInvalid_quantidade)
print("ValueErrorInvalid_tempo: ", ValueErrorInvalid_tempo)
print('\n')

print("TypeErrorUnsuported_quantidade_ERROS: ",
      TypeErrorUnsuported_quantidade_ERROS)
print("Aberturas de dicas - TypeErrorUnsuported: ",
      TypeErrorUnsuported_quantidade)
print("TypeErrorUnsuported_tempo: ", TypeErrorUnsuported_tempo)
print('\n')

print("TypeErrorCant_quantidade_ERROS: ", TypeErrorCant_quantidade_ERROS)
print("Aberturas de dicas - TypeErrorCant: ", TypeErrorCant_quantidade)
print("TypeErrorCant_tempo: ", TypeErrorCant_tempo)
print('\n')

print("IndexErrorIndex_quantidade_ERROS: ", IndexErrorIndex_quantidade_ERROS)
print("Aberturas de dicas - IndexErrorIndex: ",
      IndexErrorIndex_quantidade)
print("IndexErrorIndex_tempo: ", IndexErrorIndex_tempo)
print('\n')

print("ZeroDivisionErrorDivision_quantidade_ERROS: ",
      ZeroDivisionErrorDivision_quantidade_ERROS)
print("Aberturas de dicas - ZeroDivisionErrorDivision: ",
      ZeroDivisionErrorDivision_quantidade)
print("ZeroDivisionErrorDivision_tempo: ", ZeroDivisionErrorDivision_tempo)
print('\n')

print("ZeroDivisionErrorFloat_quantidade_ERROS: ",
      ZeroDivisionErrorFloat_quantidade_ERROS)
print("Aberturas de dicas - ZeroDivisionErrorFloat: ",
      ZeroDivisionErrorFloat_quantidade)
print("ZeroDivisionErrorFloat_tempo: ", ZeroDivisionErrorFloat_tempo)
print('\n')

with open('saida_traducao.txt', 'w') as f2:
    for item in lista_traducao:
        f2.write("%s\n" % item)

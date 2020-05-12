import pandas as pd
import numpy as np

class translator:
    variable_counter = 16
    def __init__(self, symbol_table=dict()):
            '''generate binary code from instruction type and components
            A-instruction: @value, here value can be literal
            C-instruction: dest=comp;jump

            look into specification contract table for conversion'''
            self.symbols = symbol_table

    

    def get_binary(self, instruction_type, components):
        self.binary_code = ''

        if instruction_type == 0:
           self.binary_code = self.translate_Ainstruction(instruction_type, components)
           
        elif instruction_type == 1:
            self.binary_code = self.translate_Cinstruction(instruction_type, components)
        else:
            print('This instruction type is not supported yet.')
            return -1
        return self.binary_code

    def translate_Ainstruction(self, instruction_type, components):
        #handle A-instruction
        address = components['address']
        #check for variable
        if not address.isdigit():
            if not address in self.symbols:
                self.symbols[address] = str(translator.variable_counter)
                translator.variable_counter += 1
            address = self.symbols[address]
        return "{:0>15}".format(str(instruction_type) + bin(int(address))[2:])
        
    def translate_Cinstruction(self, instruction_type, components):
        #handle C-instruction
        cinstr_map = pd.DataFrame(pd.read_csv('data.txt', sep=',', encoding='utf-16', dtype='string'), columns=['field','symbol','binary'])
        cinstr_map = cinstr_map.replace(np.nan, 'null', regex=True)
        return str(instruction_type) + '11' + \
                      cinstr_map.loc[(cinstr_map['symbol'] == components['comp']) & (cinstr_map['field'] == 'comp'), 'binary'].values[0] + \
                      cinstr_map.loc[(cinstr_map['symbol'] == components['dest']) & (cinstr_map['field'] == 'dest'), 'binary'].values[0] + \
                      cinstr_map.loc[(cinstr_map['symbol'] == components['jump']) & (cinstr_map['field'] == 'jump'), 'binary'].values[0]


    
        

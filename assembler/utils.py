import pandas as pd

def get_predefined_symbols():
    '''Create a dataframe containing Hack
    computer predefined symbols

    placeholder: symbol, value

    Label RAM address (hexa)
SP 0 0x0000
LCL 1 0x0001
ARG 2 0x0002
THIS 3 0x0003
THAT 4 0x0004
R0-R15 0-15 0x0000-f
SCREEN 16384 0x4000
KBD 24576 0x6000

    return dataframe'''
    symbols = [['R0','0'],
               ['R1','1'],
               ['R2','2'],
               ['R3','3'],
               ['R4','4'],
               ['R5','5'],
               ['R6','6'],
               ['R7','7'],
               ['R8','8'],
               ['R9','9'],
               ['R10','10'],
               ['R11','11'],
               ['R12','12'],
               ['R13','13'],
               ['R14','14'],
               ['R15','15'],
               ['SP','0'],
               ['LCL','1'],
               ['ARG','2'],
               ['THIS','3'],
               ['THAT','4'],
               ['SCREEN','16384'],
               ['KBD','24576']]
    return pd.DataFrame(symbols, columns=['label','value'])
    
def get_sym_bin_mapping():
    '''Create a dataframe containing symbolic to
    binary mapping

    placeholder: field, symbol, binary

    return dataframe'''

    dest_map = [['dest','null','000'],
                ['dest','M','001'],
                ['dest','D','010'],
                ['dest','MD','011'],
                ['dest','A','100'],
                ['dest','AM','101'],
                ['dest','AD','110'],
                ['dest','AMD','111']]
    
    jump_map = [['jump','null','000'],
                ['jump','JGT','001'],
                ['jump','JEQ','010'],
                ['jump','JGE','011'],
                ['jump','JLT','100'],
                ['jump','JNE','101'],
                ['jump','JLE','110'],
                ['jump','JMP','111']]
    
    comp_map = [['comp','null','1101010'],
                ['comp','0','0101010'],
                ['comp','1','0111111'],
                ['comp','-1','0111010'],
                ['comp','D','0001100'],
                ['comp','A','0110000'],
                ['comp','!D','0001101'],
                ['comp','!A','0110001'],
                ['comp','-D','0001111'],
                ['comp','-A','0110011'],
                ['comp','D+1','0011111'],
                ['comp','A+1','0110111'],
                ['comp','D-1','0001110'],
                ['comp','A-1','0110010'],
                ['comp','D+A','0000010'],
                ['comp','D-A','0010011'],
                ['comp','A-D','0000111'],
                ['comp','D&A','0000000'],
                ['comp','D|A','0010101'],
                ['comp','M','1110000'],
                ['comp','!M','1110001'],
                ['comp','-M','1110011'],
                ['comp','M+1','1110111'],
                ['comp','M-1','1110010'],
                ['comp','D+M','1000010'],
                ['comp','D-M','1010011'],
                ['comp','M-D','1000111'],
                ['comp','D&M','1000000'],
                ['comp','D|M','1010101']]

    hack_cinstruction_map = dest_map + jump_map + comp_map
    hack_cinstruction_map = pd.DataFrame(hack_cinstruction_map,
                                         columns = ['field', 'symbol', 'binary'])
    
    return hack_cinstruction_map

def save_csv(dataframe, csv_name):
    '''given a dataframe, save to csv file'''
    dataframe.to_csv(csv_name,encoding='utf-16')

    
if __name__ == "__main__":
    sym_bin_map_df = get_sym_bin_mapping()
    pre_sym_df = get_predefined_symbols()
    save_csv(sym_bin_map_df, 'data.txt')
    save_csv(pre_sym_df, 'symbols.txt')

    
    

import myparser
import mytranslator
import pandas as pd
import os
    
def assembler(filename):
    '''open a file with .asm extension and remove whitespaces
    and comments then do first pass to handle symbols (labels
    and variables). in second pass translate in binary code'''
    
    try:
        if not filename.endswith('.asm'):
            print("Cannot process, input file format is not supported")
            return -1

        # load assembler code
        with open(filename) as f:
            data = f.readlines()
            
        binary_code = [] # initialize the container to store binary translated code
        line_no = 0 # start line counter
        parser = myparser.parser()
        
        ###### First pass ######
        #create and populate symbol table with predefined symbols
        symbol_df = pd.DataFrame(pd.read_csv('symbols.txt', sep=',', encoding='utf-16', dtype='string'), columns=['label','value'])
        symbol_table = dict(zip(symbol_df.label, symbol_df.value))

        preprocessed_data = []
        for line in data:
            line = line.strip()
            #remove comments
            if '//' in line: 
                line = line[:line.find('//')]
                
            if line:
                instruction_type, components = parser.parse(line)
                #if it's label then update symbol table
                if instruction_type == 2:
                    if not components['label'] in symbol_table:
                        symbol_table[components['label']] = str(line_no)

                #this is an instruction so add to preprocessed code
                else:
                    preprocessed_data.append(line)
                    line_no+=1
        
        ###### Second pass ######
        translator = mytranslator.translator(symbol_table)
        for line in preprocessed_data:
            instruction_type, components = parser.parse(line)
            binary_code.append(translator.get_binary(instruction_type, components))
        print(symbol_table)
    except Exception as e:
        print(e)
        return

    return binary_code
    
if __name__ == "__main__":
    input_filename = input("Enter Filename: ")

    output_filename = os.path.splitext(input_filename)

    with open(output_filename[0] + '.hack', 'w') as of:
            of.writelines('\n'.join(assembler(input_filename)))
    
        
        


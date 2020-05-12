class parser:

    def __init__(self):
        '''identify instruction type, break lines into components
    return type, components
                             
    A-instruction: @value
    C-instruction: dest=comp;jump
    label declaration: (label)

    Assumptions:
    - no whitespaces at start and end.'''
        self.instruction_type = -1
        self.components = dict()

    def parse(self, line):
        if line.startswith('(') and line.endswith(')'):
            self.parse_label(line)
            
        elif line.startswith('@'): #A-instruction
            self.parse_ainstruction(line)
            
        else:
            self.parse_cinstruction(line)
        return (self.instruction_type, self.components)
    
    def parse_ainstruction(self, line):
        self.instruction_type = 0
        self.components['address'] = line[1:].strip()

    def parse_cinstruction(self, line):
        self.instruction_type = 1
        self.components['dest'] = 'null'
        self.components['comp'] = 'null'
        self.components['jump'] = 'null'
        
        if '=' in line:
            self.components['dest'] = (line.split('=')[0]).strip()
            if ';' in line:
                self.components['comp'] = ((line.split('=')[0]).split(';')[0]).strip()
                self.components['jump'] = ((line.split('=')[0]).split(';')[1]).strip()
            self.components['comp'] = (line.split('=')[1]).strip()

        elif ';' in line:
            self.components['comp'] = (line.split(';')[0]).strip()
            self.components['jump'] = (line.split(';')[1]).strip()
        else:
            self.components['comp'] = line.strip()

    def parse_label(self, line):
        self.instruction_type = 2
        self.components['label'] = line[1:-1].strip()



                

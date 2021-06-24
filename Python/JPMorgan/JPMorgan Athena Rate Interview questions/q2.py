orgstruct = {'ceo': {'tech': {'a': None, 'b': None}, 'HR': {'a':{'x':None}, 'b':None, 'c':None}}}

orgstruct1 = {'ceo': {'tech': {'a': None}}}
orgstruct2 = {'ceo': {'tech': None}}
orgstruct3 = {'ceo': None}

def countmanagers(orgstruct:dict, num_managers = 0):

    for _, value in orgstruct.items():
        if isinstance(value,dict):
            num_managers += 1
            num_managers = countmanagers(value, num_managers)
            

        continue
    return num_managers

def countmanagers1(orgstruct:dict, num_managers = 0):

    for _, value in orgstruct.items():
        if isinstance(value,dict):
            num_managers = countmanagers1(value, num_managers)
            
            if len(value) >= 3:
                num_managers += 1
                
        continue
    return num_managers

print(countmanagers1(orgstruct))

        
    
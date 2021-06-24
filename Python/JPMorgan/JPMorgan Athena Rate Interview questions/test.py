def distributePortfolio(x:dict, cash:int):
    CurrentPortfolio = sum(x.values())
    NewPortfolio = CurrentPortfolio + cash
    TargetValue = NewPortfolio / len(x)
    
    
    for key, value in x.items():
        balance = TargetValue - value 
        x[key] = balance
    return x

def distributePortfolio2(x:dict, cash:int, weightage:dict):
    CurrentPortfolio = sum(x.values())
    NewPortfolio = CurrentPortfolio + cash
    
    
    for key, value in x.items():
        TargetValue = weightage[key] * NewPortfolio
        Balance = TargetValue - value
        x[key] = Balance
    return x

print(distributePortfolio2({'a':1000,'b':2000}, 3000, {'a':0.8, 'b':0.2}))




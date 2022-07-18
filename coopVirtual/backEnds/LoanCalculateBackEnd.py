
class LoanCalculateBackEnd:
    
    def calculate(self, interes, amount, coute):
        data = []

        monthCuote  = (amount * interes) / (1-pow((1 + interes), (-coute)))
        monthCuote  = monthCuote
        
        for i in range(coute):
            if i == 0:
                monthAmount = amount
            else:
                monthAmount = data[i - 1]['saldoInsoluto']
                
            monthInteres    = monthAmount * interes
            amortizacion    = monthCuote - monthInteres
            
            if i == 0:
                amortizacionAc  = amortizacion
                saldoInsoluto   = amount - amortizacionAc 
                
            else:
                amortizacionAc  = data[i - 1]['amortizacionAc'] + amortizacion
                saldoInsoluto   = monthAmount - amortizacion
            
            
            data.append({
                "cuoteNo"           : (i + 1),
                "monthCoute"        : monthCuote,
                "interes"           : monthInteres,
                "amortizacion"      : amortizacion,
                "amortizacionAc"    : amortizacionAc,
                "saldoInsoluto"     : saldoInsoluto,
            })
        
        return data
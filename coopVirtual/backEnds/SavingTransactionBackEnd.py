from django.db.models import Sum
from coopVirtual.models.SavingTransactionModel import SavingTransactionModel

class SavingTransactionBackEnd:
    
    def savingNormalTotal(selef):
        total               = 0
        savingTransaction   = SavingTransactionModel.objects.exclude(id_tipo_ahorro_id = 2).order_by("tipo_transaccion").annotate(total_amount = Sum('monto'))
        
        for list in savingTransaction:
            if int(list.tipo_transaccion == 1):
                total += float(list.total_amount)
            else:
                total -= float(list.total_amount)

        return total
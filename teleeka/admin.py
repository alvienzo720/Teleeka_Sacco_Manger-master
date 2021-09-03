from django.contrib import admin

from . models import *


admin.site.register(Client)
admin.site.register(SavingGroup)
admin.site.register(Deposit)
admin.site.register(Withdrawl)
admin.site.register(Loan)



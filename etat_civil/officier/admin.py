"""
admin of the officier app.
"""
from django.contrib import admin
from .models import Declaration, Declarant, Enfant, Pere, Mere


admin.site.register(Declaration)
admin.site.register(Declarant)
admin.site.register(Enfant)
admin.site.register(Pere)
admin.site.register(Mere)

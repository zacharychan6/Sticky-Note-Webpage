from django.contrib import admin
from .models import sticky_note
from .models import Author
# Register your models here.
admin.site.register(sticky_note)
admin.site.register(Author)

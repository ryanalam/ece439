from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'profession', 'telephone_number', 'email')
    list_filter = ('profession',)
    search_fields = ('name', 'email')
    fields = ('id','name', 'address', 'profession', 'telephone_number', 'email')  # Specify the fields you want to edit

# Register the Student model with the custom admin class
admin.site.register(Student, StudentAdmin)

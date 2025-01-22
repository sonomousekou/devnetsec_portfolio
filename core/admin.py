from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.apps import apps

# Get all the models from your Django application
app = apps.get_app_config('core')

# Iterate over each model and register it with customized Admin class
for model in app.get_models():
     @admin.register(model)
     class CustomAdmin(ImportExportModelAdmin, admin.ModelAdmin):
         list_display = [field.name for field in model._meta.fields if field.name != "id"]


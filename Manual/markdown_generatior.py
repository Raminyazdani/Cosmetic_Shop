import django.apps
from Cosmetic_Shop.wsgi import *
django.apps.AppConfig.ready = lambda self: None
print("Django is ready")
for app in django.apps.apps.get_app_configs():
    app.ready()

models = []
for model in django.apps.apps.get_models():
    if model.__module__.split('.')[0] == "django":
        continue
    models.append(model)
dict_temp = {}
apps_models = {}
for model in models:
    app_name = model._meta.app_label
    if app_name not in apps_models:
        apps_models[app_name] = []
    apps_models[app_name].append(model)

apps_model_fields_and_related = {}
for app_name, models in apps_models.items():
    for model in models:
        model_name = model.__name__
        if app_name not in apps_model_fields_and_related:
            apps_model_fields_and_related[app_name] = {}
        apps_model_fields_and_related[app_name][model_name] = {}
        for field in model._meta.fields:
            apps_model_fields_and_related[app_name][model_name][field.name] = field
        for field in model._meta.many_to_many:
            apps_model_fields_and_related[app_name][model_name][field.name] = field
        for field in model._meta.related_objects:
            apps_model_fields_and_related[app_name][model_name][field.name] = field
with open("models_rel.md","w")as m:
    with open('models.md', 'w') as f:
        for app_name, models in apps_model_fields_and_related.items():
            f.write(f"* {app_name}\n")
            m.write(f"* {app_name}\n")
            model_count = 1
            for model_name, fields in models.items():
                f.write(f"\t{model_count}. {model_name}\n")
                m.write(f"\t{model_count}. {model_name}\n")
                field_count = 1
                for field_name, field in fields.items():
                    if str(field).startswith("<"):
                        f.write(f"\t\t* {field_name} : {field}\n")
                        m.write(f"\t\t* {field_name} : {field}\n")
                    else:
                        f.write(f"\t\t{field_count}. {field_name}\\")
                        f.write(f" {field}\n")
                    field_count += 1
                model_count += 1
                f.write("\n")
                m.write("\n")
            f.write("\n")
            m.write("\n")

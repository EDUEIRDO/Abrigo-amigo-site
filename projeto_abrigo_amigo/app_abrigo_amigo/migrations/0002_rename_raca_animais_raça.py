# Generated by Django 5.0.3 on 2024-03-07 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_abrigo_amigo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animais',
            old_name='raca',
            new_name='raça',
        ),
    ]

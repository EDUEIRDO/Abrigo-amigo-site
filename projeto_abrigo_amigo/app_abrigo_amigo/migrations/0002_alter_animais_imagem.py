# Generated by Django 5.0.3 on 2024-03-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abrigo_amigo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animais',
            name='imagem',
            field=models.ImageField(upload_to='projeto_abrigo_amigo/app_abrigo_amigo/fotos/'),
        ),
    ]
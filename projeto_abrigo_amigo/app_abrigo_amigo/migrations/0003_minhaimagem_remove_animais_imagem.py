# Generated by Django 5.0.3 on 2024-03-24 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_abrigo_amigo', '0002_alter_animais_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='MinhaImagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens/')),
            ],
        ),
        migrations.RemoveField(
            model_name='animais',
            name='imagem',
        ),
    ]

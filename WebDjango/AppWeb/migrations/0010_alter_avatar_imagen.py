# Generated by Django 3.2.15 on 2022-11-06 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0009_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(blank=True, default='avatares/administrador.png', null=True, upload_to='avatares'),
        ),
    ]

# Generated by Django 2.1.4 on 2018-12-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='tipo',
            field=models.CharField(choices=[('Deportes', 'Deportes'), ('Cultura', 'Cultura'), ('Politica', 'Politica'), ('Economia', 'Economia'), ('Actualidad', 'Actualidad')], max_length=100),
        ),
    ]

# Generated by Django 4.1.7 on 2023-03-31 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtyProd', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipe',
            name='personnels',
        ),
        migrations.AddField(
            model_name='equipe',
            name='personnels',
            field=models.ManyToManyField(to='ArtyProd.personnel'),
        ),
    ]

# Generated by Django 5.0.3 on 2024-05-26 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0004_rename_orderitems_ordermodel_ordereditems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customermodel',
            old_name='userid',
            new_name='username',
        ),
    ]

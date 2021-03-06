# Generated by Django 4.0.1 on 2022-02-25 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='wel',
        ),
        migrations.AlterField(
            model_name='booking',
            name='Patient_name',
            field=models.TextField(default='R', max_length=30),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dc',
            field=models.TextField(default='Rao', max_length=30),
        ),
        migrations.AlterField(
            model_name='family_doc',
            name='dc_name',
            field=models.TextField(default='Dr. Nene', max_length=30),
        ),
        migrations.AlterField(
            model_name='pd_doc',
            name='dc_name',
            field=models.TextField(default='Dr.Rao', max_length=30),
        ),
    ]

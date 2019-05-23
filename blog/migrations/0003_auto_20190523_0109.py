# Generated by Django 2.0.13 on 2019-05-23 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_cliente_orden_tecnico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orden',
            name='cliente',
        ),
        migrations.AddField(
            model_name='orden',
            name='cliente',
            field=models.ManyToManyField(to='blog.Cliente'),
        ),
        migrations.RemoveField(
            model_name='orden',
            name='tecnico',
        ),
        migrations.AddField(
            model_name='orden',
            name='tecnico',
            field=models.ManyToManyField(to='blog.Tecnico'),
        ),
    ]
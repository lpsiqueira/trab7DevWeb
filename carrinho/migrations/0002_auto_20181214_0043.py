# Generated by Django 2.1.4 on 2018-12-14 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carrinho',
            name='id',
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='appsite.Projeto', unique=True),
        ),
    ]
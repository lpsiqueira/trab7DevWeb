# Generated by Django 2.1.4 on 2018-12-14 01:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('carrinho', '0002_auto_20181214_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrinho',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carrinho',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appsite.Projeto'),
        ),
    ]

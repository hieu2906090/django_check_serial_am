# Generated by Django 2.1.4 on 2019-01-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PagesApp', '0004_auto_20190110_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='giaodichdetail',
            name='note',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
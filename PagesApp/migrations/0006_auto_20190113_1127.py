# Generated by Django 2.1.4 on 2019-01-13 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PagesApp', '0005_auto_20190112_0000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='giaodich',
            old_name='em_id',
            new_name='em',
        ),
        migrations.RenameField(
            model_name='giaodichdetail',
            old_name='em_id',
            new_name='em',
        ),
        migrations.RenameField(
            model_name='giaodichdetail',
            old_name='gd_id',
            new_name='gd',
        ),
    ]
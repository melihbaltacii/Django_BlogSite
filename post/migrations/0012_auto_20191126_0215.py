# Generated by Django 2.2.7 on 2019-11-25 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20191126_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='postcomment',
            new_name='postComment',
        ),
    ]
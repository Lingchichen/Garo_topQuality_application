# Generated by Django 2.0.5 on 2018-06-13 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_qa_app', '0009_auto_20180613_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='can_add',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='can_edit',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
    ]

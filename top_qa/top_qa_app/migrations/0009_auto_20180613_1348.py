# Generated by Django 2.0.5 on 2018-06-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_qa_app', '0008_auto_20180612_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='source',
            field=models.CharField(choices=[('COMPANY_WEBSITE', 'Company Website'), ('OTHERS', 'Others'), ('LINKEDIN', 'LinkedIn')], max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

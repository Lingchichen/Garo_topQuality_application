# Generated by Django 2.0.5 on 2018-06-11 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_qa_app', '0006_auto_20180611_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='source',
            field=models.CharField(choices=[('OTHERS', 'Others'), ('LINKEDIN', 'LinkedIn'), ('COMPANY_WEBSITE', 'Company Website')], max_length=255),
        ),
    ]
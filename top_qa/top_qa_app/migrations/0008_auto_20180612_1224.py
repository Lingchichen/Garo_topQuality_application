# Generated by Django 2.0.5 on 2018-06-12 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_qa_app', '0007_auto_20180611_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='company_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='job_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='other_information',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='source',
            field=models.CharField(choices=[('OTHERS', 'Others'), ('COMPANY_WEBSITE', 'Company Website'), ('LINKEDIN', 'LinkedIn')], max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='source_type',
            field=models.CharField(blank=True, default='TQR-India-Lead', max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sourced_by',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('contact_type', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('source_type', models.CharField(max_length=255)),
                ('other_information', models.CharField(max_length=255)),
                ('listed', models.CharField(max_length=255)),
                ('bounce_back', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('can_edit', models.BooleanField(default=False)),
                ('can_add', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]

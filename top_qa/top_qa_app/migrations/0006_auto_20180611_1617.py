# Generated by Django 2.0.5 on 2018-06-11 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top_qa_app', '0005_auto_20180608_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='category',
            field=models.CharField(choices=[('FB_Bakery', 'FB Bakery'), ('FB_Beverages_Alcohol', 'FB Beverages(Alcohol)'), ('FB_Beverages_Non-Alcohol', 'FB Beverages(Non-Alcohol)'), ('FB_Canned_Food', 'FB Canned Food'), ('FB_Dairy', 'FB Dariy'), ('FB_Flavours_and_Ingredients', 'FB Flavours and Ingredients'), ('FB_Food_and_Beverage', 'FB Food and Beverage'), ('FB_Frozen', 'FB Frozen'), ('FB_Bakery', 'FB Bakery'), ('FB_Meat_Seafood', 'FB Meat/Seafood'), ('FB_Nutritional', 'FB Nutritional'), ('FB_Organics', 'FB Organics'), ('FB_Packaging_General', 'FB Packaging (General)'), ('FB_Snacks_Confectionary', 'FB Snacks/Confectionary'), ('FB_Vegetables_and_Produce', 'FB Vegetables and Produce'), ('Medical_BioTech', 'Medical - BioTech'), ('Medical_Devices', 'Medical - Devices'), ('Medical_Healthcare', 'Medical - Healthcare'), ('Medical_Pharma', 'Medical - Pharma')], max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_type',
            field=models.CharField(choices=[('HA_CONTACT', 'HA-Contact'), ('HR_CONTACT', 'HR-Contact')], max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sourced_by',
            field=models.CharField(max_length=255),
        ),
    ]

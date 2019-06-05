from django.db import models
from django.contrib.auth import authenticate, login
# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    can_edit = models.BooleanField(default=False)
    can_add = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


class Contact(models.Model):
    # define choices
    HA_CONTACT = 'HA_CONTACT'
    HR_CONTACT = 'HR_CONTACT'
    LINKEDIN = 'LINKEDIN'
    COMPANY_WEBSITE = 'COMPANY_WEBSITE'
    OTHERS = 'OTHERS'
    YES = 'YES'
    NO = 'NO'
    FB_Bakery = 'FB_Bakery'
    FB_Beverages_Alcohol = 'FB_Beverages_Alcohol'
    FB_Beverages_NonAlcohol = 'FB_Beverages_Non-Alcohol'
    FB_Canned_Food = 'FB_Canned_Food'
    FB_Dairy = 'FB_Dairy'
    FB_Flavours_and_Ingredients = 'FB_Flavours_and_Ingredients'
    FB_Food_and_Beverage = 'FB_Food_and_Beverage'
    FB_Frozen = 'FB_Frozen'
    FB_PetFood = 'FB_PetFood'
    FB_Meat_Seafood = 'FB_Meat_Seafood'
    FB_Nutritional = 'FB_Nutritional'
    FB_Organics = 'FB_Organics'
    FB_Packaging_General = 'FB_Packaging_General'
    FB_Snacks_Confectionary = 'FB_Snacks_Confectionary'
    FB_Vegetables_and_Produce = 'FB_Vegetables_and_Produce'
    Medical_BioTech = 'Medical_BioTech'
    Medical_Devices = 'Medical_Devices'
    Medical_Healthcare = 'Medical_Healthcare'
    Medical_Pharma = 'Medical_Pharma'
    # contact_id=models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    company_name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    # CATEGORY DROPDOWN NOT DECIDE YET
    CATEGORY_CHOICE = (
        (FB_Bakery, 'FB Bakery'),
        (FB_Beverages_Alcohol, 'FB Beverages(Alcohol)'),
        (FB_Beverages_NonAlcohol, 'FB Beverages(Non-Alcohol)'),
        (FB_Canned_Food, 'FB Canned Food'),
        (FB_Dairy, 'FB Dariy'),
        (FB_Flavours_and_Ingredients, 'FB Flavours and Ingredients'),
        (FB_Food_and_Beverage, 'FB Food and Beverage'),
        (FB_Frozen, 'FB Frozen'),
        (FB_PetFood, 'FB Pet Food'),
        (FB_Meat_Seafood, 'FB Meat/Seafood'),
        (FB_Nutritional, 'FB Nutritional'),
        (FB_Organics, 'FB Organics'),
        (FB_Packaging_General, 'FB Packaging (General)'),
        (FB_Snacks_Confectionary, 'FB Snacks/Confectionary'),
        (FB_Vegetables_and_Produce, 'FB Vegetables and Produce'),
        (Medical_BioTech, 'Medical - BioTech'),
        (Medical_Devices, 'Medical - Devices'),
        (Medical_Healthcare, 'Medical - Healthcare'),
        (Medical_Pharma, 'Medical - Pharma'),

    )
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICE)

    CONTACT_CHOICE = (
        (HA_CONTACT, 'HA-Contact'),
        (HR_CONTACT, 'HR-Contact')
    )
    contact_type = models.CharField(max_length=255, choices=CONTACT_CHOICE)
    SOURCE_CHOICE = {
        (LINKEDIN, 'LinkedIn'),
        (COMPANY_WEBSITE, 'Company Website'),
        (OTHERS, 'Others')
    }
    source = models.CharField(max_length=255, choices=SOURCE_CHOICE)
    # default to username is loggedin
    sourced_by = models.CharField(
        max_length=255, default="", blank=True, null=True)
    source_type = models.CharField(
        max_length=255, default="TQR-India-Lead", blank=True)
    other_information = models.CharField(
        max_length=255, default="", blank=True, null=True)

    listed = models.BooleanField(default=True)
    doNotEmail = models.BooleanField(default=False)

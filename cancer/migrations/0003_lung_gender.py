# Generated by Django 4.1.7 on 2023-12-27 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0002_lung_alter_breast_area_mean_alter_breast_area_se_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lung',
            name='GENDER',
            field=models.IntegerField(default=0),
        ),
    ]

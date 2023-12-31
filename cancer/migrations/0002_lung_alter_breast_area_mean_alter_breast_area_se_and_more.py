# Generated by Django 4.2.4 on 2023-08-08 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='lung',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AGE', models.IntegerField(default=0)),
                ('SMOKING', models.IntegerField(default=0)),
                ('YELLOW_FINGERS', models.IntegerField(default=0)),
                ('ANXIETY', models.IntegerField(default=0)),
                ('PEER_PRESSURE', models.IntegerField(default=0)),
                ('CHRONIC_DISEASE', models.IntegerField(default=0)),
                ('FATIGUE', models.IntegerField(default=0)),
                ('ALLERGY', models.IntegerField(default=0)),
                ('WHEEZING', models.IntegerField(default=0)),
                ('ALCOHOL', models.IntegerField(default=0)),
                ('CONSUMING', models.IntegerField(default=0)),
                ('COUGHING', models.IntegerField(default=0)),
                ('SHORTNESS_OF_BREATH', models.IntegerField(default=0)),
                ('SWALLOWING_DIFFICULTY', models.IntegerField(default=0)),
                ('CHEST_PAIN', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='breast',
            name='area_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='area_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='area_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='compactness_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='compactness_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='compactness_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concave_points_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concave_points_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concave_points_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concavity_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concavity_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='concavity_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='fractal_dimension_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='fractal_dimension_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='fractal_dimension_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='perimeter_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='perimeter_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='perimeter_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='radius_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='radius_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='radius_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='smoothness_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='smoothness_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='smoothness_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='symmetry_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='symmetry_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='symmetry_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='texture_mean',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='texture_se',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='breast',
            name='texture_worst',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]

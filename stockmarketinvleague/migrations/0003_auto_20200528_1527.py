# Generated by Django 3.0.5 on 2020-05-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockmarketinvleague', '0002_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='companyDescription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='companyName',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='low_high',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='price',
            field=models.FloatField(blank=True, max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sector',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='symbol',
            field=models.CharField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
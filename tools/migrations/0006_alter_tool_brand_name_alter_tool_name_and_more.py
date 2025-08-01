# Generated by Django 5.2.3 on 2025-07-21 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_tool_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='brand_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='tool',
            name='room',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='section',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tool',
            name='tracking_number',
            field=models.CharField(max_length=20),
        ),
    ]

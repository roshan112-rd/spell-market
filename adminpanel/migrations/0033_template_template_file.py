# Generated by Django 3.2 on 2022-12-05 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0032_alter_promocode_promo_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='template_file',
            field=models.FileField(blank=True, null=True, upload_to='template_files/'),
        ),
    ]

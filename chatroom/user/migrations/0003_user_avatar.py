# Generated by Django 4.1.5 on 2023-01-09 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_bio_user_mobile_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default_user.png', null=True, upload_to=''),
        ),
    ]

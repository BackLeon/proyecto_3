# Generated by Django 4.1.4 on 2023-01-26 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0005_alter_publication_options_alter_publication_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='profile_image',
            field=models.ImageField(default='batman.png', upload_to=''),
        ),
    ]

# Generated by Django 3.2.12 on 2022-03-25 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('degreed2', '0010_auto_20220324_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='subsection_id',
            field=models.CharField(blank=True, db_index=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='subsection_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]

# Generated by Django 3.2.11 on 2022-02-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blackboard', '0013_blacboardglobalconfiguration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blackboardlearnerassessmentdatatransmissionaudit',
            name='enterprise_course_enrollment_id',
            field=models.IntegerField(db_index=True),
        ),
    ]

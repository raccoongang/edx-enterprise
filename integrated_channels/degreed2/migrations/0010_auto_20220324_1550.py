# Generated by Django 3.2.12 on 2022-03-24 15:50

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('degreed2', '0009_alter_degreed2learnerdatatransmissionaudit_completed_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='enterprise_customer_uuid',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='grade',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='instructor_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='plugin_configuration_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='total_hours',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='course_completed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='course_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='enterprise_course_enrollment_id',
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='error_message',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='degreed2learnerdatatransmissionaudit',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

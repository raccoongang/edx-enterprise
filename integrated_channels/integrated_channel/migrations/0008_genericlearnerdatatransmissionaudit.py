# Generated by Django 3.2.12 on 2022-03-25 17:48

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('integrated_channel', '0007_delete_learnerdatatransmissionaudit'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericLearnerDataTransmissionAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('enterprise_customer_uuid', models.UUIDField(blank=True, null=True)),
                ('plugin_configuration_id', models.PositiveIntegerField(blank=True, null=True)),
                ('enterprise_course_enrollment_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('course_id', models.CharField(max_length=255)),
                ('course_completed', models.BooleanField(default=True)),
                ('completed_timestamp', models.DateTimeField(blank=True, null=True)),
                ('instructor_name', models.CharField(blank=True, max_length=255)),
                ('grade', models.FloatField(blank=True, null=True)),
                ('total_hours', models.FloatField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 3.1.3 on 2022-01-26 08:39

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_sendgrid_parse', '0010_auto_20220125_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='attachment_info',
            field=jsonfield.fields.JSONField(blank=True, null=True, verbose_name='Attachment Info'),
        ),
        migrations.AlterField(
            model_name='email',
            name='envelope',
            field=jsonfield.fields.JSONField(blank=True, default={'from': None, 'to': None}, null=True, verbose_name='Envelope'),
        ),
    ]

# Generated by Django 3.0.4 on 2020-04-05 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_productinorder_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='session_key',
            field=models.CharField(blank=True, default=None, max_length=128, null=True),
        ),
    ]

# Generated by Django 2.2.3 on 2019-12-31 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ee_control_upload', '0002_auto_20191230_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='username',
            field=models.CharField(max_length=150, primary_key=True, serialize=False),
        ),
    ]
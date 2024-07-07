# Generated by Django 5.0.6 on 2024-06-28 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_courseconditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('theory', 'نظري'), ('practical', 'عملي')], default='theory', max_length=50),
            preserve_default=False,
        ),
    ]
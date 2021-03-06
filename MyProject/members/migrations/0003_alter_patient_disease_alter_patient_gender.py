# Generated by Django 4.0.3 on 2022-05-23 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_patient_disease'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='disease',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.specialties'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]

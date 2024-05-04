# Generated by Django 5.0.3 on 2024-04-24 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_usersubmission_remove_doctorpatientfile_doctor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorPatientFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(max_length=100, unique=True)),
                ('age', models.IntegerField(verbose_name='Age (years)')),
                ('sex', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], default=True, verbose_name='Sex')),
                ('cp', models.CharField(choices=[('Typical Angina', 'Typical Angina'), ('Atypical Angina', 'Atypical Angina'), ('Non-Anginal Pain', 'Non-Anginal Pain'), ('Asymptomatic', 'Asymptomatic')], max_length=256, verbose_name='Chest Pain Type')),
                ('trestbps', models.IntegerField(verbose_name='Resting Blood Pressure (mm Hg) on admission to the hospital')),
                ('chol', models.IntegerField(verbose_name='Serum Cholesterol (mg/dl)')),
                ('fbs', models.BooleanField(choices=[(True, 'True'), (False, 'False')], default=False, verbose_name='Fasting Blood Sugar > 120 mg/dl?')),
                ('restecg', models.CharField(choices=[('Normal', 'Normal'), ('Abnormal - ST-T wave', 'Abnormal - ST-T wave'), ('Abnormal - Left Ventricular Hypertrophy', 'Abnormal - Left Ventricular Hypertrophy')], max_length=256, verbose_name='Resting Electrocardiographic Results')),
                ('thalach', models.IntegerField(verbose_name='Maximum Heart Rate Achieved')),
                ('exang', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False, verbose_name='Exercise Induced Angina?')),
                ('oldpeak', models.FloatField(verbose_name='ST Depression Induced by Exercise Relative to Rest')),
                ('slope', models.CharField(choices=[('Upsloping', 'Upsloping'), ('Flat', 'Flat'), ('Downsloping', 'Downsloping')], max_length=256, verbose_name='Slope of the Peak Exercise ST Segment')),
                ('ca', models.FloatField(verbose_name='Number of Major Vessels Colored by Fluoroscopy')),
                ('thal', models.CharField(choices=[('Normal', 'Normal'), ('Fixed Defect', 'Fixed Defect'), ('Reversible Defect', 'Reversible Defect')], max_length=256, verbose_name='Thalassemia')),
                ('diagnosis', models.CharField(max_length=255)),
                ('prognosis', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserSubmission',
        ),
    ]

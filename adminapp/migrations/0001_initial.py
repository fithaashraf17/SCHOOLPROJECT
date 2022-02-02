# Generated by Django 4.0.1 on 2022-01-31 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coursename', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='sessionyear_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('photo', models.FileField(upload_to='tea')),
                ('fathername', models.CharField(default='', max_length=200)),
                ('mothername', models.CharField(default='', max_length=200)),
                ('section', models.CharField(default='', max_length=200)),
                ('dob', models.CharField(default='', max_length=32)),
                ('phone', models.CharField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('status', models.CharField(default='pending', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='student_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(upload_to='student')),
                ('fathername', models.CharField(default='', max_length=200)),
                ('mothername', models.CharField(default='', max_length=200)),
                ('standard', models.CharField(default='', max_length=200)),
                ('dob', models.CharField(default='', max_length=32)),
                ('phone', models.CharField(default='', max_length=500)),
                ('admission_no', models.CharField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=500)),
                ('feetype', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('roll', models.CharField(default='', max_length=500)),
                ('regno', models.CharField(default='', max_length=500)),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=32)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('hpassword', models.TextField(default='')),
                ('courseid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.course_tb')),
                ('sesid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.sessionyear_tb')),
            ],
        ),
        migrations.CreateModel(
            name='teacher_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('photo', models.FileField(upload_to='tea')),
                ('fathername', models.CharField(default='', max_length=200)),
                ('mothername', models.CharField(default='', max_length=200)),
                ('section', models.CharField(default='', max_length=200)),
                ('dob', models.CharField(default='', max_length=32)),
                ('phone', models.CharField(default='', max_length=500)),
                ('qualification', models.CharField(default='', max_length=500)),
                ('gender', models.CharField(default='', max_length=500)),
                ('address', models.CharField(default='', max_length=500)),
                ('experience', models.CharField(default='', max_length=500)),
                ('subject', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=200)),
                ('organisationaddress', models.CharField(default='', max_length=200)),
                ('password', models.CharField(default='', max_length=32)),
                ('designation', models.CharField(default='', max_length=200)),
                ('achievments', models.CharField(default='', max_length=32)),
                ('document', models.FileField(upload_to='teacher')),
                ('status', models.CharField(default='pending', max_length=200)),
                ('hpassword', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='timetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(default='', max_length=200)),
                ('div', models.CharField(default='', max_length=200)),
                ('day', models.CharField(default='', max_length=200)),
                ('period1', models.CharField(default='', max_length=200)),
                ('period2', models.CharField(default='', max_length=200)),
                ('period3', models.CharField(default='', max_length=200)),
                ('period4', models.CharField(default='', max_length=200)),
                ('period5', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='subject_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectname', models.CharField(default='', max_length=200)),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course_tb')),
                ('teacherid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.teacher_tb')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject1', models.FloatField(default=0)),
                ('subject2', models.FloatField(default=0)),
                ('subject3', models.FloatField(default=0)),
                ('subject4', models.FloatField(default=0)),
                ('subject5', models.FloatField(default=0)),
                ('subject_assignment_marks', models.CharField(default='', max_length=200)),
                ('sem', models.CharField(default='', max_length=200)),
                ('examtype', models.CharField(default='', max_length=200)),
                ('totalmark', models.CharField(default='', max_length=200)),
                ('studentmark', models.CharField(default='', max_length=200)),
                ('grade', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salarytype', models.CharField(default='', max_length=200)),
                ('allowance', models.CharField(default='', max_length=200)),
                ('month', models.CharField(default='', max_length=200)),
                ('date', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('teacherid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.teacher_tb')),
            ],
        ),
        migrations.CreateModel(
            name='notification_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('teacherid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='notification_stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='leave_report_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavedate', models.CharField(default='', max_length=200)),
                ('leave_message', models.TextField()),
                ('status', models.CharField(default='pending', max_length=200)),
                ('teacherid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.teacher_tb')),
            ],
        ),
        migrations.CreateModel(
            name='leave_report_student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leavedate', models.CharField(default='', max_length=200)),
                ('leave_message', models.TextField()),
                ('status', models.CharField(default='pending', max_length=200)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='feedback_teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedbackreply', models.TextField()),
                ('teacherid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.teacher_tb')),
            ],
        ),
        migrations.CreateModel(
            name='feedback_stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField()),
                ('feedbackreply', models.TextField()),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='fee_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(default='', max_length=200)),
                ('feetype', models.CharField(default='', max_length=200)),
                ('feeamount', models.CharField(default='', max_length=200)),
                ('clas', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('period', models.CharField(default='quarter1', max_length=200)),
                ('studentid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
        migrations.CreateModel(
            name='attendance_student_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(default='', max_length=200)),
                ('total_lec', models.CharField(default='', max_length=200)),
                ('lec_attended', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='pending', max_length=200)),
                ('studentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.student_tb')),
            ],
        ),
    ]

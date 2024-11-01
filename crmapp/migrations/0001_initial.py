# Generated by Django 4.2.16 on 2024-10-24 11:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leadstage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_type', models.CharField(choices=[('MEETING', 'Meeting'), ('CALL', 'Call'), ('INTERVIEW', 'Interview'), ('OTHER', 'Other')], max_length=20)),
                ('description', models.TextField()),
                ('from_date_time', models.DateTimeField()),
                ('to_date_time', models.DateTimeField()),
                ('location', models.CharField(max_length=255)),
                ('related_to', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ClockIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clock_in_time', models.DateTimeField(auto_now_add=True)),
                ('clock_out_time', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='company_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=40)),
                ('status', models.CharField(blank=True, max_length=40, null=True)),
                ('firstname', models.CharField(max_length=40)),
                ('lastname', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IndustryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20)),
                ('mobile_country_code', models.CharField(max_length=20)),
                ('executive_name', models.CharField(blank=True, max_length=40, null=True)),
                ('exe_designation', models.CharField(blank=True, max_length=40, null=True)),
                ('source', models.CharField(blank=True, max_length=40, null=True)),
                ('product', models.CharField(blank=True, max_length=40, null=True)),
                ('requirement', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=40, null=True)),
                ('gst', models.CharField(blank=True, max_length=40, null=True)),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.country')),
                ('stages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leadstage.leadstage')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Taskactivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_title', models.CharField(max_length=30)),
                ('due_date', models.DateTimeField()),
                ('priorty', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('task_description', models.CharField(blank=True, max_length=250, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='task_attachments/')),
                ('status', models.CharField(choices=[('incomplete', 'Incomplete'), ('inprogress', 'In Progress'), ('completed', 'Completed')], default='incomplete', max_length=20)),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.lead')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.country')),
            ],
        ),
        migrations.AddField(
            model_name='lead',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.state'),
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_up_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('lead', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.lead')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.taskactivity')),
            ],
        ),
        migrations.CreateModel(
            name='DeletedTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('task_title', models.CharField(max_length=30)),
                ('due_date', models.DateTimeField()),
                ('priorty', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10)),
                ('task_description', models.CharField(blank=True, max_length=250, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='task_attachments/')),
                ('related_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.lead')),
            ],
        ),
        migrations.CreateModel(
            name='contact_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=20, unique=True)),
                ('mobile_country_code', models.CharField(max_length=20)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.city')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.country')),
                ('state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crmapp.state')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crmapp.state'),
        ),
        migrations.CreateModel(
            name='bussiness_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executive_name', models.CharField(blank=True, default='none', max_length=40, null=True)),
                ('exe_designation', models.CharField(blank=True, max_length=40, null=True)),
                ('source', models.CharField(blank=True, max_length=40, null=True)),
                ('product', models.CharField(blank=True, max_length=40, null=True)),
                ('requirement', models.CharField(blank=True, max_length=250, null=True)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('industry_type', models.CharField(blank=True, max_length=40, null=True)),
                ('gst', models.CharField(blank=True, max_length=40, null=True)),
                ('stages', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leadstage.leadstage')),
            ],
        ),
    ]
# Generated by Django 3.1.1 on 2020-11-12 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('domain', models.CharField(max_length=60)),
                ('ip', models.CharField(max_length=15)),
                ('cname', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('idc_address', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=10)),
                ('contact_phone', models.CharField(max_length=20)),
                ('assistant', models.CharField(max_length=10)),
                ('assistant_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('business', models.CharField(max_length=50)),
                ('project', models.CharField(max_length=60)),
                ('application', models.CharField(max_length=60)),
                ('deploy_dir', models.CharField(max_length=100)),
                ('log_dir', models.CharField(max_length=100)),
                ('local_ip', models.CharField(max_length=18)),
                ('port', models.IntegerField()),
                ('leader', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='devops.user', to_field='username')),
            ],
        ),
    ]

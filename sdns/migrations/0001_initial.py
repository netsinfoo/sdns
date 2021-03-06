# Generated by Django 3.1.3 on 2021-02-05 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0043_add_tenancy_to_aggregates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('owner', models.CharField(max_length=1, null=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Resp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='use_domain', to='sdns.domain')),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=30)),
                ('reg', models.CharField(max_length=1)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdns.domain')),
                ('ip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.ipaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Ns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdns.domain')),
                ('ns', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.ipaddress')),
            ],
        ),
        migrations.CreateModel(
            name='Mx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('prior', models.CharField(max_length=2, null=True)),
                ('dom', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sdns.domain')),
                ('mx', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.ipaddress')),
            ],
        ),
        migrations.CreateModel(
            name='DomainServ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('relation', models.CharField(max_length=1)),
                ('dominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sdns.domain')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ipam.service')),
            ],
        ),
        migrations.CreateModel(
            name='Cts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('reg', models.CharField(max_length=1)),
                ('content', models.CharField(max_length=30)),
                ('registro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ipam.ipaddress')),
            ],
        ),
        migrations.AddConstraint(
            model_name='resp',
            constraint=models.UniqueConstraint(fields=('name', 'dom', 'tipo'), name='unique_resp'),
        ),
        migrations.AddConstraint(
            model_name='register',
            constraint=models.UniqueConstraint(fields=('host', 'domain'), name='unique_register'),
        ),
        migrations.AddConstraint(
            model_name='ns',
            constraint=models.UniqueConstraint(fields=('ns', 'dom'), name='unique_ns'),
        ),
        migrations.AddConstraint(
            model_name='mx',
            constraint=models.UniqueConstraint(fields=('mx', 'dom'), name='unique_,mx'),
        ),
    ]

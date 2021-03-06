# Generated by Django 3.2.6 on 2021-10-06 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SanctionAdd',
            fields=[
                ('ent_num', models.PositiveIntegerField()),
                ('add_num', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('address', models.TextField()),
                ('address_more', models.TextField()),
                ('country', models.TextField()),
                ('add_remarks', models.TextField()),
            ],
            options={
                'db_table': 'sanction_add',
            },
        ),
        migrations.CreateModel(
            name='SanctionAlt',
            fields=[
                ('ent_num', models.PositiveIntegerField()),
                ('alt_num', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('alt_type', models.TextField()),
                ('alt_remarks', models.TextField()),
            ],
            options={
                'db_table': 'sanction_alt',
            },
        ),
        migrations.CreateModel(
            name='SanctionMain',
            fields=[
                ('ent_num', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='제재번호')),
                ('sdn_name', models.TextField()),
                ('sdn_type', models.CharField(max_length=20)),
                ('program', models.TextField()),
                ('title', models.TextField()),
                ('call_sign', models.CharField(max_length=20)),
                ('vess_type', models.TextField()),
                ('tonnage', models.CharField(max_length=20)),
                ('grt', models.CharField(max_length=10)),
                ('vess_flag', models.CharField(max_length=50)),
                ('vess_owner', models.CharField(max_length=200)),
                ('remarks', models.TextField()),
                ('is_sdn', models.CharField(max_length=2)),
            ],
            options={
                'db_table': 'sanction_main',
            },
        ),
    ]

# Generated by Django 3.2.6 on 2021-10-14 02:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uploader.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=uploader.utils.rename_file_to_uuid, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['tif', 'jpeg'])])),
                ('description', models.TextField(null=True)),
                ('uploaded_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
    ]

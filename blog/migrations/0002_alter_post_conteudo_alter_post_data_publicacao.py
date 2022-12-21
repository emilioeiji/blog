# Generated by Django 4.1.4 on 2022-12-21 04:40

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

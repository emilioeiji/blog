# Generated by Django 4.1.4 on 2023-02-23 21:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_post_data_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='conteudo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]

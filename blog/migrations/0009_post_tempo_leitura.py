# Generated by Django 4.1.4 on 2023-02-24 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_tag_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tempo_leitura',
            field=models.CharField(default=30, max_length=2),
        ),
    ]
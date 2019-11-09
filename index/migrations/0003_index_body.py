# Generated by Django 2.0 on 2019-10-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_index_information_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index_Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_body_name', models.CharField(max_length=50)),
                ('blog_body_time', models.DateTimeField(auto_now_add=True)),
                ('blog_body_context', models.TextField()),
                ('blog_body_type_1', models.CharField(max_length=15)),
                ('blog_body_type_2', models.CharField(max_length=15)),
            ],
        ),
    ]

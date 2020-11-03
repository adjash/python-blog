# Generated by Django 3.1.3 on 2020-11-03 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=500)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 2.1 on 2018-08-04 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trvl_app', '0002_auto_20180803_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Miasto')),
            ],
            options={
                'verbose_name': 'Miasto',
                'verbose_name_plural': 'Miasta',
            },
        ),
        migrations.AlterField(
            model_name='travel',
            name='topic',
            field=models.CharField(max_length=100, verbose_name='Tytuł'),
        ),
    ]
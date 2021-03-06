# Generated by Django 3.2.3 on 2021-06-20 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userr', '0003_auto_20210617_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userr.register')),
            ],
        ),
    ]

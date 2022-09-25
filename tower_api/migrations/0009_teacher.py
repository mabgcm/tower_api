# Generated by Django 4.1.1 on 2022-09-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tower_api', '0008_material_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('F', 'female'), ('M', 'male')], default='male', max_length=1)),
                ('adress', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('photo', models.ImageField(blank=True, upload_to='profile_pics/')),
                ('apply_date', models.DateField(auto_now_add=True)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
# Generated by Django 4.1.1 on 2022-09-24 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tower_api', '0003_alter_material_event_link_alter_material_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.CharField(max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tower_api.course')),
            ],
        ),
    ]
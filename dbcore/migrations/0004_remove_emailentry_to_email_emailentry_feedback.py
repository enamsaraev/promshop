# Generated by Django 4.2.4 on 2023-09-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0003_alter_mainpage_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emailentry',
            name='to_email',
        ),
        migrations.AddField(
            model_name='emailentry',
            name='feedback',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='emailentries', to='dbcore.feedback'),
        ),
    ]

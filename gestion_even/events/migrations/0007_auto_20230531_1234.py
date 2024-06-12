# Generated by Django 2.2.28 on 2023-05-31 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20230531_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='ticket',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='events.Ticket'),
        ),
    ]
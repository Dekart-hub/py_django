# Generated by Django 4.1.5 on 2023-03-23 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('comment', models.CharField(max_length=256, null=True)),
                ('ord_date', models.DateTimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='dish',
            old_name='weight',
            new_name='ccal',
        ),
        migrations.RemoveField(
            model_name='dish',
            name='products',
        ),
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='dish',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='dishes/'),
        ),
        migrations.DeleteModel(
            name='Cook',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='order',
            name='dish_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.dish'),
        ),
        migrations.AddField(
            model_name='order',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

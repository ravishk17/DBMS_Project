# Generated by Django 2.2 on 2019-04-05 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aid', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=150)),
                ('description', models.TextField(blank=True, max_length=264)),
                ('products', models.TextField(blank=True, max_length=150)),
                ('shop_pic', models.FileField(blank=True, upload_to='documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('aid', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.Admin')),
                ('tid', models.ForeignKey(default=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='shop.Admin'), on_delete=django.db.models.deletion.CASCADE, to='shop.Tenant')),
            ],
        ),
    ]

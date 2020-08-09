# Generated by Django 3.0.7 on 2020-08-09 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcuser', '0003_fcuser_useremail'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='수량')),
                ('register_date', models.DateTimeField(auto_now_add=True, verbose_name='등록시간')),
                ('fcuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fcuser.Fcuser', verbose_name='사용자')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='상품')),
            ],
            options={
                'verbose_name': '주문',
                'verbose_name_plural': '주문',
                'db_table': 'fc_order',
            },
        ),
    ]

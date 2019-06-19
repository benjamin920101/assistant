# Generated by Django 2.1.3 on 2019-06-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='支出金額'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.IntegerField(choices=[(0, '未分類'), (1, '飲食'), (2, '衣服'), (3, '交通'), (4, '教育'), (5, '娛樂'), (99, '其它')], default=0, verbose_name='支出類別'),
        ),
    ]

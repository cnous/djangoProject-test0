# Generated by Django 4.1 on 2022-08-29 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cinema',
            name='images',
            field=models.ImageField(upload_to='cinema_posters/', verbose_name='عکس '),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='showtime',
            name='status',
            field=models.IntegerField(choices=[(1, 'فروش آغاز نشده'), (2, 'در حال فروش بلیت'), (3, 'بلیت\u200cها تمام شد'), (4, 'فروش بلیت بسته شد'), (5, 'فیلم پخش شد'), (6, 'سانس لغو شد')]),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_count', models.IntegerField(verbose_name='تعداد صندلی')),
                ('order_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان خرید')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.profile', verbose_name='خریدار')),
                ('showtime', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ticketing.showtime', verbose_name='سانس')),
            ],
            options={
                'verbose_name': 'بلیت',
                'verbose_name_plural': 'بلیت',
            },
        ),
    ]
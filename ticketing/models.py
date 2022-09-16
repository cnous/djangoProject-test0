from django.db import models

# Create your models here.

class Movie(models.Model):
    class Meta:
        verbose_name = 'movie'
    name = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    length = models.IntegerField()
    year = models.IntegerField()
    description = models.TextField(null=True)
    poster = models.ImageField('پوستر', upload_to="movie_posters/")

    def __str__(self):
        return self.name

class Cinema(models.Model):
    class Meta:
        verbose_name = 'cinema'
    cinema_code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    capacity = models.IntegerField()
    phone = models.CharField(max_length=11, null=True)
    address = models.TextField()
    images = models.ImageField('عکس ', upload_to="cinema_posters/")
    #blank=True add a delete parameter in django admin

    def __str__(self):
        return self.name

class Showtime (models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.PROTECT)
    cinema = models.ForeignKey('Cinema', on_delete=models.PROTECT)
    start_time = models.DateTimeField()
    price = models.IntegerField('قیمت')
    salable_seat = models.IntegerField()
    free_seat = models.IntegerField()
    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت‌ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )
    status = models.IntegerField(choices=status_choices)

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)

    def get_price_display(self):
        return '{} تومان'.format(self.price)

    def reserve_seats(self, seat_count):
        assert isinstance(seat_count, int) and seat_count > 0, 'Number of seats should be a positive integer'
        assert self.status == Showtime.SALE_OPEN, 'Sale is not open'
        assert self.free_seat >= seat_count, 'Not enough free seats'
        self.free_seat -= seat_count
        if self.free_seat == 0:
            self.status = Showtime.TICKETS_SOLD
        self.save()

class Ticket(models.Model):
    class Meta:
        verbose_name = 'بلیت'
        verbose_name_plural = 'بلیت'
    showtime = models.ForeignKey('Showtime', on_delete=models.PROTECT, verbose_name='سانس')
    customer = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, verbose_name='خریدار')
    seat_count = models.IntegerField('تعداد صندلی')
    order_time = models.DateTimeField('زمان خرید', auto_now_add=True)

    def __str__(self):
        return "{} بلیت به نام {} برای فیلم {}".format(self.seat_count, self.customer, self.showtime.movie)


from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


PAY_OPT = (
    ('cash','Cash'),
    ('cards','Cards'),
    ('mblbnk','Mobile Banking'),
)
Discount = (
    ('percent','Percent'),
    ('flat','Flat'),
)
size_type = (
    ('foot','Foot'),
    ('meter','Meter'),
)
RATING = (
    (1, '★☆☆☆☆'),
    (2, '★★☆☆☆'),
    (3, '★★★☆☆'),
    (4, '★★★★☆'),
    (5, '★★★★★'),
)
doc_type = (
    ('nid','NID Card'),
    ('passport','Passport'),
)
Prk_type = (
    ('selfprk','Self Parking'),
)


class country(models.Model):
    name = models.CharField( max_length=50,unique=True)
    def __str__(self):
        return self.name

class services_cat(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    

class facilities(models.Model):
    category = models.ManyToManyField(services_cat,max_length=30)
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name


class services(models.Model):
    name = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name




# class options(models.Model):
#     category
#     meal_plans
#     free_opt
#     paid_opt

class room_cat(models.Model):
    name = models.CharField(max_length=50)
    persons = models.PositiveIntegerField()
    def __str__(self):
        return self.name
    
class room_view(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class furniture(models.Model):
    name = models.CharField( max_length=50)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.name
class bed_option(models.Model):
    name = models.CharField( max_length=50)
    quantity = models.PositiveIntegerField()
    def __str__(self):
        return self.name

class faq(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=300)
    def __str__(self):
        return self.question

class hotelroom(models.Model):
    room_cat = models.OneToOneField(room_cat, on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    size_type = models.CharField(choices=size_type,max_length=5,null=True,blank=True)
    room_size = models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    room_view = models.ForeignKey(room_view,on_delete=models.DO_NOTHING)
    windows = models.PositiveIntegerField()
    bed_opt = models.ForeignKey(bed_option,on_delete=models.DO_NOTHING)
    ac = models.BooleanField()
    bedsheets = models.BooleanField(default=True)
    celing_fan = models.BooleanField(default=True)
    extra_fan = models.BooleanField(default=False)
    extra_bed = models.BooleanField(default=False)
    wifi = models.BooleanField(default=True)
    furniture = models.ManyToManyField(furniture,blank=True)
    balcony = models.BooleanField(default=False)
    balcony_size = models.PositiveIntegerField()
    def __str__(self):
        return self.room_cat.name

class check_in_rqm(models.Model):
    payment = models.CharField(max_length=100,null=True,blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    documents = models.CharField(choices=doc_type,max_length=20,null=True,blank=True)
    extras = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.payment

class hotel(models.Model):
    unique_id = models.PositiveIntegerField(unique=True)
    vendor = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='name',unique=True)
    image = models.ImageField(upload_to='hotels/',default='default/default.png')
    country = models.ForeignKey(country,on_delete=models.DO_NOTHING)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    road = models.TextField()
    gmap_link = models.TextField(null=True,blank=True)
    rating = models.IntegerField(choices=RATING)
    rooms = models.ForeignKey(hotelroom, on_delete=models.CASCADE)

    payment_option = models.CharField(choices=PAY_OPT,max_length=10)
    discount = models.CharField(choices=Discount,max_length=10)
    # review = models.ForeignKey

    services = models.ManyToManyField(services)
    facilities = models.ManyToManyField(facilities)
    pets = models.BooleanField()
    parking = models.CharField(choices=Prk_type,max_length=20)
    
    
    check_in_rqm = models.OneToOneField(check_in_rqm,on_delete=models.DO_NOTHING)
    policies = models.TextField()
    faq = models.OneToOneField(faq,blank=True,null=True,on_delete=models.DO_NOTHING)
    hotel_created_at = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField( auto_now_add=True)
    Updated_at = models.DateField( auto_now_add=True)
    def __str__(self):
        return self.name


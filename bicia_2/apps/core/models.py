from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Max

# Create your models here.

EVENT_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

CYCLIST_CATEGORIES = (
    ('P', 'Principiante'),
    ('I', 'Intermedia'),
    ('A', 'Avanzada'),
)

SIZE_OPTIONS  = (
    ('S', 'Small'),
    ('M', 'Medium'),
    ('L', 'Large'),
    ('XL', 'X Large'),
    ('XXL', 'XX Large'),
)

PACKAGE_OPTIONS  = (
    ('D', 'Entregado'),
    ('U', 'Pendiente'),
)

SUSCRIPTION_STATUS  = (
    ('A', 'Accepted'),
    ('P', 'In Process'),
)

class Event(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    cost = models.DecimalField(max_digits=10, decimal_places=3)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    category =  models.CharField(max_length=1, choices=EVENT_CATEGORIES, default='P')
    suscriptions =  models.PositiveIntegerField(default=0)
    medals = models.PositiveIntegerField(default=0)
    jerseys = models.PositiveIntegerField(default=0)
    left_medals = models.PositiveIntegerField(default=0)
    left_jerseys = models.PositiveIntegerField(default=0)
    left_suscriptions = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.name


class Cyclist(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, db_index=True)
    secondlastname = models.CharField(max_length=50)
    email = models.EmailField(db_index=True)
    age = models.PositiveIntegerField()
    birthday = models.DateField() 
    created = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=50)
    category = models. CharField(max_length=1, choices=CYCLIST_CATEGORIES, default='P')
    alias = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    emergency_phone = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s %s' % (self.firstname, self.lastname, self.secondlastname)



class Suscription(models.Model):
    user= models.ForeignKey(User)
    event = models.ForeignKey(Event)
    cyclist = models.ForeignKey(Cyclist)
    number = models.PositiveIntegerField()
    jersey = models.BooleanField(default=False)
    medal = models.BooleanField(default=False)
    ride = models.BooleanField(default=False)    
    size = models.CharField(max_length=1, choices=SIZE_OPTIONS, default='L')
    package = models.CharField(max_length=1, choices=PACKAGE_OPTIONS, default='U')
    status = models.CharField(max_length=1, choices=SUSCRIPTION_STATUS, default='U')

    class Meta:
      unique_together = (('event', 'number'), ('event', 'cyclist'))

    def __str__(self):
        return '%s %s' % (self.number, self.cyclist)

    def save(self, *args, **kwargs):
      max_num = Suscription.objects.filter(event=self.event).aggregate(Max('number'))
      self.num  = max_num + 1
      super(Suscription, self).save(*args, **kwargs)
      if self.jersey:
        self.event.left_jerseys -= 1
      if self.medal:
        self.event.left_medals -= 1

      self.event.left_suscriptions -= 1
      self.event.save()


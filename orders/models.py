from django.db import models

# Create your models here.

class Order(models.Model):
    name  = models.CharField(max_length=30)
    drink = models.CharField(max_length=30)
    extra = models.CharField(max_length=30, default="", blank=True)
    ready = models.BooleanField(default=False)
    submitted_date = models.DateTimeField('Order submitted time')

    def __str__(self):
        if self.ready is True:
            state = "Done"
        else:
            state = "Todo"


        if self.extra is "":
            return '{0}: {1} ({2}) -- {3}'.format(self.name, self.drink, self.submitted_date.time().strftime('%H:%M'), state)
        else:
            return '{0}: {1} ({2}/{4}) -- {3}'.format(self.name, self.drink, self.submitted_date.time().strftime('%H:%M'), self.ready, state)

        # return self.from_text + ": " + self.order_text + ()
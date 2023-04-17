from django.db import models

# Create your models here.

class login(models.Model):
     username=models.CharField(max_length=100)
     password=models.CharField(max_length=100)
     type=models.CharField(max_length=20)


class staff(models.Model):
     name=models.CharField(max_length=100)
     place=models.CharField(max_length=100)
     post=models.CharField(max_length=100)
     pin=models.CharField(max_length=100)
     email=models.CharField(max_length=100)
     phone_number=models.CharField(max_length=100)
     photo=models.CharField(max_length=100)
     gender=models.CharField(max_length=100)
     type=models.CharField(max_length=20)
     LOGIN=models.ForeignKey(login, on_delete=models.CASCADE)


class user(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    


class donation(models.Model):
     donation_type=models.CharField(max_length=100)
     date=models.CharField(max_length=100)
     description=models.CharField(max_length=200)
    #  type=models.CharField(max_length=20)

class payment(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=200)
    # type = models.CharField(max_length=20)



class marriage(models.Model):
    USER=models.ForeignKey(user, on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    groom_name=models.CharField(max_length=100)
    bride_name=models.CharField(max_length=100)
    groom_address=models.CharField(max_length=100)
    bride_address=models.CharField(max_length=100)
    no_guest=models.CharField(max_length=100)
    # type=models.CharField(max_length=100)

class confession(models.Model):
    USER=models.ForeignKey(user, on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    #type=models.CharField(max_length=100)

class baptism(models.Model):
    USER=models.ForeignKey(user, on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    no_guest = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class sermons(models.Model):
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class prayerdetails(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class events(models.Model):
    event_name=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class funddetails(models.Model):
    amount=models.CharField(max_length=100)
    expenditure=models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class participation(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    EVENTS=models.ForeignKey(events, on_delete=models.CASCADE)
    award=models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class eventreport(models.Model):
    STAFF = models.ForeignKey(user, on_delete=models.CASCADE)
    EVENTS = models.ForeignKey(events, on_delete=models.CASCADE)
    description=models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

class complaint(models.Model):
    USER = models.ForeignKey(user, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    # type = models.CharField(max_length=100)

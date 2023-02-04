from django.db import models

# Create your models here.


class Persone(models.Model):
    name = models.CharField("Фамилия Имя Отчество", max_length=50)

    def __str__(self):
        return self.name

    def all_phones_to_string(self):
        return ", ".join([phone.phone for phone in self.phones.all()])
    
    def all_email_to_string(self):
        return ", ".join([email.email for email in self.emails.all()])



class Phone(models.Model):
    phone = models.CharField("Телефон", max_length=50)
    contact = models.ForeignKey(Persone,
                                on_delete=models.CASCADE,
                                related_name="phones")

    def __str__(self):
        return self.phone

class Email(models.Model):
    email = models.CharField("Электронная почта", max_length=50)
    contact = models.ForeignKey(Persone,
                                on_delete=models.CASCADE,
                                related_name="emails")

    def __str__(self):
        return self.email
    

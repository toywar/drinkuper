# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.forms import ModelForm

class PassedDrinkup(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    comments = models.TextField()
    passed = models.BooleanField(default=True)

    class MetaPassedDrinkup:
        ordering = ('-time',)

class RequestDrinkup(models.Model):
    date = models.CharField(max_length=50, verbose_name=u'Date')
    name = models.CharField(max_length=50, verbose_name=u'Name')
    location = models.CharField(max_length=50, verbose_name=u'Location')
    comments = models.TextField(verbose_name=u'Comments')

    class Meta:
        verbose_name = ('Request drinkup')
        verbose_name_plural = ('Requests drinkups')
    def __unicode__(self):
        return self.name

class RequestForm(ModelForm):
    class Meta:
        model = RequestDrinkup

#todo: release feedback form
#class Contact(models.Model):
#    subject = models.CharField(max_length=100, verbose_name=u'Subject:')
#    name = models.CharField(max_length=50, verbose_name=u'Name:')
#    mail = models.EmailField(verbose_name=u'E-Mail:')
#    text = models.TextField(verbose_name=u'Message:')
#
#    class Meta:
#        verbose_name = ('Contact')
#        verbose_name_plural = ('Contacts')
#    def __unicode__(self):
#        return self.subject
#
#class ContactForm(ModelForm):
#    class Meta:
#        model = Contact

class PassedDrinkupAdmin(admin.ModelAdmin):
    list_display = ('time', 'name', 'location', 'comments')

class RequestDrinkupAdmin(admin.ModelAdmin):
    list_display = ('date', 'name', 'location', 'comments')

admin.site.register(PassedDrinkup, PassedDrinkupAdmin)
admin.site.register(RequestDrinkup)
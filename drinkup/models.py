from django.db import models, connection
from django.contrib import admin

class PassedDrinkup(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    comments = models.TextField()
    passed = models.BooleanField(default=True)

    class MetaPassedDrinkup:
        ordering = ('-time',)

# todo: rebuild class
class RequestDrinkup(models.Model):
    time = models.DateTimeField()
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    comments = models.TextField()

    class MetaRequestDrinkup:
        ordering = ('time',)

class RequestDrinkupAdmin(admin.ModelAdmin):
     list_display = ('time', 'name', 'location', 'comments')

class PassedDrinkupAdmin(admin.ModelAdmin):
     list_display = ('time', 'name', 'location', 'comments')

#TODO: add database connector
#def DatabaseConnector():
#    cursor = connection.cursor()
#    cursor.execute("SELECT * FROM drinkup_passeddrinkup")
#    row = cursor.fetchone()
#    return row

admin.site.register(RequestDrinkup, RequestDrinkupAdmin)
admin.site.register(PassedDrinkup, PassedDrinkupAdmin)

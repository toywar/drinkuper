from django.db import connection

def DatabaseConnector():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM drinkup_passeddrinkup")
    row = cursor.fetchone()
    return row
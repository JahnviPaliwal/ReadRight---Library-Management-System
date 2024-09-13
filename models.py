from django.db import models

class Bookadd(models.Model):
    book_name  = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_stock = models.IntegerField()
    book_desc = models.TextField()



class Issue(models.Model):
    student_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.IntegerField()
    book_name = models.CharField(max_length=100)
    issue_date = models.CharField(max_length=100)
    date_submm = models.CharField(max_length=100)








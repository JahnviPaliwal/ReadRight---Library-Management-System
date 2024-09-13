from django.shortcuts import render,redirect

from .models import *


def main_p(request):
    return render(request , "main_p.html")

def bookadd(request):
    if request.method == "POST":
        data = request.POST
        book_name = data.get("book_name")
        book_author = data.get("book_author")
        book_stock = data.get("book_stock")
        book_desc = data.get("book_desc")


        Bookadd.objects.create(
            book_name = book_name,
            book_author=book_author,
            book_stock=book_stock,
            book_desc = book_desc,

        )

        return redirect("/bookadd/")


    return render(request, "bookadd.html")

def orderlist_book(request):
    query_set = Bookadd.objects.all()
    context = {'bookadd': query_set}
    return render(request, 'orderlist_book.html', context)

# Create your views here.
def issue(request):
    if request.method == "POST":
        data = request.POST
        student_name = data.get("student_name")
        department = data.get("department")
        year = data.get("year")
        book_name = data.get("book_name")
        issue_date = data.get("issue_date")
        date_submm = data.get("date_submm")


        Issue.objects.create(
            student_name = student_name,
            department=department,
            year=year,
            book_name = book_name,
            issue_date=issue_date,
            date_submm = date_submm,
        )

        return redirect("/issue/")

    query_set = Issue.objects.all()
    context = {'issue': query_set}

    return render(request, 'issue.html',context)

def delete_issue(request,id):
    queryset = Issue.objects.get(id = id)
    queryset.delete()

    return redirect("/issue/")





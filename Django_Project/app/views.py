from django.shortcuts import render, HttpResponse, redirect
from .models import Record, Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required # 必須要在使用者登入的情況下才能使用
def hello(request):
    # return HttpResponse('hello')
    title = '何哲平的Flask'
    return render(request,'app\hello.html', {'title':title})

@login_required # 必須要在使用者登入的情況下才能使用
def frontpage_(request):
    return render(request,'app\index_.html', {})

@login_required # 必須要在使用者登入的情況下才能使用
def frontpage(request):
    record_form = RecordForm(initial={'balance_type':'支出'})
    records = Record.objects.filter() # 取得某一範圍資料
    income_list = [record.cash for record in records if record.balance_type == '收入']
    outcome_list = [record.cash for record in records if record.balance_type == '支出']
    income = sum(income_list) if len(income_list) != 0 else 0
    outcome = sum(outcome_list) if len(outcome_list) != 0 else 0
    net = income - outcome
    # return render(request,'app\index.html', {'records':records, 'income':income, 'outcome':outcome, 'net':net})
    return render(request, 'app\index.html', locals()) # locals -> 拿取所有變數 (取得在這個function底下所有的變數)

@login_required # 必須要在使用者登入的情況下才能使用
def settings(request):
    categories = Category.objects.filter()
    return render(request, 'app\settings.html', locals())

@login_required # 必須要在使用者登入的情況下才能使用
def addCategory(request):
    if request.method == "POST":
        posted_data = request.POST
        category = posted_data["add_category"]
        Category.objects.get_or_create(category=category)
    return redirect("/settings")

@login_required # 必須要在使用者登入的情況下才能使用
def deleteCategory(request, category):
    Category.objects.filter(category=category).delete() # 刪除一筆資料
    return redirect("/settings")

@login_required # 必須要在使用者登入的情況下才能使用
def addRecord(request):
    if request.method == "POST":
        form = RecordForm(request.POST)
        if form.is_valid(): form.save()
    return redirect("/")

@login_required # 必須要在使用者登入的情況下才能使用
def deleteRecord(request):
    if request.method == "POST":
        id = request.POST["delete_val"]
        Record.objects.filter(id=id).delete() # 刪除一筆資料
    return redirect("/")
from django.shortcuts import render
from django.http import HttpResponse
# from .models import Food

def calorie(request):
    # 各モデルから全ての要素を呼び出す
    # foods = Food.object.all()
    # motions = Motion.object.all()
    context = {
        # 'foods': foods,
        # 'motions': motions,
    }
    return render(request,'acsys_system/calorie/save_calorie.html',context)
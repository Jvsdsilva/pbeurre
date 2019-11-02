from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import RegistrationForm
from django import forms
from django.http import HttpResponse
from django.template import loader
from aliments.models import Products
from aliments.models import Foodsave
from aliments import dbInsert
from aliments import dbRequests
from django.contrib.auth.models import User


# go to home
def index(request):
    # dbInsert.insertCategory()
    # dbInsert.insertStore()
    # dbInsert.insertProducts()
    template = loader.get_template('Aliments/index.html')
    return HttpResponse(template.render(request=request))


# loged in
def login(request):
    template = loader.get_template('Aliments/user.html')
    return HttpResponse(template.render(request=request))


# redirect to user connected page
def connected(request):
    template = loader.get_template('Aliments/aliments.html')
    return HttpResponse(template.render(request=request))


# logout user
def logout(request):
    template = loader.get_template('Aliments/index.html')
    return HttpResponse(template.render(request=request))


# Create new user
def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login')
    else:
        form = RegistrationForm()

        return render(request, 'Aliments/signup.html', {'form': form})


# request results
def results(request):
    result_res = []
    search = request.POST.get('searchbtn', None)
    query_index = request.POST['query_index']
    query_nav = request.POST['query_nav']

    if search == 'searchbtn':
        if query_index != "" or query_nav != "":
            if query_index != "":
                query = query_index

            if query_nav != "":
                query = query_nav

            results = dbInsert.get_Results(query)
        else:
            text = "Veiullez saisir un produit"
            return render(request, 'Aliments/index.html', {'text': text})

    if len(results) == 0:
        text = "Nous n'avons pas ce produit, veiullez reessayer!"
        return render(request, 'Aliments/results.html', {'text': text})
    else:
        for result in results:
            contexts = {}
            contexts['id'] = result.id
            contexts['nameAlim'] = result.nameAlim
            contexts['image'] = result.image
            contexts['nutritionGrade'] = result.nutritionGrade

            result_res.append(contexts)
        # print(result_res)
        return render(request, 'Aliments/results.html',
                      {'results': result_res})


# redirect to page details for a specific product
def results_details(request, pk):
    obj_aliment = Products.objects.get(pk=pk)

    context = {
        'id': obj_aliment.id,
        'image': obj_aliment.image,
        'nameAlim': obj_aliment.nameAlim,
        "descriptionAlim": obj_aliment.descriptionAlim,
        "nutritionGrade": obj_aliment.nutritionGrade
    }

    return render(request, 'Aliments/results_details.html', context)


# page os products
def aliment(request):

    foodsave = request.POST.get('foodsavebtn', None)

    if foodsave == 'foodsavebtn':
        pk = request.POST['id']
        current_user = request.user

        obj_aliment = Products.objects.get(pk=pk)

        obj_user = User(id=current_user.id)

        dbInsert.insertFoodsave(obj_aliment, obj_user)
    current_user_id = request.user
    saved_products = dbInsert.get_saved_products(current_user_id.id)

    if len(saved_products) == 0:
        text = "Vous n'avez pas de produits enregistrées!"
        return render(request, 'Aliments/aliments.html', {'text': text})
    else:
        args = {'foodsave': saved_products}

        return render(request, 'Aliments/aliments.html', args)


# page os condictions
def mentions(request):
    template = loader.get_template('Aliments/mentions.html')
    return HttpResponse(template.render(request=request))


# page contact
def contact(request):
    template = loader.get_template('Aliments/based.html')
    return HttpResponse(template.render(request=request))

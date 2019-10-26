from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from aliments.models import Products
from aliments import dbInsert
from aliments import dbRequests
# views.py
from django.shortcuts import redirect
from .forms import RegistrationForm

def index(request):
    template = loader.get_template('Aliments/index.html')
    return HttpResponse(template.render(request=request))


def results(request):
    # get query from user
    # call treatement to show results
    #context = {}
    result_res= []
    search = request.POST.get('searchbtn',None)
    query_index = request.POST['query_index']
    query_nav = request.POST['query_nav']
    #print(query_index)
    #print(query_nav)
    """context['searchbtn'] = search
    context['query_index'] = query_index
    context['query_nav'] = query_nav"""
    
    if query_index !="":
        query = query_index
    
    if query_nav !="":
        query = query_nav

    results = dbInsert.get_Results(query)

    if len(results) == 0:
        text = "Nous n'avons pas ce produit, veiullez reessayer!"
        return render(request, 'Aliments/results.html', {'text': text}) 
    else:
        for result in results:
            contexts = {}
            contexts['nameAlim'] = result.nameAlim
            contexts['image'] = result.image
            contexts['nutritionGrade'] = result.nutritionGrade

            result_res.append(contexts)
            # print(result_res)
        return render(request, 'Aliments/results.html', {'results': result_res})


def results_details(request):
    """aliment = Products.objects.get(pk=id_alim)
    context = {
        'nameAlim': aliment.nameAlim,
        "descriptionAlim": aliment.description_ingred,
        "nutritionGrade": aliment.nutrition_grades
    }"""
    return render(request, 'Aliments/results_details.html')
   

"""def logout(request):
    template = loader.get_template('Aliments/index.html')
    return HttpResponse(template.render(request=request))"""


"""def login(request):

    template = loader.get_template('Aliments/user.html')
    return HttpResponse(template.render(request=request))"""


def signup(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('Aliments/index.html')
    else:
        form = RegistrationForm()

    #template = loader.get_template('Aliments/signup.html')
    #return HttpResponse(template.render(request=request))
    return render(request, 'Aliments/signup.html', {'form': form})

def aliment(request):
    # request = dbRequests.DbRequests()
    # Create store list
    # category_list = request.Request_categories()
    # print(category_list)
    # products_list = request.Request_products()
    # print(products_list)
    # Call bulk_create to create records in a single call
    # Category.objects.bulk_create(category_list)

    # dbInsert.insertCategory()
    # dbInsert.insertStore()
    # dbInsert.insertProducts()

    # print(products_list)

    template = loader.get_template('Aliments/aliments.html')
    return HttpResponse(template.render(request=request))


def mentions(request):
    template = loader.get_template('Aliments/mentions.html')
    return HttpResponse(template.render(request=request))


def contact(request):
    template = loader.get_template('Aliments/based.html')
    return HttpResponse(template.render(request=request))


def listing(request):
    """albums = ["<li>{}</li>".format(album['name']) for album in ALBUMS]
    message = <ul>{}</ul>.format("\n".join(albums))
    return HttpResponse(message)"""


def detail(request, album_id):
    """id = int(album_id) # make sure we have an integer.
    album = ALBUMS[id] # get the album with its id.
    artists = " ".join([artist['name'] for artist in album['artists']]) # grab artists name and create a string out of it.
    message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
    return HttpResponse(message)"""


def search(request):
    query = request.GET.get('query')
    if not query:
        message = "Aucun artiste n'est demandé"
    else:
        albums = [
            album for album in ALBUMS
            if query in " ".join(artist['name'] for artist in album['artists'])
        ]

        if len(albums) == 0:
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]
            message = """
                Nous avons trouvé les albums correspondant à votre requête ! Les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)

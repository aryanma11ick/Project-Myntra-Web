from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


# homepage/views.py
from django.shortcuts import render

def home(request):
    # Define the categories to display
    categories = [
        "Kurtas & Suits",
        "Kurtis, Tunics & Tops",
        "Sarees",
        "Ethnic Wear",
        "Dresses",
        "Tops",
        "Tshirts",
        "Jeans",
    ]
    
    # Render the homepage with categories
    return render(request, 'homepage/home.html', {'categories': categories})


# # Create your views here.
# def index(request):
#     return HttpResponse("Hello World")


# def index(request):
#     html_page='myapp\index.html'
#     return render(request,html_page)


#sending data from back end to the front end
#create var context to pass the data and assign everything to it


# def index(request):
#     html_page='myapp\home.html'
#     product= { 'image_url':"https://assets.myntassets.com/dpr_2,q_60,w_210,c_limit,fl_progressive/assets/images/25892106/2024/10/24/1aaf1645-3589-4aee-80de-3ed6ff7df3751729768804020-HM-Ruched-Sleeve-Wrap-Dress-5241729768803665-1.jpg"  ,
#                'product_link': "https://www.myntra.com/dresses/h%26m/hm-ruched-sleeve-wrap-dress/25892106/buy",
#                'product_name': "ABC"

#     }

#     return render(request, html_page, {'product':product})

# df_product_info = pd.read_csv(r"D:\Project Myntra Web\products.csv")

# def index(request):
#     html_page = "myapp\home.html"
#     #print(df_product_info)
#     df_data= df_product_info.to_dict(orient='records')
#     context= {'product_data':df_data}
#     print(df_data)
#     return render(request, html_page,context)

# def home(request):
#     return HttpResponse("From Home")

# def product_grid(request):

#     products = df[['id', 'product_name', 'image_url']].to_dict(orient='records')
#     html_page = 'app/product_grid.html'
#     return render(request, html_page, {'products': products})

# def product_details(request, product_id, sortBy="popularity"):
#     html_page = 'myapp/product_details.html'
#     product= []
#     print(df_product_info['id'][0])
#     x=df_product_info['id'][0]
#     print(type(x))
#     product = df_product_info[df_product_info['id'] == product_id].to_dict(orient='records')
#     # print(product)
#     # print(product_id,type(product_id))
#     if product:
#         product = product[0]
#     else:
#         product = None
    
#     return render(request, html_page, {'product':product})


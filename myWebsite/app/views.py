from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import pandas as pd

# views.py
def home(request):
    return render(request, 'home.html')

def category_page(request, category_name):
    # Get sort-by parameter from the URL (default to popularity)
    sort_by = request.GET.get('sort_by', 'popularity')
    print(category_name)
    file_map = {
        'popularity': f'{category_name}_popularity.csv',
        'new': f'{category_name}_new.csv',
        'discount': f'{category_name}_discount.csv',
        'rating': f'{category_name}_Customer%20rating.csv',
    }

    csv_file = file_map.get(sort_by)
    products = []
    print(csv_file)

    # Read data from the corresponding CSV file using pandas
    if csv_file:
        try:
            df = pd.read_csv(f'C:/Users/Aryan/Documents/Projects/mamun-intership/Project-Myntra-Web/Project-Myntra-Web/{csv_file}')  # Replace `path_to_csv` with your actual folder path
            products = df.to_dict('records')  # Convert DataFrame to a list of dictionaries
            

        except FileNotFoundError:
            products = []  # Handle missing CSV files gracefully

    context = {
        'category_name': category_name,
        'products': products,
        'sort_by': sort_by,
    }
    return render(request, 'category_page.html', context)

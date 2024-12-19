from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
import pandas as pd

# views.py
def home(request):
    return render(request, 'home.html')

def category_page(request, category_name):
    # Category names mapping
    category_names = {
        'kurtas-and-suits': 'Kurtas & Suits',
        'kurtis-tunics-tops': 'Kurtis, Tunics and Tops',
        'sarees': 'Sarees',
        'ethnic-wear': 'Ethnic Wear',
        'dresses': 'Dresses',
        'tops': 'Tops',
        'tshirts': 'Tshirts',
        'jeans': 'Jeans'
    }

    # Get the display name or use 'Unknown Category' if not found
    display_name = category_names.get(category_name, 'Unknown Category')

    # Get the sort-by parameter (default to 'popularity')
    sort_by = request.GET.get('sort_by', 'popularity')

    # File mapping for different sorts
    file_map = {
        'popularity': f'{category_name}_popularity.csv',
        'new': f'{category_name}_new.csv',
        'discount': f'{category_name}_discount.csv',
        'rating': f'{category_name}_Customer%20rating.csv',
    }

    # Get the CSV file based on the sort option
    csv_file = file_map.get(sort_by)
    products = []

    # Read data from the CSV file using pandas
    if csv_file:
        try:
            df = pd.read_csv(f'C:/Users/Aryan/Documents/Projects/mamun-intership/Project-Myntra-Web/Project-Myntra-Web/{csv_file}')
            products = df.to_dict('records')  # Convert the DataFrame to a list of dictionaries
        except FileNotFoundError:
            products = []  # If the CSV file is not found, return an empty list

    # Context to pass to the template
    context = {
        'category_name': category_name,
        'display_name': display_name,
        'products': products,
        'sort_by': sort_by,
    }

    return render(request, 'category_page.html', context)

def product_page(request, category_name, product_id):
    # Get the sort_by parameter from the URL query string (default to 'popularity')
    sort_by = request.GET.get('sort_by', 'popularity')  # Default to 'popularity'

    # File mapping for different sorts (for the product's CSV file)
    file_map = {
        'popularity': f'{category_name}_popularity.csv',
        'new': f'{category_name}_new.csv',
        'discount': f'{category_name}_discount.csv',
        'rating': f'{category_name}_Customer%20rating.csv',
    }

    # Get the CSV file for the selected sort option
    csv_file = file_map.get(sort_by)
    print(f"Loading CSV: {csv_file} for sort by {sort_by}")

    # Try to load the CSV file for the category
    product = None
    if csv_file:
        try:
            df = pd.read_csv(f'C:/Users/Aryan/Documents/Projects/mamun-intership/Project-Myntra-Web/Project-Myntra-Web/{csv_file}')
            # Search for the product by its product_id
            product = df[df['id'] == int(product_id)].to_dict('records')
            if product:
                product = product[0]  # If product is found, get the first record
        except FileNotFoundError:
            product = None  # If CSV is not found, return None

    # Context to pass to the template
    context = {
        'product': product if product else None,
        'sort_by': sort_by,  # Pass the sort_by to the template
        'category_name': category_name,
    }

    return render(request, 'product_page.html', context)
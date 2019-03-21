from django.shortcuts import render

from .documents import ProductDocument


def search_products(request):
    query = request.GET.get('q')
    results = None

    if query:
        results = ProductDocument.search().query(
            "multi_match", query=query, fields=["name", "description"]
        )

    context = {
        'results': results
    }
    return render(request, 'search/search_products.html', context)

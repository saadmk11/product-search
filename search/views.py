from django.shortcuts import render

from .documents import ProductDocument


def search_products(request):
    query = request.GET.get('q')
    results = None

    if query:
        search = ProductDocument.search().query(
            "multi_match", query=query, fields=["name", "description"]
        )
        results = search.execute()

    context = {
        'results': results
    }
    return render(request, 'search/search_products.html', context)

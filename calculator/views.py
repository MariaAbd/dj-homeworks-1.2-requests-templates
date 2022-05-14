from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'butter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def all_recipes(request):
    context = {'data': DATA}
    return render(request, 'all_recipes.html', context)


def recipy(request, dish):
    servings = request.GET.get('servings')
    context = {'data': DATA[dish]}
    if servings is not None:
        for ingredient, amount in DATA[dish].items():
            amount = amount * int(servings)
            DATA[dish][ingredient] = amount
    return render(request, 'recipes.html', context)

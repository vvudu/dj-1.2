from django.http import HttpResponse
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
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, dish):
   
    servings = request.GET.get('servings', 1) 
    try:
        servings = int(servings)
    except ValueError:
        servings = 1

    # Получаем данные рецепта
    recipe = DATA.get(dish)
    if recipe is None:
        return HttpResponse(f"Рецепт для {dish} не найден.", status=404)

    # Умножаем количество ингредиентов на количество порций
    scaled_recipe = {ingredient: amount * servings for ingredient, amount in recipe.items()}

    # Контекст для шаблона
    context = {
        'recipe': scaled_recipe,
        'dish': dish,
        'servings': servings
    }

    # Отправляем данные в шаблон
    return render(request, 'calculator/index.html', context)
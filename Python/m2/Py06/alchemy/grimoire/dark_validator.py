from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    the_ingred = dark_spell_allowed_ingredients()
    for ingred in the_ingred:
        if ingred in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

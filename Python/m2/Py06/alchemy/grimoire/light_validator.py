from alchemy.grimoire import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    the_ingred = light_spellbook.light_spell_allowed_ingredients()
    for ingred in the_ingred:
        if ingred in ingredients.lower():
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"

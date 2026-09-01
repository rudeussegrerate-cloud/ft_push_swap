

def light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from alchemy.grimoire.light_validator import validate_ingredients
    return (f"{spell_name} "
            f"({validate_ingredients(ingredients)})")

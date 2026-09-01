#!/usr/bin/env python3
import alchemy.grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    print("Testing record light spell: Spell recorded: ", end="")
    print(alchemy.grimoire.light_spell_record("Fantasy",
                                              "Earth, wind and fire"))

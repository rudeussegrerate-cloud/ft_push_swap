"""Exercise 0: Space Station Data Validation using Pydantic v2."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    """Pydantic model for validating space station data."""

    station_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Unique station identifier (3-10 chars)",
    )
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Station name (1-50 chars)",
    )
    crew_size: int = Field(
        ...,
        ge=1,
        le=20,
        description="Number of crew members (1-20)",
    )
    power_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Power level percentage (0.0-100.0)",
    )
    oxygen_level: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Oxygen level percentage (0.0-100.0)",
    )
    last_maintenance: datetime = Field(
        ...,
        description="DateTime of last maintenance",
    )
    is_operational: bool = Field(
        default=True,
        description="Whether station is operational",
    )
    notes: Optional[str] = Field(
        default=None,
        max_length=200,
        description="Optional notes (max 200 chars)",
    )


def display_station(station: SpaceStation) -> None:
    """Display station information in a readable format."""
    status = "Operational" if station.is_operational else "Offline"
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    print(f"Status: {status}")


def main() -> None:
    """Demonstrate SpaceStation model validation."""
    print("Space Station Data Validation")
    print("=" * 40)

    # --- Valid station ---
    valid_station = SpaceStation(
        station_id="ISS001",
        name="International Space Station",
        crew_size=6,
        power_level=85.5,
        oxygen_level=92.3,
        last_maintenance=datetime(2024, 1, 15, 8, 30, 0),
        is_operational=True,
        notes="All systems nominal.",
    )
    display_station(valid_station)

    print("=" * 40)

    # --- Invalid station (crew_size > 20) ---
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="BAD001",
            name="Overcrowded Station",
            crew_size=99,  # violates le=20
            power_level=50.0,
            oxygen_level=80.0,
            last_maintenance=datetime(2024, 1, 15, 8, 30, 0),
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

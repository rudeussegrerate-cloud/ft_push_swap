"""Exercise 2: Space Crew Management with nested Pydantic models."""

from datetime import datetime
from enum import Enum
from typing import List

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(str, Enum):
    """Enum for crew member ranks."""

    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    """Pydantic model for an individual crew member."""

    member_id: str = Field(
        ...,
        min_length=3,
        max_length=10,
        description="Member identifier (3-10 chars)",
    )
    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Full name (2-50 chars)",
    )
    rank: Rank = Field(
        ...,
        description="Crew member rank",
    )
    age: int = Field(
        ...,
        ge=18,
        le=80,
        description="Age in years (18-80)",
    )
    specialization: str = Field(
        ...,
        min_length=3,
        max_length=30,
        description="Area of expertise (3-30 chars)",
    )
    years_experience: int = Field(
        ...,
        ge=0,
        le=50,
        description="Years of experience (0-50)",
    )
    is_active: bool = Field(
        default=True,
        description="Whether crew member is active",
    )


class SpaceMission(BaseModel):
    """Pydantic model for a space mission with nested crew list."""

    mission_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Mission identifier (5-15 chars, must start with M)",
    )
    mission_name: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Mission name (3-100 chars)",
    )
    destination: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Mission destination (3-50 chars)",
    )
    launch_date: datetime = Field(
        ...,
        description="Planned launch date and time",
    )
    duration_days: int = Field(
        ...,
        ge=1,
        le=3650,
        description="Mission duration in days (1 to 3650)",
    )
    crew: List[CrewMember] = Field(
        ...,
        min_length=1,
        max_length=12,
        description="List of crew members (1-12)",
    )
    mission_status: str = Field(
        default="planned",
        description="Current mission status",
    )
    budget_millions: float = Field(
        ...,
        ge=1.0,
        le=10000.0,
        description="Budget in millions of dollars (1.0-10000.0)",
    )

    @model_validator(mode="after")
    def validate_mission_rules(self) -> "SpaceMission":
        """Apply safety and operational rules after field validation."""
        # Rule 1: mission_id must start with "M"
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")

        # Rule 2: must have at least one Commander or Captain
        senior_ranks = {Rank.commander, Rank.captain}
        has_senior = any(m.rank in senior_ranks for m in self.crew)
        if not has_senior:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: long missions need 50% experienced crew (5+ years)
        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            ratio = experienced / len(self.crew)
            if ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need at least 50%"
                    " crew with 5+ years experience"
                )

        # Rule 4: all crew members must be active
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise ValueError(
                f"All crew must be active. Inactive: {', '.join(inactive)}"
            )

        return self


def display_mission(mission: SpaceMission) -> None:
    """Display mission details in a readable format."""
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"  - {member.name} ({member.rank.value})"
            f" - {member.specialization}"
        )


def main() -> None:
    """Demonstrate SpaceMission model with nested CrewMember validation."""
    print("Space Mission Crew Validation")
    print("=" * 40)

    # --- Build crew members ---
    sarah = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.commander,
        age=40,
        specialization="Mission Command",
        years_experience=15,
        is_active=True,
    )
    john = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.lieutenant,
        age=32,
        specialization="Navigation",
        years_experience=8,
        is_active=True,
    )
    alice = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.officer,
        age=28,
        specialization="Engineering",
        years_experience=5,
        is_active=True,
    )

    # --- Valid mission ---
    valid_mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date=datetime(2024, 6, 1, 9, 0, 0),
        duration_days=900,
        crew=[sarah, john, alice],
        mission_status="planned",
        budget_millions=2500.0,
    )
    display_mission(valid_mission)

    print("=" * 40)

    # --- Invalid mission: no Commander or Captain ---
    print("Expected validation error:")
    try:
        cadet1 = CrewMember(
            member_id="CM010",
            name="Bob Lee",
            rank=Rank.cadet,
            age=22,
            specialization="Science",
            years_experience=1,
            is_active=True,
        )
        cadet2 = CrewMember(
            member_id="CM011",
            name="Eva Green",
            rank=Rank.officer,
            age=25,
            specialization="Medicine",
            years_experience=2,
            is_active=True,
        )
        SpaceMission(
            mission_id="M2024_BAD",
            mission_name="Doomed Mission",
            destination="Jupiter",
            launch_date=datetime(2024, 7, 1, 9, 0, 0),
            duration_days=200,
            crew=[cadet1, cadet2],  # no Commander or Captain
            budget_millions=500.0,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

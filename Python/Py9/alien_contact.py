"""Exercise 1: Alien Contact Logs with custom @model_validator."""

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(str, Enum):
    """Enum for types of alien contact."""

    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    """Pydantic model for validating alien contact reports."""

    contact_id: str = Field(
        ...,
        min_length=5,
        max_length=15,
        description="Contact identifier (5-15 chars, must start with AC)",
    )
    timestamp: datetime = Field(
        ...,
        description="DateTime of the contact event",
    )
    location: str = Field(
        ...,
        min_length=3,
        max_length=100,
        description="Location of contact (3-100 chars)",
    )
    contact_type: ContactType = Field(
        ...,
        description="Type of alien contact",
    )
    signal_strength: float = Field(
        ...,
        ge=0.0,
        le=10.0,
        description="Signal strength on 0.0-10.0 scale",
    )
    duration_minutes: int = Field(
        ...,
        ge=1,
        le=1440,
        description="Duration in minutes (1 min to 24 hours)",
    )
    witness_count: int = Field(
        ...,
        ge=1,
        le=100,
        description="Number of witnesses (1-100)",
    )
    message_received: Optional[str] = Field(
        default=None,
        max_length=500,
        description="Optional received message (max 500 chars)",
    )
    is_verified: bool = Field(
        default=False,
        description="Whether the contact has been verified",
    )

    @model_validator(mode="after")
    def validate_contact_rules(self) -> "AlienContact":
        """Apply business rules after field-level validation."""
        # Rule 1: contact_id must start with "AC"
        if not self.contact_id.startswith("AC"):
            raise ValueError(
                "Contact ID must start with 'AC' (Alien Contact)"
            )

        # Rule 2: physical contact must be verified
        if (
            self.contact_type == ContactType.physical
            and not self.is_verified
        ):
            raise ValueError("Physical contact reports must be verified")

        # Rule 3: telepathic contact needs at least 3 witnesses
        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses"
            )

        # Rule 4: strong signals (> 7.0) should include a message
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def display_contact(contact: AlienContact) -> None:
    """Display contact report in a readable format."""
    print("Valid contact report:")
    print(f"ID: {contact.contact_id}")
    print(f"Type: {contact.contact_type.value}")
    print(f"Location: {contact.location}")
    print(f"Signal: {contact.signal_strength}/10")
    print(f"Duration: {contact.duration_minutes} minutes")
    print(f"Witnesses: {contact.witness_count}")
    if contact.message_received:
        print(f"Message: '{contact.message_received}'")


def main() -> None:
    """Demonstrate AlienContact model validation."""
    print("Alien Contact Log Validation")
    print("=" * 38)

    # --- Valid contact ---
    valid_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp=datetime(2024, 3, 15, 22, 45, 0),
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    display_contact(valid_contact)

    print("=" * 38)

    # --- Invalid: telepathic with only 1 witness ---
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime(2024, 3, 16, 10, 0, 0),
            location="Roswell, New Mexico",
            contact_type=ContactType.telepathic,
            signal_strength=5.0,
            duration_minutes=10,
            witness_count=1,  # violates rule: needs >= 3
            is_verified=False,
        )
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

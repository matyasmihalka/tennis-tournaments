from unicodedata import category
import pytest

from tournaments.models import Tournaments, Registration


@pytest.mark.django_db
def test_torunaments_model():
    tournament = Tournaments(
        category="START",
        event_date="2022-02-04T09:00:00Z",
        place="Test place",
        prestige=100,
        surface="CLAY",
        capacity=16,
        price=1000,
    )
    tournament.save()
    assert tournament.category == "START"
    assert tournament.event_date == "2022-02-04T09:00:00Z"
    assert tournament.place == "Test place"
    assert tournament.prestige == 100
    assert tournament.surface == "CLAY"
    assert tournament.capacity == 16
    assert tournament.price == 1000
    assert tournament.status == "OPEN"
    assert tournament.created
    assert tournament.updated
    # assert (
    #     str(tournament)
    #     == f"Tournament of category {tournament.category} on {tournament.event_date} at {tournament.place}"
    # )


@pytest.mark.django_db
def test_registrations_model(create_user, add_tournament):
    user = create_user()
    tournament = add_tournament()
    registration = Registration(user=user, tournament=tournament, status="REGISTERED")
    registration.save()
    assert registration.user == user
    assert registration.tournament == tournament
    assert registration.status == "REGISTERED"
    assert registration.registered_on
    assert registration.cancelled_on == None

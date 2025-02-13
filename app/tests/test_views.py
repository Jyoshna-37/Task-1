import pytest
from django.urls import reverse
from app.models import Candidate


@pytest.mark.django_db
def test_candidate_list(client):
    # Create a user
    Candidate.objects.create(name='Jyoshna', email='jyoshna@gmail.com', experience=5)
    Candidate.objects.create(name='Veekshitha', email='veekshitha@gmail.com', experience=1)

    response = client.get(reverse('candidate_list'))

    assert response.status_code == 200
    data = response.json()
    assert "candidates" in data
    assert len(data["candidates"]) == 2
    assert data["candidates"][0]["name"] == "Jyoshna"
    assert data["candidates"][1]["email"] == "veekshitha@gmail.com"
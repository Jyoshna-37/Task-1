import pytest
from app.models import Candidate


@pytest.mark.django_db
def test_is_experienced():
    candidate_experieced = Candidate.objects.create(name='Jyoshna', email='jyoshna@gmail.com', experience=5)
    candidate_inexperieced =  Candidate.objects.create(name='Veekshitha', email='veekshitha@gmail.com', experience=1)

    assert candidate_experieced.is_experienced() is True
    assert candidate_inexperieced.is_experienced() is False
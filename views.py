from django.shortcuts import render
from django.http import JsonResponse
from .models import Candidate

# Create your views here.

def candidate_list(request):
    candidates = list(Candidate.objects.values('name', 'email', 'experience'))
    return JsonResponse({'candidates': candidates}, safe=False)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

# views
@login_required()
def index(request, *args, **kwargs):
  template = 'pets/index.html'
  context = {
    'year': datetime.now().year,
  }

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

"""
function for displaying the portal homepage when a user logs in
"""


@login_required
def index_view(request):
    if request.user.is_authenticated:

        template_name = 'portal/index.html'

        return render(request, template_name, {})
    else:
        messages.warning(request, 'You have to login to access the portal')
        return redirect('login')



from django.http import HttpResponse

from django.shortcuts import redirect


def unauthnticated_user(view_func):
	def wrapper_func(request, *args, **kwarags):
		if request.user.is_authenticated:
			return redirect('home')
		else:
			return view_func(request, *args, **kwarags)

	return wrapper_func



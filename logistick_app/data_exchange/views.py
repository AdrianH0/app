from django.shortcuts import render
from data_exchange.models import Orders
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from data_exchange.forms import Orders
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# @csrf_exempt
class Login(View):
	def get(self, request):
		return render(request, 'login.html')
	def post(self, request):
		username = request.POST.get('username')
		password = request.POST.get('password')
		try:
			user = authenticate(username=username, password=password)
			# user = User.objects.get(username=username, password=password)
			if username in ('adrianh'):
				return HttpResponseRedirect("/orders")
			else:
				return HttpResponseRedirect("/partner")
			# response = HttpResponse("Zalogowano")
			#
			# response.set_cookie('logged_in', value=username, max_age=86400)
		# return response
		except User.DoesNotExist:
			response = HttpResponse("Błąd logowania")
			response.delete_cookie('logged_id')
			return response


class Manager(LoginRequiredMixin, View):
	login_url = '/login/'
	def get(self, request):
		orders = Orders.objects.all()
		return render(request, 'orders_view.html', {'orders': orders})
	# def get(self, request):
	# 	orders = Orders.objects.all()
	# 	ctx = {
	# 		'orders': orders
	# 	}
	# 	return render(request, 'orders_view.html', ctx)
	#
	# @csrf_exempt
	# def post(self, request):
	# 	status = request.POST.get('order_id')
	# 	order = Orders.objects.get(order_id=status)
	# 	order.order_status = request.POST.get('status')
	# 	order.save()

class Partner(LoginRequiredMixin, View):
	login_url = '/login/'
	pass


class ChangeStatus(LoginRequiredMixin, View):
	login_url = '/login/'
	def post(self, request):
		form = Orders(request.POST)
		if form.is_valid():
			order_id = request.POST.get('order_id')
			order_status = request.POST.get('status_field')
			t = Orders.objects.get(order_id=order_id)
			t.order_status = order_status
			t.save()
			return HttpResponseRedirect("/orders")
				# HttpResponse("Order status changed!")
				# HttpResponseRedirect("/orders")
				#render(request, 'change_status.html', {'form': form})
	def get(self, request):
		form = Orders()
		return render(request, 'change_status.html', {'form': form})
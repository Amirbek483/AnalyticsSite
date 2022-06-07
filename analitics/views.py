from django.shortcuts import render,redirect
from .forms import *

def send_analytics_file(request):
		if request.method == 'POST':
				form = AnalyticsForm(request.POST, request.FILES)
				if form.is_valid():
						form.save()
						return redirect('result')
		else:
				form = AnalyticsForm()
		return render(request, 'analitics.html', {'form': form})
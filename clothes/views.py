from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import *
from clothes.models import *
from clothesliner.functions import *

def home(request):
	q = Designer.objects.all()
	r = {}
	for designer in q:
		s = Pant.objects.filter(designer__exact=designer).values('style').distinct()
		r[designer] = Style.objects.filter(id__in=s)
	return render_to_response('templates/home.html', {'designers':q, 'styles':r}, context_instance=RequestContext(request))

def results(request):
	waist = request.POST.get('waist')
	inseam = request.POST.get('inseam')
	designer = request.POST.get('designers')
	style = request.POST.get('style')
	
#	reference_pant = find_pants(designer, style, waist, inseam)
	compare_measurements = {"waist": waist, "inseam": inseam}
	compare_margin_of_error = {"waist": 2, "inseam": 3}
	acceptable_pants = compare_pants(compare_measurements, compare_margin_of_error, "")
	
	return render_to_response('templates/results.html', {'pants': acceptable_pants}, context_instance=RequestContext(request))

def product_info(request):
	return HttpResponse("product info")
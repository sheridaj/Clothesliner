from clothes.models import *

def compare_pants(reference_measurements, reference_margins_of_error, reference_flags):
	q = Pant.objects.all()
	for category, measurement in reference_measurements.items():
		measurement = float(str(measurement))
		moe = reference_margins_of_error[category]
		kwargs = {'%s__%s' % (category, 'range'): (measurement-moe, measurement+moe)}
		q = q.filter(**kwargs)
	return q 
	
#def find_pants(designer, style, waist, inseam):
#	q = Pant.objects.filter(designer__exact=designer)
#	q = q.filter(style__exact=style)
#	q = q.filter(waist__exact=waist)
#	q = q.filter(inseam__exact=inseam)
#	return q if q.exists() else return 
from clothes.models import *

def compare_pants(reference_measurements, reference_margins_of_error, reference_flags):
	q = Pant.objects.all()
#	q1 = q.filter(waist__range=(1,40))
	for category, measurement in reference_measurements.items():
		measurement = float(str(measurement))
		moe = reference_margins_of_error[category]
		kwargs = {'%s__%s' % (category, 'range'): (measurement-moe, measurement+moe)}
		q1 = q.filter(**kwargs)
	return q
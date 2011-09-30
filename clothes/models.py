from django.db import models

class Fabric(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Fly(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Closure(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Weave(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Origin(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Treatment(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Pocket_Style(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Pocket_Location(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Certification(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Gender(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Color(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Pattern(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Style(models.Model):
	name = models.CharField(max_length=200)
	def __unicode__(self):
	        return self.name

class Designer(models.Model):
	name = models.CharField(max_length=200)
	webAddress = models.URLField(null=True, blank=True)
	def __unicode__(self):
	        return self.name

class Retailer(models.Model):
	name = models.CharField(max_length=200)
	webAddress = models.URLField(null=True, blank=True)
	def __unicode__(self):
	        return self.name

class Item(models.Model):
	primary_color = models.ForeignKey(Color, null=True, blank=True, related_name="primary_color")
	secondary_color = models.ForeignKey(Color, null=True, blank=True, related_name="secondary_color")
	gender = models.ForeignKey(Gender, null=True, blank=True)
	designer = models.ForeignKey(Designer, null=True, blank=True)
	manufacturing_location = models.ForeignKey(Origin, null=True, blank=True, related_name='manufacture_location')
	organic = models.NullBooleanField()
	certification = models.ForeignKey(Certification, null=True, blank=True)
	
	class Meta:
		abstract = True

class Cloth_Item(Item):
	fabric = models.ForeignKey(Fabric, null=True, blank=True)
	fabric_dimensions = models.FloatField(null=True, blank=True)
	weave = models.ForeignKey(Weave, null=True, blank=True)
	cut_on_bias = models.NullBooleanField()
	preshrunk = models.NullBooleanField()
	material_origin = models.ForeignKey(Origin, null=True, blank=True, related_name='material_origin')
	treatment = models.ForeignKey(Treatment, null=True, blank=True)
	pattern = models.ForeignKey(Pattern, null=True, blank=True)
	pattern_thickness = models.FloatField(null=True, blank=True)
	pattern_gap_size = models.FloatField(null=True, blank=True)
	
	class Meta:
		abstract = True

class Pant(Cloth_Item):
	waist = models.FloatField(null=True, blank=True)
	front_rise = models.FloatField(null=True, blank=True)
	back_rise = models.FloatField(null=True, blank=True)
	hips = models.FloatField(null=True, blank=True)
	inseam = models.FloatField(null=True, blank=True)
	thigh = models.FloatField(null=True, blank=True)
	knee = models.FloatField(null=True, blank=True)
	outseam = models.FloatField(null=True, blank=True)
	cuff = models.FloatField(null=True, blank=True)
	cuff_unfinished = models.NullBooleanField()
	rear_pocket_quantity = models.IntegerField(null=True, blank=True)
	rear_pocket_depth = models.FloatField(null=True, blank=True)
	rear_pocket_breadth = models.FloatField(null=True, blank=True)
	rear_pocket_style = models.ForeignKey(Pocket_Style, null=True, blank=True, related_name="rear_style")
	cargo_pocket_quantity = models.IntegerField(null=True, blank=True)
	cargo_pocket_depth = models.FloatField(null=True, blank=True)
	cargo_pocket_breadth = models.FloatField(null=True, blank=True)
	hidden_pocket_quantity = models.IntegerField(null=True, blank=True)
	hidden_pocket_location = models.ForeignKey(Pocket_Location, null=True, blank=True)
	change_pocket_quantity = models.IntegerField(null=True, blank=True)
	front_pocket_quantity = models.IntegerField(null=True, blank=True)
	front_pocket_style = models.ForeignKey(Pocket_Style, null=True, blank=True, related_name="front_style")
	front_pocket_depth = models. FloatField(null=True, blank=True)
	front_pocket_breadth = models.FloatField(null=True, blank=True)
	pleat_number = models.IntegerField(null=True, blank=True)
	belt_loop_quantity = models.IntegerField(null=True, blank=True)
	belt_loop_height = models.FloatField(null=True, blank=True)
	belt_loop_breadth = models.FloatField(null=True, blank=True)
	rivets = models.NullBooleanField()
	fly = models.ForeignKey(Fly, null=True, blank=True)
	closure = models.ForeignKey(Closure, null=True, blank=True)
	waistband_curve = models.NullBooleanField()
	style = models.ForeignKey(Style, null=True, blank=True)
	def __unicode__(self):
		a = "" if self.designer is None else self.designer.name
		b = "" if self.style is None else self.style.name
		c = "" if self.waist is None else self.waist
		d = "" if self.inseam is None else self.inseam
		return a+" "+b+" "+c+" "+d if a+b+c+d != "" else "Some Pants"
	
class Pant_Stock_Item(models.Model):
	item = models.ForeignKey(Pant)
	retailer = models.ForeignKey(Retailer)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	url_link = models.URLField(null=True)
	inventory_number = models.IntegerField(null=True)
	dateAdded = models.DateTimeField()
	current = models.BooleanField()
	preferred = models.BooleanField()

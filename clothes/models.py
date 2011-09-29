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
	webAddress = models.URLField()
	def __unicode__(self):
	        return self.name

class Retailer(models.Model):
	name = models.CharField(max_length=200)
	webAddress = models.URLField()
	def __unicode__(self):
	        return self.name

class Item(models.Model):
	primary_color = models.ForeignKey(Color, null=True, related_name="primary_color")
	secondary_color = models.ForeignKey(Color, null=True, related_name="secondary_color")
	gender = models.ForeignKey(Gender, null=True)
	designer = models.ForeignKey(Designer, null=True)
	manufacturing_location = models.ForeignKey(Origin, null=True)
	organic = models.NullBooleanField()
	certification = models.ForeignKey(Certification, null=True)
	
	class Meta:
		abstract = True

class Cloth_Item(models.Model):
	fabric = models.ForeignKey(Fabric, null=True)
	fabric_dimensions = models.FloatField(null=True)
	weave = models.ForeignKey(Weave, null=True)
	cut_on_bias = models.NullBooleanField()
	preshrunk = models.NullBooleanField()
	material_origin = models.ForeignKey(Origin, null=True)
	treatment = models.ForeignKey(Treatment, null=True)
	pattern = models.ForeignKey(Pattern, null=True)
	pattern_thickness = models.FloatField(null=True)
	pattern_gap_size = models.FloatField(null=True)
	
	class Meta:
		abstract = True

class Pant(Item):
	waist = models.FloatField(null=True)
	front_rise = models.FloatField(null=True)
	back_rise = models.FloatField(null=True)
	hips = models.FloatField(null=True)
	inseam = models.FloatField(null=True)
	thigh = models.FloatField(null=True)
	knee = models.FloatField(null=True)
	outseam = models.FloatField(null=True)
	cuff = models.FloatField(null=True)
	cuff_unfinished = models.NullBooleanField()
	rear_pocket_quantity = models.IntegerField(null=True)
	rear_pocket_depth = models.FloatField(null=True)
	rear_pocket_breadth = models.FloatField(null=True)
	rear_pocket_style = models.ForeignKey(Pocket_Style, null=True, related_name="rear_style")
	cargo_pocket_quantity = models.IntegerField(null=True)
	cargo_pocket_depth = models.FloatField(null=True)
	cargo_pocket_breadth = models.FloatField(null=True)
	hidden_pocket_quantity = models.IntegerField(null=True)
	hidden_pocket_location = models.ForeignKey(Pocket_Location, null=True)
	change_pocket_quantity = models.IntegerField(null=True)
	front_pocket_quantity = models.IntegerField(null=True)
	front_pocket_style = models.ForeignKey(Pocket_Style, null=True, related_name="front_style")
	front_pocket_depth = models. FloatField(null=True)
	front_pocket_breadth = models.FloatField(null=True)
	pleat_number = models.IntegerField(null=True)
	belt_loop_quantity = models.IntegerField(null=True)
	belt_loop_height = models.FloatField(null=True)
	belt_loop_breadth = models.FloatField(null=True)
	rivets = models.NullBooleanField()
	fly = models.ForeignKey(Fly, null=True)
	closure = models.ForeignKey(Closure, null=True)
	waistband_curve = models.NullBooleanField()
	style = models.ForeignKey(Style, null=True)
	def __unicode__(self):
	        return self.designer.name+" "+self.style.name

class Pant_Stock_Item(models.Model):
	item = models.ForeignKey(Pant)
	retailer = models.ForeignKey(Retailer)
	price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
	url_link = models.URLField(null=True)
	inventory_number = models.IntegerField(null=True)
	dateAdded = models.DateTimeField()
	current = models.BooleanField()
	preferred = models.BooleanField()

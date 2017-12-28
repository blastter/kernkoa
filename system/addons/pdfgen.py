from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter, legal
from reportlab.pdfbase.pdfmetrics import stringWidth
import math
class pdfGenerator:
	
	c = None
	height = None
	width = None
	
	marginLeft = 5
	marginBottom = 8
	
	def __init__(self, file, pagesize=None):
		if pagesize == None:
			pagesize = letter
		self.width, self.height = pagesize
		#print self.height
		#print self.width
		self.c = canvas.Canvas(file, pagesize = pagesize)
		
	def addString(self,left, bottom, text, font = None, size = None, maxwidth = None, maxlines = None):
		if font != None and size != None:
			self.c.setFont(font, size)
		self.c.drawString(left+(self.marginLeft*mm), bottom-(self.marginBottom*mm), text)
	
	def addParagraph(self, left, bottom, text, font, size, maxwidth, minleft, maxlines=None, vals = None):
		lineHeight = 13
		if maxlines == None:
			maxlines = 1
		lines = []
		while len(lines) <= maxlines:
			if len(lines) > 0:
				left = minleft
			print str(stringWidth(text, font, size) + left) + " - " + str(maxwidth)
			if stringWidth(text, font, size) + left > maxwidth:
				#print len(text)
				maxlen = int(math.floor(len(text) * maxwidth/(stringWidth(text, font, size) + left)))
				if "firstline" in vals and len(lines) == 0:
					maxlen = vals["firstline"]
				elif "charline" in vals and len(lines) > 0:
					maxlen = vals["charline"]
				self.addString(left, bottom - (len(lines) * lineHeight), text[:maxlen], font, size, maxwidth, maxlines)
				lines.append(text[:maxlen])
				text = text[maxlen:]
			else:
				self.addString(left, bottom - (len(lines) * lineHeight), text, font, size, maxwidth, maxlines)
				lines.append(text)
			#print len(lines)
		if len(lines)>0:
			return True
		return False
	
	def addParagraphPluss(self, text, vals):
		lines = []
		while len(lines) < vals["lines"]:
			if len(text) >= vals["firstline"] and len(lines) == 0:
				lines.append(text[:vals["firstline"]])
				self.addString(vals["left"], vals["bottom"], text[:vals["firstline"]], vals["font"], vals["fontsize"])
				text = text[vals["firstline"]:]
			elif len(text) >= vals["charline"]:
				
				self.addString(vals["minleft"], vals["bottom"] - (len(lines)*vals['lineheight']), text[:vals["charline"]], vals["font"], vals["fontsize"])
				text = text[vals["charline"]:]
				lines.append(text[:vals["charline"]])
			else:
				self.addString(vals["minleft"], vals["bottom"] - (len(lines)*vals['lineheight']), text, vals["font"], vals["fontsize"])
				lines.append(text)
			
	
	def save(self):
		self.c.save()
	
	def genFormat(self, data, format):
		for key,val in format.iteritems():
			if key in data:
				if "lines" in format:
					maxlines = format["lines"]
				else:
					maxlines = 1
				#print key
				#print repr(val)
				#print data[key]
				if "lines" in val:
					#self.addParagraph(val["left"], val["bottom"], data[key], val["font"], val["fontsize"], val["maxwidth"], 44, maxlines, val)
					if len(data[key]) <= val["firstline"]:
						self.addString(val["left"], val["bottom"], data[key], val["font"], val["fontsize"])
					else:
						self.addParagraphPluss(data[key], val)
				else:
					self.addString(val["left"], val["bottom"], data[key], val["font"], val["fontsize"])
				#self.addString(val["left"], val["bottom"], data[key], val["font"], val["fontsize"], val["maxwidth"], maxlines)
	def newPage(self):
		self.c.showPage()
		
#from pdfgen import *
#test = pdfGenerator("/usr/local/sacservices/test.pdf")
#test.addString(33,233,"Albin Trotter E.")
#test.save()
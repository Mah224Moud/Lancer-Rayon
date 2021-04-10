# coding=utf-8
import os
import sys
from PIL import Image, ImageDraw, ImageFont


def interpole( x1, y1, x2, y2, x) :
        # x=x1 -> y=y1
        # x=x2 -> y=y2
        return (x-x2)/(x1-x2)*y1 + (x-x1)/(x2-x1)*y2

class boite:
	def __init__(self, boleft, upright):
		self.boleft = boleft
		self.upright = upright
# box se cree par boite( (xleft, ybottom), (xright, yup))

class viewport:
	def __init__(self, boxworld, boxscreen):
		self.world=boxworld
		self.screen=boxscreen
	def toworld( self,x,y):
		xworld= interpole( float(self.screen.boleft[0]), float(self.world.boleft[0]), 
			float(self.screen.upright.boleft[0]), float(self.world.upright.boleft[0]), float(x))
		yworld= interpole( float(self.screen.boleft[1]), float(self.world.boleft[1]), 
			float(self.screen.upright.boleft[1]), float(self.world.upright.boleft[1]), float(y))
		return (xworld, yworld)
	def toscreen( self, x,y):
		xscreen = interpole( float(self.world.boleft[0]), float(self.screen.boleft[0]), 
			float(self.world.upright[0]), float(self.screen.upright[0]), float(x))
		yscreen= interpole( float(self.world.boleft[1]), float(self.screen.boleft[1]), 
			float(self.world.upright[1]), float(self.screen.upright[1]), float(y))
		return (int(xscreen), int(yscreen))

# viewport( boxworld, boxscreen)
view= viewport( boite( (-1., -1.), (1., 1.) ), boite( (0., 399.), (399., 0.)))
img=Image.new("RGB", (400,400), (255,255,255))
c = ImageDraw.Draw(img) # c pour canvas

def milieuX( x1,x2):
	return float((x1+x2))/2.

def sierpinski( niv, x0,y0, x1,y1, x2,y2):
	if 0==niv:
		(i0, j0)= view.toscreen( x0,y0)	
		(i1, j1)= view.toscreen( x1,y1)	
		(i2, j2)= view.toscreen( x2,y2)	
		c.polygon(  [ (i0, j0), (i1, j1), (i2, j2)], fill=None, outline=(0,0,0))
	else:
		sierpinski( niv-1, x0,y0, milieuX(x0,x1), milieuX(y1,y2), milieuX(x0, x2), milieuX(y0, y2))
		sierpinski( niv-1, x1,y1, milieuX( x1,x0), milieuX(y1, y0), milieuX( x1, x2), milieuX(y1, y2))
		sierpinski( niv-1, x2,y2, milieuX( x2,x0), milieuX(y2, y0), milieuX( x2,x1), milieuX(y2, y1))

sierpinski( 11, -2., -1., 2., -1., 0., 1.)
#sierpinski( 10, -1., -1., 1., -1., 0., 1.)

img.show()
img.save( "sierpinski.png")

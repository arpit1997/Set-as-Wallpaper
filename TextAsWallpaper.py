import os
import platform
import cairosvg
from subprocess import call
string_quote = input('Enter The Text ')
background = input('Enter background colour ')
text_colour = input('Enter Text colour ')
text_stroke = input('Enter Text stroke ')
font_name = input('Enter font name ')
font_size = input('Enter font size(px) ') 
svg_template1 = '''<svg height="1080" width="1920" >
	<rect x="0" y="0" height="1080" width="1920" style="fill:{};stroke:black" />
	<text x="960" y="540" 
		text-anchor="middle" font-weight="bold" font-size="{}" 
		lengthAdjust="spacingAndGlyphs" 
		style="fill:{};stroke:{};font-family: {} font-weight: normal; font-style: normal" >
		{}
	</text>
</svg>'''
s = []
for i in string_quote:
	s.append('&#')
	s.append(str(ord(i)))
	s.append(';')
quote = ''.join(s)
svg_template1 = svg_template1.format(background,font_size,text_colour,text_stroke,font_name,quote)
svg = open('wallpaper.svg','w')
svg.write(svg_template1)
svg.close() 
desktop_enviorment = os.environ['XDG_CURRENT_DESKTOP']
if desktop_enviorment == "unity":
	call(["gsettings","set","org.gnome.desktop.background","picture-uri","file://"+os.getcwd()+"/"+"wallpaper.svg"])

import json
import os
import click

@click.command()
@click.argument('source')
@click.argument('target')

def startcode(source, target):
	""" Converts Sloth annotation file to input file for OpenCV Haar cascade
		classifier.
	"""
	
	file = open(source, 'r')
	data = json.load(file)
	
	with open(target, 'w') as fo:

		for prvek in data:

			try:
			
				if prvek["annotations"]:

					name = prvek['filename'] 
					prefix = "pos_raw/"
					rsl = name[len(prefix):] if name.startswith(prefix) else name
					line_str = "{0} {1}".format(rsl, len(prvek["annotations"]))

					for rect in prvek["annotations"]:
				
						height = int(rect['height'])
						width = int(rect['width'])
						x = int(rect['x'])
						y = int(rect['y'])
						line_str += " {0} {1} {2} {3}".format(x, y, width, height)

					line_str += "\n"
					fo.write(line_str)


			except KeyError:
				pass


	fo.close()


if __name__ == '__main__':
    startcode()

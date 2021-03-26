#Importing all the libraries needed
import os
import tempfile	#creates temporary file to contain .ppm image files for fast i/o
from pdf2image import convert_from_path	#converts pdfs to images
from PIL import Image 	#supports opening, manipulating and saving images
import pytesseract	#converts written content of an image or file to text
from gtts import gTTS 	#Google Translate's text-to-speech API



#this is our pdf file
filename= 'The_Last_Leaf.pdf'
#this is the directory where we will store the images from the pdf file
#C:\Users\mauryashashish\Text-to-Speech\auxiliary
save_dir= os.path.join(os.path.dirname(os.path.realpath('main.py')),'auxiliary')



#generating image files for the pages from our pdf file for first two pages
with tempfile.TemporaryDirectory() as path:
    images_from_path = convert_from_path(filename, poppler_path=r'C:\Program Files\poppler-21.03.0\Library\bin', output_folder=save_dir)



#setting up pytesseract
pytesseract.pytesseract.tesseract_cmd= r'C:\Program Files\Tesseract-OCR\tesseract.exe'



#extracting the text from ppm images into a txt file
file = open((os.path.join(save_dir,'output.txt')),'w')
i=1
for image in images_from_path:
	name= str(i)+'.jpeg'
	image.save(os.path.join(save_dir,name),'jpeg')
	i+=1
	file.write(pytesseract.image_to_string(Image.open(os.path.join(save_dir,name))))
file.close()



#converting the txt file into an mp3 file using Google text-to-speech
file= open(os.path.join(save_dir,'output.txt'),'r')
txt= file.read()
tts= gTTS(text= txt, lang='en')
tts.save('finalaudio.mp3')
file.close()



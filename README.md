# Text-to-Speech-Conversion
This repository contains a python script which converts the text from a PDF file into an mp3 audio file. This code uses file handling in python and relies on some external libraries.

<h3>Some libraries used in this python code:</h3>

<code>tempfile</code> :	creates temporary file to contain .ppm image files for fast input-output
<code>pdf2image</code> : converts pdfs to images
<code>PIL.Image</code> : supports opening, manipulating and saving images
<code>pytesseract</code> : converts written content of an image to text
<code>gtts</code> : Google Translate's text-to-speech API

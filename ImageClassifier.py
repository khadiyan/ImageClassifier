import pytesseract
import os
import shutil
import sys
from tqdm import tqdm

if len(sys.argv) != 2:
    print("Error Command", len(sys.argv))
    exit()

filepath = (str(sys.argv[1]))
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

files = os.listdir(filepath)
positive = [] #image contain text
negative = [] #no text

#Category path
if os.path.isdir(filepath + "\\" + "donation") == False:
    os.mkdir(filepath + "\\" + "donation")
if os.path.isdir(filepath + "\\" + "others") == False:
    os.mkdir(filepath + "\\" + "others")
if os.path.isdir(filepath + "\\" + "loker") == False:
    os.mkdir(filepath + "\\" + "loker")
if os.path.isdir(filepath + "\\" + "himpunan") == False:
    os.mkdir(filepath + "\\" + "himpunan")
if os.path.isdir(filepath + "\\" + "OK") == False:
    os.mkdir(filepath + "\\" + "OK")


def strfind(strText,findText):
    return strText.lower().find(findText)

pbar = tqdm(total=len(files))

for f in files:
    fullPath = (filepath + '\\' + f)
    if (os.path.isfile(fullPath)) == 1:
        imgText = pytesseract.image_to_string(fullPath)
        if len(imgText) > 10:
            if (strfind(imgText,"himpunan") != -1) or (strfind(imgText,"musyawarah") != -1) or (strfind(imgText,"bazar") != -1) or (strfind(imgText,"sidang") != -1):
                positive.append(f)
                shutil.move(fullPath, filepath + '\\' + 'himpunan\\' + f)
            elif (strfind(imgText,"donasi") != -1) or (strfind(imgText,"donation") != -1):
                positive.append(f)
                shutil.move(fullPath, filepath + '\\' + 'donation\\' + f)
            elif (strfind(imgText,"loker") != -1) or (strfind(imgText,"lowongan") != -1) or (strfind(imgText,"development") != -1) or (strfind(imgText,"career") != -1) or (strfind(imgText,"karir") != -1) or (strfind(imgText,"trainee") != -1) or (strfind(imgText,"hiring") != -1):
                positive.append(f)
                shutil.move(fullPath, filepath + '\\' + 'loker\\' + f)
            else:
                positive.append(f)
                shutil.move(fullPath, filepath + '\\' + 'others\\' + f)
        else:
            negative.append(f)
            shutil.move(fullPath, filepath + '\\' + 'OK\\' + f)
    pbar.update(1)
pbar.close()    
print("DONE!!!")
print("{} files moved".format(len(positive)))
print("{} files NOT moved".format(len(negative)))

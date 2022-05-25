from PyPDF2 import PdfFileReader
import os

class pdfcontroll:
    def pdf_conv_text(filepath):
        with open(filepath, 'rb') as f:
            text = ""
            pdf = PdfFileReader(f)
            for i in range(pdf.numPages):
                text += pdf.getPage(i).extractText()
        return text



class filecontroll:
    def text_create(filepath, pdf_text):
        if os.path.isfile(filepath.replace(".pdf",".txt")):
            return False
        else:
            with open(filepath.replace(".pdf",".txt"),'w',encoding='utf-8') as f:
                for line in pdf_text:
                    f.write(line)
                f.close()
            os.remove(filepath)
            return True

    def read_text(filepath):
        result = ''
        with open(filepath,'r',encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                result += line
                
        return result


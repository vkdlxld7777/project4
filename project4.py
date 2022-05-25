import abstract as ab
import os
import pathlib as pl

#pdf 텍스트 파일 생성
class play:
    def start():
        path = os.getcwd()+'\\file\\'
        pdf_fileList = [str(i) for i in pl.Path(path).glob("*.pdf")]
        text_fileList = [str(i) for i in pl.Path(path).glob("*.txt")]
        for i in pdf_fileList:
            if i in text_fileList:
                continue
            else:
                read_text = ab.pdfcontroll.pdf_conv_text(i)
                ab.filecontroll.text_create(i,read_text)


        #텍스트 파일 다시 읽어오기
        text_fileList = [str(i) for i in pl.Path(path).glob("*.txt")]
        textlist = []
        for i in text_fileList:
            textlist.append([i.split('\\')[-1].split('.')[0],ab.filecontroll.read_text(i)])
        
        return textlist


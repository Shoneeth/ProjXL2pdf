import os
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from PyPDF2 import PdfMerger,PdfReader
from idextract import extract_file_id
from image2pdf import imageToPdf

def merge_pdf_from_drive_links(drive_links, output_filename,GDLinks):
    # Set up authentication using the PyDrive library
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()  # Opens a new tab to authenticate
    drive = GoogleDrive(gauth)


    print("checking...")

    count=2
    countemptycells=0
    invalFiles=0
    ccoutfiles=0
    # Loop through the Google Drive links and download the PDF files
    pdf_files = []
    for link in drive_links:
        if type(link)==str:
                file_id=extract_file_id(link)

                # if file_id:
                #         #print(file_id)
                #         None
                # else:
                #         invalFiles+=1
                #         #print("File ID not found")

                file = drive.CreateFile({'id': file_id})
                try:
                        file.FetchMetadata()
                        
                        file.GetContentFile(file['title'])
                        print('fileCell-%s :- title: %s, mimeType: %s' % (count,file['title'], file['mimeType']))
                        #count+=1

                        if 'pdf' in file['mimeType']:
                                pdf_files.append(file['title'])
                        elif 'image' in file['mimeType']:
                                imageToPdf(file['title'])
                                pdf_files.append(file['title']+'.pdf')
                                if os.path.exists(file['title']):
                                        os.remove(file['title'])  
                                #print('image')
                        else:
                                invalFiles+=1
                                if os.path.exists(file['title']):
                                       os.remove(file['title'])
                                print('fileCell-%s :- file format is not a image or a pdf' % count)
                except :
                        invalFiles+=1
                        print('fileCell-%s :- file not found or invalid link'% count)
                        #count+=1
        else:
               countemptycells+=1
               print('fileCell-%s :- empty cell'% count)
               count+=1
               continue
        count+=1
    # Merge the downloaded PDF files using the PyPDF2 library
    #print(pdf_files)
    pdf_merger = PdfMerger()
    for file in pdf_files:
        with open(file, 'rb') as f:
            if PdfReader(file).is_encrypted == False :
                pdf_merger.append(f)
                ccoutfiles+=1
                print("processing..."+str(ccoutfiles)+"of"+str(GDLinks)+"..completed merging...")
            else:
                      print("%s --- file is password protected" % file)
                      invalFiles+=1
    pdf_merger.write(output_filename)

    for file in pdf_files:
          if os.path.exists(file):
                  os.remove(file)    
    
    print("total files merged: ",ccoutfiles)
    print("total empty spaces found:"+str(countemptycells)+" , "+"total invalid links:"+str(invalFiles))
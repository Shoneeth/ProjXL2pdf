import pandas as pd
from links import merge_pdf_from_drive_links

filedata= pd.read_excel("test3.xlsx","Form responses 1")   #execel file name , sheet name
drive_links = filedata['links'].values.tolist()   #column name

print(drive_links)
output_destination=str(input())
merge_pdf_from_drive_links(drive_links,output_destination+'\merged.pdf')   # output file name

print("your files are merged.")
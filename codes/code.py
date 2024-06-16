import pandas as pd
from links import merge_pdf_from_drive_links


xL_file_path=str(input("enter the excel sheet path(note:path doesn't need " ") : "))
sheetName=str(input("enter the sheet Name in excelsheet : "))
columeName=str(input("enter the colume name of the links : "))

filedata= pd.read_excel(xL_file_path,sheetName)   #execel file name , sheet name
drive_links = filedata[columeName].values.tolist()   #column name

print("Total Number of links found:",len(drive_links))

GDLinks=len(drive_links)

output_destination=str(input("enter the path for destination folder(note:path doesn't need \" \") : "))+'\\merged.pdf'
merge_pdf_from_drive_links(drive_links,output_destination,GDLinks)   # output file name


print("your files are merged. and saved at location: ",output_destination)
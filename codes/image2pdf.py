import img2pdf
from pillow_heif import register_heif_opener

def imageToPdf(file):
    
# Replace with the path to your image file
      image_path = file # Or any of the supported image formats

# Define the output PDF filename (optional)
      outname= file +'.pdf'
      output_pdf_path = outname

      register_heif_opener()
      

      with open(image_path, "rb") as image_file:
            pdf_bytes = img2pdf.convert(image_file, rotation=img2pdf.Rotation.ifvalid)

      # Write the PDF bytes to a file (optional, if you want a separate PDF)
      if output_pdf_path:
            with open(output_pdf_path, "wb") as pdf_file:
                  pdf_file.write(pdf_bytes)

      print("Image converted to PDF successfully! : ",output_pdf_path)



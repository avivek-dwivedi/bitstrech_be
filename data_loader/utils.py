import os
import zipfile
from PIL import Image
import io
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def upload_utils(request):
    file = request.FILES.get('file')
    if file:
        if file.name.endswith('.zip'):
            try:
                current_directory = os.path.dirname(os.path.abspath(__file__))
                target_directory = os.path.join(current_directory, 'data')

                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)

                with zipfile.ZipFile(file, 'r') as zip_ref:
                    zip_ref.extractall(target_directory)


                return HttpResponse("ZIP file extracted successfully.")
            except Exception as e:
                logger.error(f"Error extracting ZIP file: {str(e)}")
                return HttpResponse("Error extracting ZIP file.", status=500)
        else:
            return HttpResponse("Invalid file format. Please provide a ZIP file.", status=400)
    else:
        return HttpResponse("No file provided.", status=400)


def preprocess(dir):
    dir='E:\bitstrech\bitstrech_be\data_loader\data\train'
    

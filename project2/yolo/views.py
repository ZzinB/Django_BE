import os
from django.conf import settings
from django.shortcuts import render
from yolov5.detection import run_yolov5_detection
import subprocess

def upload_image(request):
    if request.method == 'POST':
        # 이미지 업로드 및 저장 로직
        image_file = request.FILES['file']
        image_file_path = os.path.join(settings.MEDIA_ROOT, 'images', image_file.name)
        with open(image_file_path, 'wb') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        weights_path = 'yolov5/weights/best.pt'  # 가중치 파일의 경로
        results, errors = run_yolov5_detection(image_file_path, weights_path)
        if results is not None:
            # 탐지 결과를 처리하고 필요한 작업을 수행합니다.
            return render(request, 'result.html', {'image_url': image_file_path,'results': results, 'errors': errors})
        else:
            # 오류 처리 로직
           return render(request, 'error.html', {'message': 'Failed to perform detection.'})

    else:
        # GET 요청 처리 로직
        return render(request, 'upload.html')

import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from PIL import Image
from PIL.ExifTags import TAGS
import json
from django.http import HttpResponse
from yolov5.detect import run

def home(request):
  return render(request,'home.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

# views.py
def upload_image(request):
    if request.method == 'POST':
        post = Post()
        post.image = request.FILES['image']
        post.save()
        coordinates = meta(post.image.path)
        if coordinates:
            post.coordinates = coordinates
            post.save()
            
        weights_path = 'yolov5/weights/best.pt'  # 가중치 파일의 경로
        # results = run_yolov5_detection(post.image.path, weights_path)
        rs_img, rs_label = run(source= post.image.path, weights= weights_path, project=os.path.join(settings.MEDIA_ROOT, 'yolo'))
        if rs_label:
            # 탐지 결과를 처리하고 필요한 작업을 수행합니다.
            
            post.labels = rs_label
            post.save()
            
            return redirect('/detail/'+str(post.id))

        return HttpResponse("Detection results not found.")   
    else:
        post = Post()
        return render(request, 'create.html', {'post': post})


def delete(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  post_detail.delete()
  return redirect('/create')

def meta(image_path):
    image = Image.open(image_path)
    info = image._getexif()
    image.close()

    if info is not None:
        taglabel = {}

        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            taglabel[decoded] = value

        exifGPS = taglabel.get('GPSInfo')
        if exifGPS:
            latData = exifGPS[2]
            lonData = exifGPS[4]

            if latData and lonData:
                latDeg = latData[0]
                latMin = latData[1]
                latSec = latData[2]

                lonDeg = lonData[0]
                lonMin = lonData[1]
                lonSec = lonData[2]

                Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
                if exifGPS[1] == 'S':
                    Lat = -1 * Lat

                Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
                if exifGPS[3] == 'W':
                    Lon = -1 * Lon

                coordinates = {
                    'latitude': Lat,
                    'longitude': Lon
                }

                json_data = json.dumps(coordinates)
                return json_data

    return None

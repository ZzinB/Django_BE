from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from PIL import Image
from PIL.ExifTags import TAGS
import json


# Create your views here.
def home(request):
  return render(request,'home.html')

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request, 'detail.html', {'post': post_detail})

def create(request):
  if request.method=="POST":
    post = Post()
    post.image = request.FILES['image']
    post.save()
    coordinates = meta(post.image.path)
    if coordinates:
            post.coordinates = coordinates
            post.save()
            
    return redirect('/detail/'+str(post.id))

    # return redirect('/detail/'+str(post.id),{'post':post})
  else:
    post = Post()
    return render(request,'create.html',{'post':post})
   
def delete(request, post_id):
  post_detail = get_object_or_404(Post, pk=post_id)
  post_detail.delete()
  return redirect('/create')

def meta(image_path):
  image = Image.open(image_path)
  info = image._getexif()
  image.close()
  # 새로운 딕셔너리 생성

  taglabel = {}

  for tag, value in info.items():
      decoded = TAGS.get(tag, tag)
      taglabel[decoded] = value

  exifGPS = taglabel['GPSInfo']
  if exifGPS:
    latData = exifGPS[2]
    lonData = exifGPS[4]

    if latData and lonData:
  # 도, 분, 초 계산
      # latDeg = latData[0][0] / float(latData[0][1])
      # latMin = latData[1][0] / float(latData[1][1])
      # latSec = latData[2][0] / float(latData[2][1])


      # lonDeg = lonData[0][0] / float(lonData[0][1])
      # lonMin = lonData[1][0] / float(lonData[1][1])
      # lonSec = lonData[2][0] / float(lonData[2][1]) 


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

      # Create a dictionary with latitude and longitude
      coordinates = {
          'latitude': Lat,
          'longitude': Lon
      }

      # Convert the dictionary to JSON
      json_data = json.dumps(coordinates)

      return json_data

  return None
  # # 도, 분, 초로 나타내기
  # Lat = str(int(latDeg)) + "°" + str(int(latMin)) + "'" + str(latSec) + "\"" + exifGPS[1]
  # Lon = str(int(lonDeg)) + "°" + str(int(lonMin)) + "'" + str(lonSec) + "\"" + exifGPS[3]

  # print(Lat, Lon)
  # # 도 decimal로 나타내기
  # # 위도 계산
  # Lat = (latDeg + (latMin + latSec / 60.0) / 60.0)
  # # 북위, 남위인지를 판단, 남위일 경우 -로 변경
  # if exifGPS[1] == 'S': Lat = Lat * -1

  # # 경도 계산
  # Lon = (lonDeg + (lonMin + lonSec / 60.0) / 60.0)
  # # 동경, 서경인지를 판단, 서경일 경우 -로 변경
  # if exifGPS[3] == 'W': Lon = Lon * -1

  # print(Lat, ",",  Lon)
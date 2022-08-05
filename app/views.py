from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import guideSerializer, pageSerializer, sectionSerializer
from .models import guide, page, section

class PostDataView1(APIView):
    def post(self,request):
        serializer=guideSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class PostDataView2(APIView):
    def post(self,request):
        print(request.data)
        serializer=pageSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class PostDataView4(APIView):
    def post(self,request):
        serializer=sectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class GetView(APIView):
    def post(self,request):
        guidename=request.data['guidename']
        pagedata=page.objects.filter(guidename=guidename).values()
        sectiondata=section.objects.filter(guidename=guidename).values()
        return Response({"status": "success", "data": {'pages': pagedata,'sections':sectiondata}}, status=status.HTTP_200_OK)


class SectionGetView(APIView):
    def post(self,request):
        guidename=request.data['guidename']
        pagename=request.data['pagename']
        sectionData=section.objects.filter(pagename=pagename,guidename=guidename).values()
        return Response({"status": "success", "data": {'sections':sectionData}}, status=status.HTTP_200_OK)
# Create your views here.

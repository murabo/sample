# -*- coding:utf-8 -*-
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import *
from app.serializers import ClientSerializer, LikeSerializer


class ClientView(APIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        {
         "appoint_date": 1396832700,
         "appoint_Status": 2,
        "site_id": 1,
         "test_type": "A"
         }
        """
        try:
            user_id = request.GET['user_id']
            data = Client.objects.get(pk=user_id)
            user = ClientSerializer(data)
            return Response(user.data)
        except:
            return Response({"message": "ユーザーが見つかりません"},
                            status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):

    def get(self, request, *args, **kwargs):
        """
        user_id :String 必須
        limit   :Int デフォルト値100(取得件数)
        offset  :Int 取得オフセット(取得したいページ数)
        :return:
            {
              total: 2,
              limit: 100,
              offset: 0,
              pages: [
                {
                  "url": "http://xxxxx.jp/aaa/bbb",
                  "title": "トップページ",
                  "description": "ページの概要テキスト",
                  "created_at": 1396832700
                },
                {}
              ]
            }
        """
        try:
            results = {
                "total": 0,
                "limit": 100,
                "offset": 0,
                "pages": []
            }

            user_id = request.GET['user_id']
            limit = request.GET.get('limit', 100)
            offset = request.GET.get('limit', 0)
            likes = Like.objects.filter(client=user_id)
            if likes:
                results["pages"] = LikeSerializer(likes, many=True).data
                results["total"] = len(LikeSerializer(likes, many=True).data)

            """
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            """

            return Response(results)
        except:
            return Response({"message": "お気に入り情報が見つかりません"},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        try:
            results = {
                "total": 0,
                "limit": 100,
                "offset": 0,
                "pages": []
            }
            print(request.data)
            user_id = request.data['user_id']
            url = request.data['url']
            client = Client.objects.get(pk=user_id)
            _, _ = Like.objects.get_or_create(
                client=client,
                url=url
            )
            likes = Like.objects.filter(client=client)
            if likes:
                results["pages"] = LikeSerializer(likes, many=True).data
                results["total"] = len(LikeSerializer(likes, many=True).data)

            return Response(results)
        except:
            return Response({"message": "お気に入り情報が見つかりません"},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        print(request.data)
        results = {
            "total": 0,
            "limit": 100,
            "offset": 0,
            "pages": []
        }
        user_id = request.data['user_id']
        url = request.data['url']
        client = Client.objects.get(pk=user_id)
        Like.objects.get(
            client=client,
            url=url
        ).delete()
        likes = Like.objects.filter(client=client)
        if likes:
            results["pages"] = LikeSerializer(likes, many=True).data
            results["total"] = len(LikeSerializer(likes, many=True).data)

        return Response(results)

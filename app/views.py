# -*- coding:utf-8 -*-
import datetime

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import *
from app.models import *
from app.serializers import ClientSerializer, LikeSerializer, EstimateSerializer


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
            limit = int(request.GET.get('limit', 100))
            offset = int(request.GET.get('offset', 0))
            likes = Like.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]

            if likes:
                results["pages"] = LikeSerializer(likes, many=True).data
                results["total"] = len(Like.objects.filter(client=user_id))
                results["limit"] = limit
                results["offset"] = offset

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
            limit = int(request.GET.get('limit', 100))
            offset = int(request.GET.get('offset', 0))

            url = request.data['url']
            client = Client.objects.get(pk=user_id)
            _, _ = Like.objects.get_or_create(
                client=client,
                url=url
            )
            likes = Like.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]
            if likes:
                results["pages"] = LikeSerializer(likes, many=True).data
                results["total"] = len(Like.objects.filter(client=user_id))
                results["limit"] = limit
                results["offset"] = offset

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
        limit = int(request.GET.get('limit', 100))
        offset = int(request.GET.get('offset', 0))
        url = request.data['url']
        client = Client.objects.get(pk=user_id)
        Like.objects.get(
            client=client,
            url=url
        ).delete()
        likes = Like.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]
        if likes:
            results["pages"] = LikeSerializer(likes, many=True).data
            results["total"] = len(Like.objects.filter(client=user_id))
            results["limit"] = limit
            results["offset"] = offset

        return Response(results)



class EstimateView(APIView):

    def get(self, request, *args, **kwargs):
        """
        user_id :String 必須
        limit   :Int デフォルト値100(取得件数)
        offset  :Int 取得オフセット(取得したいページ数)
        :return:
            {

            }
        """

        results = {
            "total": 0,
            "limit": 100,
            "offset": 0,
            "pages": []
        }

        user_id = request.GET['user_id']
        limit = int(request.GET.get('limit', 100))
        offset = int(request.GET.get('offset', 0))
        estimates = Estimate.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]

        if estimates:
            results["estimates"] = EstimateSerializer(estimates, many=True).data
            results["total"] = len(Estimate.objects.filter(client=user_id))
            results["limit"] = limit
            results["offset"] = offset

        return Response(results)


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
            limit = int(request.GET.get('limit', 100))
            offset = int(request.GET.get('offset', 0))


            site_id = request.data['site_id']
            banquet_id = request.data['banquet_id']
            guest_num = request.data['guest_num']
            style_id = request.data['style_id']
            party_costume_id = request.data['party_costume_id']
            photo_id = request.data['photo_id']
            before_photo_id = request.data['before_photo_id']
            cuisine_id = request.data['cuisine_id']
            cake_flg = request.data['cake_flg']
            movie_id = request.data['movie_id']
            coordinate_id = request.data['coordinate_id']
            effects = request.data['effects']
            date = request.data['date']
            time = request.data['time']

            est = Estimate(
                user_id=user_id,
                site_id=site_id,
                banquet_id=banquet_id,
                guest_num=guest_num,
                party_costume_id=party_costume_id,
                photo_id=photo_id,
                before_photo_id=before_photo_id,
                style_id=style_id,
                cuisine_id=cuisine_id,
                cake_flg=cake_flg,
                movie_id=movie_id,
                coordinate_id=coordinate_id,
                date=datetime.date.fromtimestamp(date),
                time=time
            ).save()
            for e in effects:
                est.effect.add(e)

            url = request.data['url']
            client = Client.objects.get(pk=user_id)
            _, _ = Like.objects.get_or_create(
                client=client,
                url=url
            )
            estimates = Estimate.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]
            if estimates:
                results["estimates"] = EstimateSerializer(estimates, many=True).data
                results["total"] = len(Like.objects.filter(client=user_id))
                results["limit"] = limit
                results["offset"] = offset

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
        limit = int(request.GET.get('limit', 100))
        offset = int(request.GET.get('offset', 0))
        url = request.data['url']
        client = Client.objects.get(pk=user_id)
        Like.objects.get(
            client=client,
            url=url
        ).delete()
        likes = Like.objects.filter(client=user_id)[offset * limit:limit * (1 + offset)]
        if likes:
            results["pages"] = LikeSerializer(likes, many=True).data
            results["total"] = len(Like.objects.filter(client=user_id))
            results["limit"] = limit
            results["offset"] = offset

        return Response(results)
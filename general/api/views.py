from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, DestroyModelMixin
from general.api.serializers import ItemSerializer
from general.models import Item
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
import stripe


class ItemViewSet(
    CreateModelMixin,
    GenericViewSet,
):
    serializer_class = ItemSerializer

    @action(detail=True, method=['get'])
    def buy(self, request, pk=None):
        item = self.get_object()
        stripe.api_key = "safdlgsdjfdil3443klnk_njldfjq"
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'rub'
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='',
            cancel_url='',
        )
        return Response({'session_id': session.id})

    @action(detail=True, methods=['get'])
    def item(self, request, pk=None):
        item = self.get_object()
        return Response(ItemSerializer(item).data)



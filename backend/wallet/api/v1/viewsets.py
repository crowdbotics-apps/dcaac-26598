from rest_framework import authentication
from wallet.models import (
    PaymentTransaction,
    PaymentMethod,
    TaskerWallet,
    TaskerPaymentAccount,
    CustomerWallet,
)
from .serializers import (
    PaymentTransactionSerializer,
    PaymentMethodSerializer,
    TaskerWalletSerializer,
    TaskerPaymentAccountSerializer,
    CustomerWalletSerializer,
)
from rest_framework import viewsets


class TaskerWalletViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerWallet.objects.all()


class CustomerWalletViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerWalletSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = CustomerWallet.objects.all()


class PaymentMethodViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentMethod.objects.all()


class TaskerPaymentAccountViewSet(viewsets.ModelViewSet):
    serializer_class = TaskerPaymentAccountSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = TaskerPaymentAccount.objects.all()


class PaymentTransactionViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentTransactionSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = PaymentTransaction.objects.all()

from rest_framework import viewsets
from drf_yasg.utils import swagger_auto_schema
from core.models import Patient
from core.serializers.patient import PatientSerializer
from rest_framework.permissions import IsAuthenticated

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="환자 목록 조회",
        operation_description="등록된 모든 환자 목록을 조회합니다.",
        responses={200: PatientSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="환자 등록",
        operation_description="환자의 이름, 생년월일, 성별, 전화번호, 주소를 입력받아 새 환자를 등록합니다.",
        responses={201: PatientSerializer()}
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="환자 정보 조회",
        operation_description="환자의 ID(pk)를 기준으로 상세 정보를 조회합니다.",
        responses={200: PatientSerializer()}
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="환자 정보 전체 수정",
        operation_description="환자의 모든 필드를 수정합니다. 모든 값을 전달해야 합니다 (PUT 방식).",
        responses={200: PatientSerializer()}
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="환자 정보 일부 수정",
        operation_description="환자의 일부 필드만 수정합니다. 전달된 값만 반영됩니다 (PATCH 방식).",
        responses={200: PatientSerializer()}
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="환자 삭제",
        operation_description="해당 ID의 환자 정보를 삭제합니다.",
        responses={204: '삭제 성공 (No Content)'}
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

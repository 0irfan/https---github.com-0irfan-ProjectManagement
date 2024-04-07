from django.urls import path
from .views import ProjectAuthorityListCreateAPIView,ProjectInformationListCreateAPIView,projectInformationRetrieveUpdateDestroyApiview,ProjectDetailListCreateAPIView,ProjectDetailRetrieveUpdateDestroyAPIView,ResourceListCreateAPIView,ResourceRetrieveUpdateDestroyAPIView,projectAuthorityRetrieveUpdateDestroyApiview,DeliverableListCreateAPIView,DeliverableRetreiveUpdateDestroyApiview



urlpatterns = [
    path('Project/', ProjectInformationListCreateAPIView.as_view(), name='project-list-create'),

    path('Project/<int:pk>/', projectInformationRetrieveUpdateDestroyApiview.as_view(), name='project-retrieve-update-delete'),

    path('ProjectDetail/',ProjectDetailListCreateAPIView.as_view(),name='projectdetail-list-create'),

    path('ProjectDetail/',ProjectDetailRetrieveUpdateDestroyAPIView.as_view(),name='projectdetail-retrieve-update-delete'),

    path('Resource/',ResourceListCreateAPIView.as_view(),name='resource-list-create'),

    path('Resource/',ResourceRetrieveUpdateDestroyAPIView.as_view(),name='resource-retrieve-update-destroy'),

    path('Deliverable-list-create/',DeliverableListCreateAPIView.as_view(),name='Deliverable-list-create'),

    path('Deliverable/<int:pk>/',DeliverableRetreiveUpdateDestroyApiview.as_view(),name='Deliverable-retrieve-update-delete'),

    path('ProjectAuthority/', ProjectAuthorityListCreateAPIView.as_view(), name='projectauthority-list-create'),

    path('ProjectAuthority/<int:pk>/', projectAuthorityRetrieveUpdateDestroyApiview.as_view(), name='projectauthority-retrieve-update-delete'),
]
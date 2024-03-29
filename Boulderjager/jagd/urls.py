
from django.urls import path
from . import views

app_name = 'jagd'

urlpatterns = [

    path("add-boulder/", views.add_boulders_view, name="add_boulders_view"),
    path("ranking/", views.ranking_view, name="ranking_view"),
    path("view-boulder/", views.view_boulder, name="view_boulder"),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('export-csv/', views.export_rankings_to_csv, name='export_csv'),
    path('export-ranking-detail/', views.export_combined_data_to_csv, name='export_combined_data_to_csv')
]

from django.urls import path
from . import views
urlpatterns = [
    ## MOVIE
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    
    ## REVIEW
    path('movies/<int:movie_pk>/reviews/', views.review_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/', views.review_detail_delete_update),

    ## COMMENT
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comment/', views.comment_create),
    path('movies/<int:movie_pk>/reviews/<int:review_pk>/comment/<int:comment_pk>/', views.comment_list),
]

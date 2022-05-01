"""movie_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path,path,include 

from rest_framework import routers
from rest_framework.permissions import AllowAny

from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

from movies.views import MovieViewSet
from directors.views import DirectorViewSet

from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('directors', DirectorViewSet)

schema_url_patterns = [ 
    re_path('', include('movie_api.urls')), 
] 

schema_view_v1 = get_schema_view( 
	openapi.Info( 
		title="Taeksoolee Open API", 
		default_version='v1', 
		description="django-rest-framework, movies", 
		terms_of_service="https://github.com/taeksoolee", 
	), 
	public=True, 
	permission_classes=(AllowAny,), 
	patterns=schema_url_patterns, 
)

urlpatterns = [ 
	re_path('admin/', admin.site.urls),
    re_path('api/token/', obtain_jwt_token), # JWT 토큰을 발행
    re_path('api/token/verify/', verify_jwt_token), # JWT 토큰이 유효한지 검증
    re_path('api/token/refresh/', refresh_jwt_token), # JWT 토큰을 갱신
    
	re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'), 
	re_path(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'), 
    re_path(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    re_path(r'^', include(router.urls)),
]

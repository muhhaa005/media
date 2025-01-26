
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.decorators import permission_classes

schema_view = get_schema_view(
    openapi.Info(
        title="Online store",
        default_version='v1',),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),

)

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('media.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

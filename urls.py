"""neeri_recruitment_portal URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from neeri_recruitment_portal.views import CronJobView

urlpatterns = [
    path('user/', include('user.urls')),
    path('document/', include('document.urls')),
    path('job_posting/', include('job_posting.urls')),
    path('template/', include('communication_template.urls')),
    path('admin/', admin.site.urls),
    path("cron_job/", CronJobView.as_view(), name="cron_job"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

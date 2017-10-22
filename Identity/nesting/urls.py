from django.conf.urls import url
from nesting.views import Identity_view, Identity_nest_list_view, Symptoms_document_view, Medical_History_nest_view, Identity_unique_Update
from . import views

urlpatterns = [
                    url(r'^$', Identity_view.as_view(), name = 'nesting'),
                    url(r'^Identity-nest/(?P<pk>\w+)/$', Identity_nest_list_view.as_view(), name = 'Identity_nest_list'),
                    url(r'^Symptoms-document/(?P<pk>\w+)/$', Symptoms_document_view.as_view(), name = 'Symptoms_nest_list'),
                    url(r'^Symptom-view/(?P<pk>\w+)/$', Medical_History_nest_view.as_view(), name = 'Medical_History_nest'),
                    url(r'^Identity-edit/(?P<pk>\w+)/$', Identity_unique_Update.as_view(), name = 'Identity_unique_view_update')

]

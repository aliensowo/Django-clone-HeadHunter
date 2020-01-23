from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view())

)

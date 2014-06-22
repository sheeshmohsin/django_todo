from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'todo_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #user auth urls
    url(r'^login/$','todo.views.login'),
    url(r'^auth/$', 'todo.views.auth_view'),
    url(r'^logout/$', 'todo.views.logout'),
    url(r'^loggedin/$', 'todo.views.loggedin'),
    url(r'^invalid/$', 'todo.views.invalid_login'),
    url(r'^createtask/$', 'todo.views.createtask'),
    url(r'^register/$', 'todo.views.register_user'),
    url(r'^register_success/$', 'todo.views.register_success'),
    
)
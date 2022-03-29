from django.conf.urls import url
from snippets import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]


urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    # url(r'^users/$', views.UserList.as_view()),
    # url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    # url(r'^$', views.api_root),
    # url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

"""使用路由器处理viewset"""
# from django.conf.urls import url, include
# from snippets import views
# from rest_framework.routers import DefaultRouter
#
# # 创建路由器并注册我们的视图。
# router = DefaultRouter()
# router.register(r'snippets', views.SnippetViewSet)
# router.register(r'users', views.UserViewSet)
#
# # API URL现在由路由器自动确定。
# # 另外，我们还要包含可浏览的API的登录URL。
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]



"""使用超链接"""
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

# API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$',
#         views.SnippetList.as_view(),
#         name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$',
#         views.SnippetDetail.as_view(),
#         name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$',
#         views.SnippetHighlight.as_view(),
#         name='snippet-highlight'),
#     url(r'^users/$',
#         views.UserList.as_view(),
#         name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$',
#         views.UserDetail.as_view(),
#         name='user-detail')
# ])
#
# # 可浏览API的登录和注销视图
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

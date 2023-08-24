from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *
urlpatterns=[path('',login_required(IndexView.as_view()),name='dashboard'),path('user/initialize/agency/',login_required(user_init_agency),name='user_init_agency'),path('user/initialize/agency-ajax/<int:agency_id>/',user_init_agency_ajax,name='user_init_agency_ajax'),path('user/reset/agency/',login_required(user_reset_agency),name='user_reset_agency'),path('user/initialize/agency/connect',login_required(user_connect_agency),name='user_connect_agency'),path('user/initialize/service/<int:agency_id>/',login_required(user_init_service),name='user_init_service'),path('user/initialize/service-ajax/<int:agency_id>/<int:service_id>/',user_init_service_ajax,name='user_init_service_ajax'),path('service-change-ajax/<str:service_id>/',service_change_ajax,name='service_change_ajax'),path('tags/',login_required(TagsView.as_view()),name='tags'),path('tags-ajax/',tags_ajax,name='tags_ajax'),path('tags/create/',login_required(tags_create),name='tags_create'),path('tags/update/<uuid:uuid>/',login_required(tags_update),name='tags_update'),path('tags/delete/<uuid:uuid>/',login_required(tags_delete),name='tags_delete'),path('whyus/',login_required(WhyUsView.as_view()),name='whyus'),path('whyus-ajax/',whyus_ajax,name='whyus_ajax'),path('whyus/create/',login_required(whyus_create),name='whyus_create'),path('whyus/update/<uuid:uuid>/',login_required(whyus_update),name='whyus_update'),path('whyus/delete/<uuid:uuid>/',login_required(whyus_delete),name='whyus_delete'),path('logo/',login_required(LogoView.as_view()),name='logo'),path('logo-ajax/',logo_ajax,name='logo_ajax'),path('logo/create/',login_required(logo_create),name='logo_create'),path('logo/update/<uuid:uuid>/',login_required(logo_update),name='logo_update'),path('logo/delete/<uuid:uuid>/',login_required(logo_delete),name='logo_delete'),path('announcement/',login_required(AnnouncementView.as_view()),name='announcement'),path('announcement-ajax/',announcement_ajax,name='announcement_ajax'),path('announcement/create/',login_required(announcement_create),name='announcement_create'),path('announcement/update/<uuid:uuid>/',login_required(announcement_update),name='announcement_update'),path('announcement/delete/<uuid:uuid>/',login_required(announcement_delete),name='announcement_delete'),path('fasilities/',login_required(FasilitiesView.as_view()),name='fasilities'),path('fasilities-ajax/',fasilities_ajax,name='fasilities_ajax'),path('fasilities/create/',login_required(fasilities_create),name='fasilities_create'),path('fasilities/update/<uuid:uuid>/',login_required(fasilities_update),name='fasilities_update'),path('fasilities/delete/<uuid:uuid>/',login_required(fasilities_delete),name='fasilities_delete'),path('offers/',login_required(OffersView.as_view()),name='offers'),path('offers-ajax/',offers_ajax,name='offers_ajax'),path('offers/create/',login_required(offers_create),name='offers_create'),path('offers/update/<uuid:uuid>/',login_required(offers_update),name='offers_update'),path('offers/delete/<uuid:uuid>/',login_required(offers_delete),name='offers_delete'),path('news/',login_required(NewsView.as_view()),name='news'),path('news-ajax/',news_ajax,name='news_ajax'),path('news/create/',login_required(news_create),name='news_create'),path('news/update/<uuid:uuid>/',login_required(news_update),name='news_update'),path('news/delete/<uuid:uuid>/',login_required(news_delete),name='news_delete'),path('article/',login_required(ArticleView.as_view()),name='article'),path('article-ajax/',article_ajax,name='article_ajax'),path('article/create/',login_required(article_create),name='article_create'),path('article/update/<uuid:uuid>/',login_required(article_update),name='article_update'),path('article/delete/<uuid:uuid>/',login_required(article_delete),name='article_delete'),path('events/',login_required(EventsView.as_view()),name='events'),path('events-ajax/',events_ajax,name='events_ajax'),path('events/create/',login_required(events_create),name='events_create'),path('events/update/<uuid:uuid>/',login_required(events_update),name='events_update'),path('events/delete/<uuid:uuid>/',login_required(events_delete),name='events_delete'),path('slideshow/',login_required(SlideShowView.as_view()),name='slide_show'),path('slideshow-ajax/',slideshow_ajax,name='slideshow_ajax'),path('slideshow/create/',login_required(slideshow_create),name='slideshow_create'),path('slideshow/update/<uuid:uuid>/',login_required(slideshow_update),name='slideshow_update'),path('slideshow/delete/<uuid:uuid>/',login_required(slideshow_delete),name='slideshow_delete'),path('dailyalert/',login_required(DailyAlertView.as_view()),name='daily_alert'),path('dailyalert-ajax/',dailyalert_ajax,name='dailyalert_ajax'),path('dailyalert/create/',login_required(dailyalert_create),name='dailyalert_create'),path('dailyalert/update/<uuid:uuid>/',login_required(dailyalert_update),name='dailyalert_update'),path('dailyalert/delete/<uuid:uuid>/',login_required(dailyalert_delete),name='dailyalert_delete'),path('greeting/',login_required(GreetingView.as_view()),name='greeting'),path('greeting-ajax/',greeting_ajax,name='greeting_ajax'),path('greeting/create/',login_required(greeting_create),name='greeting_create'),path('greeting/update/<uuid:uuid>/',login_required(greeting_update),name='greeting_update'),path('greeting/delete/<uuid:uuid>/',login_required(greeting_delete),name='greeting_delete'),path('pages/',login_required(PagesView.as_view()),name='pages'),path('pages-ajax/',pages_ajax,name='pages_ajax'),path('pages/create/',login_required(pages_create),name='pages_create'),path('pages/update/<uuid:uuid>/',login_required(pages_update),name='pages_update'),path('pages/delete/<uuid:uuid>/',login_required(pages_delete),name='pages_delete'),path('socialmedia/',login_required(SocialMediaView.as_view()),name='social_media'),path('socialmedia-ajax/',socialmedia_ajax,name='socialmedia_ajax'),path('socialmedia/create/',login_required(socialmedia_create),name='socialmedia_create'),path('socialmedia/update/<uuid:uuid>/',login_required(socialmedia_update),name='socialmedia_update'),path('socialmedia/delete/<uuid:uuid>/',login_required(socialmedia_delete),name='socialmedia_delete'),path('photogallery/',login_required(PhotoGalleryView.as_view()),name='photo_gallery'),path('photogallery-ajax/',photogallery_ajax,name='photogallery_ajax'),path('photogallery/create/',login_required(photogallery_create),name='photogallery_create'),path('photogallery/update/<uuid:uuid>/',login_required(photogallery_update),name='photogallery_update'),path('photogallery/delete/<uuid:uuid>/',login_required(photogallery_delete),name='photogallery_delete'),path('videogallery/',login_required(VideoGalleryView.as_view()),name='video_gallery'),path('videogallery-ajax/',videogallery_ajax,name='videogallery_ajax'),path('videogallery/create/',login_required(videogallery_create),name='videogallery_create'),path('videogallery/update/<uuid:uuid>/',login_required(videogallery_update),name='videogallery_update'),path('videogallery/delete/<uuid:uuid>/',login_required(videogallery_delete),name='videogallery_delete'),path('relatedlink/',login_required(RelatedLinkView.as_view()),name='related_link'),path('relatedlink-ajax/',relatedlink_ajax,name='relatedlink_ajax'),path('relatedlink/create/',login_required(relatedlink_create),name='relatedlink_create'),path('relatedlink/update/<uuid:uuid>/',login_required(relatedlink_update),name='relatedlink_update'),path('relatedlink/delete/<uuid:uuid>/',login_required(relatedlink_delete),name='relatedlink_delete'),path('document/',login_required(DocumentView.as_view()),name='document'),path('document-ajax/',document_ajax,name='document_ajax'),path('document/create/',login_required(document_create),name='document_create'),path('document/update/<uuid:uuid>/',login_required(document_update),name='document_update'),path('document/delete/<uuid:uuid>/',login_required(document_delete),name='document_delete'),path('menu/',login_required(MenuView.as_view()),name='menu'),path('menu-ajax/',menu_ajax,name='menu_ajax'),path('menu/create/',login_required(menu_create),name='menu_create'),path('menu/update/<uuid:uuid>/',login_required(menu_update),name='menu_update'),path('menu/delete/<uuid:uuid>/',login_required(menu_delete),name='menu_delete'),path('menu-lookup-ajax/',menu_lookup_ajax,name='menu_lookup_ajax'),path('agency/',login_required(AgencyView.as_view()),name='agency'),path('agency-ajax/',agency_ajax,name='agency_ajax'),path('agency/create/',login_required(agency_create),name='agency_create'),path('agency/update/<uuid:uuid>/',login_required(agency_update),name='agency_update'),path('agency/delete/<uuid:uuid>/',login_required(agency_delete),name='agency_delete'),path('product/',login_required(ProductView.as_view()),name='product'),path('product-ajax/',product_ajax,name='product_ajax'),path('product/create/',login_required(product_create),name='product_create'),path('product/update/<uuid:uuid>/',login_required(product_update),name='product_update'),path('product/delete/<uuid:uuid>/',login_required(product_delete),name='product_delete'),path('categories/',login_required(CategoriesView.as_view()),name='categories'),path('categories-ajax/',categories_ajax,name='categories_ajax'),path('categories/create/',login_required(categories_create),name='categories_create'),path('categories/update/<uuid:uuid>/',login_required(categories_update),name='categories_update'),path('categories/delete/<uuid:uuid>/',login_required(categories_delete),name='categories_delete'),path('templateowner/',login_required(TemplateOwnerView.as_view()),name='templateowner'),path('templateowner-ajax/',templateowner_ajax,name='templateowner_ajax'),path('templateowner/create/',login_required(templateowner_create),name='templateowner_create'),path('templateowner/update/<uuid:uuid>/',login_required(templateowner_update),name='templateowner_update'),path('templateowner/delete/<uuid:uuid>/',login_required(templateowner_delete),name='templateowner_delete'),path('template/',login_required(TemplateView_.as_view()),name='template'),path('template-ajax/',template_ajax,name='template_ajax'),path('template/create/',login_required(template_create),name='template_create'),path('template/update/<uuid:uuid>/',login_required(template_update),name='template_update'),path('template/delete/<uuid:uuid>/',login_required(template_delete),name='template_delete'),path('modellist/',login_required(ModelListView.as_view()),name='modellist'),path('modellist-ajax/',modellist_ajax,name='modellist_ajax'),path('modellist/create/',login_required(modellist_create),name='modellist_create'),path('modellist/update/<uuid:uuid>/',login_required(modellist_update),name='modellist_update'),path('modellist/delete/<uuid:uuid>/',login_required(modellist_delete),name='modellist_delete'),path('howitworks/',login_required(HowItWorksView.as_view()),name='how_it_works'),path('howitworks-ajax/',howitworks_ajax,name='howitworks_ajax'),path('howitworks/create/',login_required(howitworks_create),name='howitworks_create'),path('howitworks/update/<uuid:uuid>/',login_required(howitworks_update),name='howitworks_update'),path('howitworks/delete/<uuid:uuid>/',login_required(howitworks_delete),name='howitworks_delete'),path('about-us/',login_required(AboutUsView.as_view()),name='about_us'),path('aboutus-ajax/',aboutus_ajax,name='aboutus_ajax'),path('about-us/create/',login_required(aboutus_create),name='aboutus_create'),path('about-us/update/<uuid:uuid>/',login_required(aboutus_update),name='aboutus_update'),path('about-us/delete/<uuid:uuid>/',login_required(aboutus_delete),name='aboutus_delete'),path('testimony/',login_required(TestimonyView.as_view()),name='testimony'),path('testimony-ajax/',testimony_ajax,name='testimony_ajax'),path('testimony/create/',login_required(testimony_create),name='testimony_create'),path('testimony/update/<uuid:uuid>/',login_required(testimony_update),name='testimony_update'),path('testimony/delete/<uuid:uuid>/',login_required(testimony_delete),name='testimony_delete'),path('service/',login_required(ServiceView.as_view()),name='service'),path('service-ajax/',service_ajax,name='service_ajax'),path('service/create/',login_required(service_create),name='service_create'),path('service/update/<uuid:uuid>/',login_required(service_update),name='service_update'),path('service/delete/<uuid:uuid>/',login_required(service_delete),name='service_delete'),path('banner/',login_required(BannerView.as_view()),name='banner'),path('banner-ajax/',banner_ajax,name='banner_ajax'),path('banner/create/',login_required(banner_create),name='banner_create'),path('banner/update/<uuid:uuid>/',login_required(banner_update),name='banner_update'),path('banner/delete/<uuid:uuid>/',login_required(banner_delete),name='banner_delete'),path('location/',login_required(LocationView.as_view()),name='location'),path('location-ajax/',location_ajax,name='location_ajax'),path('location/create/',login_required(location_create),name='location_create'),path('location/update/<uuid:uuid>/',login_required(location_update),name='location_update'),path('location/delete/<uuid:uuid>/',login_required(location_delete),name='location_delete'),path('user/',login_required(UserView.as_view()),name='user'),path('user-ajax/',user_ajax,name='user_ajax'),path('user/create/',login_required(user_create),name='user_create'),path('user/update/<uuid:uuid>/',login_required(user_update),name='user_update'),path('user/delete/<uuid:uuid>/',login_required(user_delete),name='user_delete'),path('hitcount-ajax/<str:period>/',hitcount_ajax,name='hitcount_ajax')]
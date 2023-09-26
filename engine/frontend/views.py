_A3='random_model'
_A2='random_paint'
_A1='latest_kind'
_A0='tags_list'
_z='categories_list'
_y='baseurl'
_x='content_detail'
_w='translations__name'
_v='videogallery'
_u='banner'
_t='latest_news'
_s='latest_announcement'
_r="Menu Group '%s' belum terdaftar, silahkan daftar di halaman <a href='%s'>admin</a>"
_q='Halaman tidak ditemukan!'
_p='all'
_o='name'
_n='pages'
_m='pagetype'
_l='count'
_k='testimony'
_j='aboutus'
_i='/dashboard'
_h='document'
_g='howitworks'
_f='proses'
_e='menugroup'
_d="service untuk '%s' belum terdaftar, silahkan daftar di halaman <a href='%s'>admin</a>"
_c='greeting'
_b='product'
_a='offers'
_Z='fasilities'
_Y=False
_X='socialmedia'
_W='relatedlink'
_V='menu'
_U='home'
_T='/admin'
_S='slug'
_R='order_item'
_Q='slideshow'
_P='kind'
_O='footer_menu_2'
_N='footer_menu_1'
_M='is_mobile'
_L='article'
_K='events'
_J='logo'
_I='base_url'
_H='photogallery'
_G=True
_F='news'
_E='frontend'
_D='announcement'
_C='-updated_at'
_B='-is_header_text'
_A=None
import calendar,datetime,random
from django_authbox.common import get_natural_datetime
from django.shortcuts import redirect
from django.apps import apps
from django.contrib.contenttypes.models import ContentType
from django.contrib.sites.models import Site
from django.core.cache import cache
from django.core.paginator import Paginator
from django.db.models import Count,OuterRef,Subquery
from django.http import Http404,JsonResponse
from django.views.generic import TemplateView
from hitcount.models import Hit,HitCount
from hitcount.views import HitCountMixin
from menu.models import MenuGroup
from parler.utils import get_active_language_choices
from django.utils.text import Truncator
from backend.views import get_menu_caches,get_translated_active_page,get_menu_caches_footer
from core.common import get_agency_info
from django_authbox.common import add_months,get_site_id_front,get_template,get_week_date
from django_authbox.views import service_exists
from .calendar import sync_calendar_all
from .models import *
from django.utils.html import strip_tags
def get_calendar_ajax(request,year,month):A='get_calendar_ajax';print(A,request);print(A,year,month);res=sync_calendar_all(request,year,month);return JsonResponse(res,safe=_Y)
def get_menu_group(site_id):
	menugroup=MenuGroup.objects.filter(site_id=site_id,kind=1)
	if menugroup:return menugroup[0].id
	else:raise Http404("Menu Group belum terdaftar, silahkan daftar di halaman <a href='%s'>admin</a>"%_i)
def get_photo(model_name):return Subquery(Photo.objects.filter(object_id=OuterRef('id'),content_type__model=model_name).values('file_path')[:1])
def get_logo(site_id,max_data=1):
	subquery_foto=get_photo(_J);logo=Logo.objects.filter(site_id=site_id).values(_o).annotate(file_path=subquery_foto)[:max_data]
	if logo:return logo
	return _A
def get_base_url(request,path_count=0):
	A='/';my_path=request.path.split(A)
	if my_path:
		if len(my_path)>2:
			if not path_count:return my_path[0]+A+my_path[1]+A+my_path[2]
			tmp=''
			for i in range(0,path_count+1):tmp+=my_path[i]+A
			return tmp
def add_months(sourcedate,months):month=sourcedate.month-1+months;year=sourcedate.year+month//12;month=month%12+1;day=min(sourcedate.day,calendar.monthrange(year,month)[1]);return datetime.date(year,month,day)
def get_statistic(site_id,is_cache=_Y):
	C='user_agent';B=')';A='load from DB (';context={};tgl=datetime.datetime.now();content_type_id=ContentType.objects.get(app_label='sites',model='site');content_type_id=content_type_id.id if content_type_id else _A;hitcount_id=HitCount.objects.filter(content_type_id=content_type_id,object_pk=site_id).first();hitcount_id=hitcount_id.id if hitcount_id else _A;tgl00=tgl+datetime.timedelta(days=1);jam00=datetime.datetime(tgl00.year,tgl00.month,tgl00.day,0,1,0);timeout=(jam00-tgl00).seconds;selisih=0;tmp='hit_today';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);hit_today=Hit.objects.filter(hitcount_id=hitcount_id,created__year=tgl.year,created__month=tgl.month,created__day=tgl.day);tmp_cache=hit_today.count()if hit_today else 1;cache.set(tmp,tmp_cache,timeout,version=site_id);context[tmp]=tmp_cache
	else:hit_today=Hit.objects.filter(hitcount_id=hitcount_id,created__year=tgl.year,created__month=tgl.month,created__day=tgl.day);context[tmp]=hit_today.count()if hit_today else 1;selisih=context[tmp]-tmp_cache;print('selisih = ',selisih)
	tmp='hit_yesterday';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);start_date=tgl+datetime.timedelta(days=-1);tmp_cache=Hit.objects.filter(hitcount_id=hitcount_id,created__year=start_date.year,created__month=start_date.month,created__day=start_date.day).count();cache.set(tmp,tmp_cache,timeout,version=site_id)
	context[tmp]=tmp_cache;tmp='hit_this_week';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);start_date,end_date=get_week_date(tgl.year,tgl.month,tgl.day);tmp_cache=Hit.objects.filter(hitcount_id=hitcount_id,created__range=(start_date,end_date)).count();cache.set(tmp,tmp_cache,timeout,version=site_id)
	tmp_cache+=selisih;context[tmp]=tmp_cache;tmp='hit_last_week';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);start_date,end_date=get_week_date(tgl.year,tgl.month,tgl.day);start_date=start_date+datetime.timedelta(days=-7);end_date=end_date+datetime.timedelta(days=-7);tmp_cache=Hit.objects.filter(hitcount_id=hitcount_id,created__range=(start_date,end_date)).count();cache.set(tmp,tmp_cache,timeout,version=site_id)
	context[tmp]=tmp_cache;tmp='hit_this_month';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);tmp_cache=Hit.objects.filter(hitcount_id=hitcount_id,created__year=tgl.year,created__month=tgl.month).count();cache.set(tmp,tmp_cache,timeout,version=site_id)
	tmp_cache+=selisih;context[tmp]=tmp_cache;tmp='hit_last_month';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);start_date=add_months(tgl,-1);tmp_cache=Hit.objects.filter(hitcount_id=hitcount_id,created__year=start_date.year,created__month=start_date.month).count();cache.set(tmp,tmp_cache,timeout,version=site_id)
	context[tmp]=tmp_cache;start_date=tgl+datetime.timedelta(hours=-5);start_date=datetime.datetime(start_date.year,start_date.month,start_date.day,start_date.hour,0,0);end_date=datetime.datetime(tgl.year,tgl.month,tgl.day,tgl.hour,59,59);hit_online=Hit.objects.filter(hitcount_id=hitcount_id,created__range=(start_date,end_date)).values(C).order_by(C).distinct();context['hit_online']=hit_online.count()if hit_online else 1;tmp='hit_all';tmp_cache=cache.get(tmp,version=site_id)
	if not(is_cache and tmp_cache is not _A):print(A+tmp+B);hit_count=HitCount.objects.filter(object_pk=site_id,content_type_id=content_type_id);tmp_cache=hit_count[0].hits if hit_count else 1;cache.set(tmp,tmp_cache,timeout,version=site_id)
	tmp_cache+=selisih;context[tmp]=tmp_cache;return context
def get_model_content(site_id,lang,model,kind,max_data):
	subquery_foto=get_photo(kind);obj=model.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
	for i in obj:i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_banner(site_id,max_data=3):subquery_foto=get_photo(_u);return Banner.objects.filter(site_id=site_id).annotate(file_path=subquery_foto)[:max_data]
def get_announcement(site_id,lang,max_data=3,max_words=20):
	subquery_foto=get_photo(_D);obj=Announcement.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by('priority',_C)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_slideshow(site_id,lang,max_data=5):subquery_foto=get_photo(_Q);obj=SlideShow.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_C)[:max_data];obj=list(obj);random.shuffle(obj);return obj
def get_fasilities(site_id,lang,exclude_id=[],is_header_text=_A,is_shuffle=_A):
	print('exclude_id',exclude_id);subquery_foto=get_photo(_Z)
	if is_header_text is _A:print('isheadertext1',is_header_text);obj=Fasilities.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).exclude(id__in=exclude_id).annotate(file_path=subquery_foto).order_by(_B,_R)[:10];print(obj)
	else:print('isheadertext2',is_header_text);obj=Fasilities.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).exclude(id__in=exclude_id).exclude(is_header_text=is_header_text).annotate(file_path=subquery_foto).order_by(_B,_R)[:10]
	obj=list(obj)
	if is_shuffle:random.shuffle(obj)
	return obj
def get_offers(site_id,lang,exclude_id=[],is_header_text=_A,is_shuffle=_A):
	subquery_foto=get_photo(_a)
	if is_header_text is _A:obj=Offers.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).exclude(id__in=exclude_id).annotate(file_path=subquery_foto).order_by(_B,_R)[:10]
	else:obj=Offers.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).exclude(id__in=exclude_id).exclude(is_header_text=_G).annotate(file_path=subquery_foto).order_by(_B,_R)[:10]
	return obj
def get_whyus(site_id,lang,max_data=3):return WhyUs.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_B,_C)[:max_data]
def get_dailyalert(site_id,lang,max_data=3):return DailyAlert.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_C)[:max_data]
def get_howitworks(site_id,lang,max_data=3,max_words=20):
	obj=HowItWorks.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_B,_R)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_aboutus(site_id,lang,max_data=1,max_words=100):subquery_foto=get_photo(_j);obj=AboutUs.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto)[:max_data];return obj
def get_testimony(site_id,lang,max_data=3,max_words=20):
	subquery_foto=get_photo(_k);obj=Testimony.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_product(site_id,lang,max_data=3,max_words=20):subquery_foto=get_photo(_b);obj=Product.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_R)[:max_data];return obj
def get_greeting(site_id,lang,max_data=1):subquery_foto=get_photo(_c);return Greeting.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_C)[:max_data]
def get_events(site_id,lang,max_data=3):subquery_foto=get_photo(_K);return Events.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
def get_photogallery(site_id,lang,max_data=3):subquery_foto=get_photo(_H);return PhotoGallery.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_R)[:max_data]
def get_videogallery(site_id,lang,max_data=3):subquery_foto=get_photo(_v);return VideoGallery.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
def get_relatedlink(site_id,lang,max_data=3):return RelatedLink.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_C)[:max_data]
def get_news(site_id,lang,max_data=3,max_words=20):
	subquery_foto=get_photo(_F);obj=News.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_article(site_id,lang,max_data=3,max_words=20):
	subquery_foto=get_photo(_L);obj=Article.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_document(site_id,lang,max_data=3,max_words=20):
	obj=Document.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_B,_C)[:max_data]
	for i in obj:
		if not i.is_header_text:i.content=Truncator(strip_tags(i.content)).words(max_words);i.created_at=get_natural_datetime(i.created_at)
	return obj
def get_socialmedia(site_id,max_data=5):return SocialMedia.objects.filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_C)[:max_data]
def get_categories_list(site_id,lang,max_data,model):
	A='categories_id';subquery=Subquery(Categories.objects.translated(lang).filter(id=OuterRef(A)).values(_w)[:1]);subquery_slug=Subquery(Categories.objects.translated(lang).filter(id=OuterRef(A)).values(_S)[:1]);categories_list=[];obj=model.objects.filter(site_id=site_id).values(A).annotate(count=Count(A)).annotate(name=subquery).annotate(slug=subquery_slug).order_by(A)[:max_data]
	if obj:
		all_data=0
		for i in obj:all_data+=i[_l]
		categories_list=list(obj);categories_all={A:0,_l:all_data,_o:'All',_S:_p};categories_list.insert(0,categories_all);return categories_list
def get_tags_list(site_id,lang,max_data,model):
	site_name={f"{model.__name__.lower()}__site":f"{site_id}"};val=f"{model.__name__.lower()}__tags";subquery=Subquery(Tags.objects.translated(lang).filter(id=OuterRef(val)).values(_w)[:1]);subquery_slug=Subquery(Tags.objects.translated(lang).filter(id=OuterRef(val)).values(_S)[:1]);tags_list=[];obj=model.tags.through.objects.filter(**site_name).values(val).annotate(count=Count(val)).annotate(name=subquery).annotate(slug=subquery_slug).order_by(val)[:max_data]
	if obj:
		all_data=0
		for i in obj:all_data+=i[_l]
		tags_list=list(obj);tags_all={'tags_id':0,_l:all_data,_o:'All',_S:_p};tags_list.insert(0,tags_all);return tags_list
def get_latest_model(site_id,lang,max_data,model,kind,exclude_slug=_A):
	subquery_foto=get_photo(kind)
	if exclude_slug:return model.objects.translated(lang).filter(site_id=site_id).annotate(file_path=subquery_foto).exclude(slug=exclude_slug).order_by(_B,_C)[:max_data]
	return model.objects.translated(lang).filter(site_id=site_id).annotate(file_path=subquery_foto).order_by(_B,_C)[:max_data]
def get_random_items(qs,max_data):possible_ids=list(qs.values_list('id',flat=_G));req_no_of_random_items=len(possible_ids)+1 if len(possible_ids)+1<max_data else max_data;possible_ids=random.choices(possible_ids,k=req_no_of_random_items);return qs.filter(pk__in=possible_ids)
def get_related_model(site_id,lang,max_data,model,kind,exclude_slug=_A):
	subquery_foto=get_photo(kind)
	if exclude_slug:qs=model.objects.translated(lang).filter(site_id=site_id,is_header_text=_Y).exclude(slug=exclude_slug)
	else:qs=model.objects.translated(lang).filter(site_id=site_id,is_header_text=_Y)
	if qs:random_paint=get_random_items(qs,max_data);random_paint=random_paint.annotate(file_path=subquery_foto);header_text=model.objects.translated(lang).filter(site_id=site_id,is_header_text=_G).annotate(file_path=subquery_foto);return (header_text|random_paint).order_by(_B)
def get_content_detail(site_id,lang,model,kind,slug):
	subquery_foto=get_photo(kind);obj=model.objects.translated(lang).filter(site_id=site_id,slug=slug).annotate(file_path=subquery_foto)
	if obj:obj=obj.get();obj.created_at=get_natural_datetime(obj.created_at);return obj
	raise Http404(_q)
def get_content_list(site_id,lang,model,kind,slug):
	A='-created_at'
	if not slug:raise Http404(_q)
	subquery_foto=get_photo(kind)
	if slug==_p:return model.objects.translated(lang).filter(site_id=site_id,is_header_text=_Y).annotate(file_path=subquery_foto).order_by(A)
	else:
		categories=Categories.objects.filter(slug=slug);categories=categories.get()if categories else _A
		if categories:return model.objects.translated(lang).filter(site_id=site_id,categories_id=categories.id,is_header_text=_Y).annotate(file_path=subquery_foto).order_by(A)
		raise Http404('Categories '+slug+' tidak ditemukan!')
def get_location(site_id,lang,max_data=2):return Location.objects.language(lang).filter(site_id=site_id,status=OptStatusPublish.PUBLISHED).order_by(_B,_C)[:max_data]
def get_og(site_id):
	ret={};ret['og_type']='website';site=Site.objects.get(id=site_id)
	if site:ret['og_url']=site.domain
	return ret
class IndexView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		hostname=request.get_host();hostname_split=hostname.strip().split('.')
		if hostname_split[0]=='www':hostname_split.pop(0);hostname='.'.join(hostname_split);return redirect(f"https://{hostname}")
		service=service_exists(request);print('service from index',service);service_type=service;print('servicetype',service_type)
		if not service_type:raise Http404("service belum terdaftar, silahkan daftar di halaman <a href='%s'>admin</a>"%_T)
		self.site_id=get_site_id_front(request)
		if request.session.session_key:obj=Site.objects.get(id=self.site_id);hit_count=HitCount.objects.get_for_object(obj);HitCountMixin.hit_count(request,hit_count)
		template=get_template(self.site_id);print('template=',template);self.template_name=template+'index.html';return super().get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super().get_context_data(*(args),**kwargs);context[_m]='index';context[_M]=self.request.device[_M];active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,kinds=1,exclude_menu=0);context.update(menu);menu_footer1=get_menu_caches_footer(self.request,_N,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_N);context.update(menu_footer1);menu_footer2=get_menu_caches_footer(self.request,_O,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_O);context.update(menu_footer2);agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];context[_u]=get_banner(self.site_id);context[_D]=get_announcement(self.site_id,lang,max_data=5);context[_Q]=get_slideshow(self.site_id,lang,max_data=5);context['dailyalert']=get_dailyalert(self.site_id,lang,max_data=5);context[_g]=get_howitworks(self.site_id,lang,max_data=5);context[_j]=get_aboutus(self.site_id,lang);context[_k]=get_testimony(self.site_id,lang,max_data=5);context[_b]=get_product(self.site_id,lang,max_data=5);context['whyus']=get_whyus(self.site_id,lang,max_data=5);context[_Z]=get_fasilities(self.site_id,lang);context[_a]=get_offers(self.site_id,lang);context[_c]=get_greeting(self.site_id,lang);context[_K]=get_events(self.site_id,lang);context[_H]=get_photogallery(self.site_id,lang);context[_v]=get_videogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_F]=get_news(self.site_id,lang,max_data=5);context[_L]=get_article(self.site_id,lang,max_data=5);context[_h]=get_document(self.site_id,lang,max_data=5);context[_X]=get_socialmedia(self.site_id,max_data=5);context['location']=get_location(self.site_id,lang);context[_I]=get_base_url(self.request);og=get_og(self.site_id);context.update(og);return context
class CheckOutView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'checkout.html';return super().get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):
		context=super().get_context_data(*(args),**kwargs);context[_m]='checkout';context[_M]=self.request.device[_M];active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,kinds=1,exclude_menu=0);context.update(menu);menu_footer1=get_menu_caches_footer(self.request,_N,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_N);context.update(menu_footer1);menu_footer2=get_menu_caches_footer(self.request,_O,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_O);context.update(menu_footer2);context[_e]=get_menu_group(self.site_id);slug=self.kwargs[_S]
		if not slug:raise Http404(_r%(self.request.get_host(),_i))
		kind=self.kwargs[_P];context[_P]=kind;model=apps.get_model(_E,kind);agency=get_agency_info(self.site_id);context.update(agency);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];content_detail=get_content_detail(self.site_id,lang,model,kind,slug);context[_x]=content_detail;context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_Q]=get_slideshow(self.site_id,lang);context[_I]=get_base_url(self.request,1);print(_y,context[_I]);return context
class DetailView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'detail.html';return super(DetailView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):
		context=super(DetailView,self).get_context_data(*(args),**kwargs);context[_m]='detail';context[_M]=self.request.device[_M];active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,kinds=1,exclude_menu=0);context.update(menu);menu_footer1=get_menu_caches_footer(self.request,_N,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_N);context.update(menu_footer1);menu_footer2=get_menu_caches_footer(self.request,_O,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_O);context.update(menu_footer2);context[_e]=get_menu_group(self.site_id);slug=self.kwargs[_S]
		if not slug:raise Http404(_r%(self.request.get_host(),_i))
		agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];model_with_categories=[_D,_F,_L,_K,_h,_n];model_with_content=[_D,_F,_L,_K,_Q,_c,_n,_H,_Z,_a,_g,_j,_k,_b,_h];model_randomize=[_F,_L,_K,_Z,_a,_g,_b];kind=self.kwargs[_P];print('kind detail',kind)
		if kind in model_with_content:context[_P]=kind
		context[_D]=get_announcement(self.site_id,lang,6);model=apps.get_model(_E,kind);latest_kind=_A;random_paint=_A;print('1',model_randomize)
		if kind in model_with_categories:context[_z]=get_categories_list(self.site_id,lang,10,model);context[_A0]=get_tags_list(self.site_id,lang,10,model);latest_kind=get_latest_model(self.site_id,lang,4,model,kind,slug);random_paint=get_related_model(self.site_id,lang,4,model,kind,slug)
		print(_P,kind);idx=0
		for i in model_randomize:
			if i==kind.lower():model_randomize.pop(idx);break
			idx+=1
		print('2',model_randomize);tmp_kind=_A
		if not latest_kind:
			random.shuffle(model_randomize)
			for i in model_randomize:
				print(_f,i);tmp_kind=i;tmp_model=apps.get_model(_E,i);latest_kind=get_latest_model(self.site_id,lang,4,tmp_model,i)
				if latest_kind:break
		context[_A1]=latest_kind;idx=0
		for i in model_randomize:
			if i==tmp_kind:model_randomize.pop(idx);break
			idx+=1
		print('3',model_randomize)
		if not random_paint:
			random.shuffle(model_randomize)
			for i in model_randomize:
				print(_f,i);tmp_kind=i;tmp_model=apps.get_model(_E,i);random_paint=get_related_model(self.site_id,lang,4,tmp_model,i)
				if random_paint:break
		context[_A2]=random_paint;idx=0
		for i in model_randomize:
			if i==tmp_kind:model_randomize.pop(idx);break
			idx+=1
		print('4',model_randomize);random_model=_A;random.shuffle(model_randomize)
		for i in model_randomize:
			print(_f,i);tmp_model=apps.get_model(_E,i);random_model=get_model_content(self.site_id,lang,tmp_model,i,7)
			if random_model:break
		context[_A3]=random_model;content_detail=get_content_detail(self.site_id,lang,model,kind,slug);context[_x]=content_detail;hit_count=HitCount.objects.get_for_object(content_detail);hit_count_response=HitCountMixin.hit_count(self.request,hit_count);context[_H]=get_photogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_Q]=get_slideshow(self.site_id,lang);context[_I]=get_base_url(self.request,1);print(_y,context[_I]);return context
class ListView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'list.html';return super(ListView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):
		context=super(ListView,self).get_context_data(*(args),**kwargs);print('enter list view');context[_m]='list';context[_M]=self.request.device[_M];active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,kinds=1,exclude_menu=0);context.update(menu);menu_footer1=get_menu_caches_footer(self.request,_N,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_N);print('menu_footer1',menu_footer1);context.update(menu_footer1);menu_footer2=get_menu_caches_footer(self.request,_O,self.site_id,active_page,kinds=1,exclude_menu=1,parent_name=_O);context.update(menu_footer2);context[_e]=get_menu_group(self.site_id);slug=self.kwargs[_S]
		if not slug:raise Http404(_r%(self.request.get_host(),_i))
		agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];model_with_categories=[_D,_F,_L,_K,_h,_n];model_with_content=[_D,_F,_L,_K,_Q,_c,_n,_H,_Z,_a,_g,_j,_k,_b,_h];model_randomize=[_F,_L,_K,_Z,_a,_g,_b];kind=self.kwargs[_P]
		if kind in model_with_content:context[_P]=kind
		else:raise Http404(_q)
		print('Kind = ',kind);context[_D]=get_announcement(self.site_id,lang,6);model=apps.get_model(_E,kind);latest_kind=_A;random_paint=_A;print('1',model_randomize)
		if kind in model_with_categories:context[_z]=get_categories_list(self.site_id,lang,10,model);context[_A0]=get_tags_list(self.site_id,lang,10,model);latest_kind=get_latest_model(self.site_id,lang,4,model,kind,slug);random_paint=get_related_model(self.site_id,lang,4,model,kind,slug)
		print('detail model = ',model,kind);print(_P,kind);idx=0
		for i in model_randomize:
			if i==kind.lower():model_randomize.pop(idx);break
			idx+=1
		print('2',model_randomize);tmp_kind=_A
		if not latest_kind:
			random.shuffle(model_randomize)
			for i in model_randomize:
				print(_f,i);tmp_kind=i;tmp_model=apps.get_model(_E,i);latest_kind=get_latest_model(self.site_id,lang,4,tmp_model,i)
				if latest_kind:break
		context[_A1]=latest_kind;idx=0
		for i in model_randomize:
			if i==tmp_kind:model_randomize.pop(idx);break
			idx+=1
		print('3',model_randomize)
		if not random_paint:
			random.shuffle(model_randomize)
			for i in model_randomize:
				print(_f,i);tmp_kind=i;tmp_model=apps.get_model(_E,i);random_paint=get_related_model(self.site_id,lang,4,tmp_model,i)
				if random_paint:break
		context[_A2]=random_paint;idx=0
		for i in model_randomize:
			if i==tmp_kind:model_randomize.pop(idx);break
			idx+=1
		print('4',model_randomize);random_model=_A;random.shuffle(model_randomize)
		for i in model_randomize:
			print(_f,i);tmp_model=apps.get_model(_E,i);random_model=get_model_content(self.site_id,lang,tmp_model,i,7)
			if random_model:break
		context[_A3]=random_model;content_list=get_content_list(self.site_id,lang,model,kind,slug)
		if content_list:kind_data_per_page=8;paginator=Paginator(content_list,kind_data_per_page);page_number=self.request.GET.get('page',1);context['page_list']=paginator.get_page(page_number)
		context[_H]=get_photogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_I]=get_base_url(self.request);context[_Q]=get_slideshow(self.site_id,lang);return context
class DescriptionView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'description.html';return super(DescriptionView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(DescriptionView,self).get_context_data(*(args),**kwargs);active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,kinds=1);context.update(menu);context[_e]=get_menu_group(self.site_id);agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];context[_D]=get_announcement(self.site_id,lang,6);model=apps.get_model(_E,_D);context[_s]=get_latest_model(self.site_id,lang,3,model,_D);model=apps.get_model(_E,_F);context[_t]=get_latest_model(self.site_id,lang,3,model,_F);context[_H]=get_photogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_I]=get_base_url(self.request);return context
class GreetingView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'greeting.html';return super(GreetingView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(GreetingView,self).get_context_data(*(args),**kwargs);active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,1);context.update(menu);context[_e]=get_menu_group(self.site_id);agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];context[_D]=get_announcement(self.site_id,lang,6);context[_c]=get_greeting(self.site_id,lang);model=apps.get_model(_E,_D);context[_s]=get_latest_model(self.site_id,lang,3,model,_D);model=apps.get_model(_E,_F);context[_t]=get_latest_model(self.site_id,lang,3,model,_F);context[_H]=get_photogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_I]=get_base_url(self.request);return context
class BookingView(TemplateView):
	site_id=_A
	def get(self,request,*args,**kwargs):
		self.site_id=get_site_id_front(request);service=service_exists(request)
		if not service:raise Http404(_d%(request.get_host(),_T))
		template=get_template(self.site_id);self.template_name=template+'booking.html';return super(BookingView,self).get(request,*(args),**kwargs)
	def get_context_data(self,*args,**kwargs):context=super(BookingView,self).get_context_data(*(args),**kwargs);active_page=get_translated_active_page(_U);menu=get_menu_caches(self.request,_V,self.site_id,active_page,1);context.update(menu);context[_e]=get_menu_group(self.site_id);agency=get_agency_info(self.site_id);context.update(agency);statistic=get_statistic(self.site_id,_G);context.update(statistic);context[_J]=get_logo(self.site_id);lang=get_active_language_choices()[0];context[_D]=get_announcement(self.site_id,lang,6);context[_c]=get_greeting(self.site_id,lang);model=apps.get_model(_E,_D);context[_s]=get_latest_model(self.site_id,lang,3,model,_D);model=apps.get_model(_E,_F);context[_t]=get_latest_model(self.site_id,lang,3,model,_F);context[_H]=get_photogallery(self.site_id,lang);context[_W]=get_relatedlink(self.site_id,lang);context[_X]=get_socialmedia(self.site_id);context[_I]=get_base_url(self.request);return context
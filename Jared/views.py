from django.shortcuts import render
from django import template
from django.http import HttpResponse

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from Jared.models import Article
from Jared.serializer import ArticleSerializer


# Create your views here.

def index_view(request):
	'''
	generate the index page
	'''
	return render(request, 'blog-index.html')



def article_pages(request, pn):
	'''
	generate the articles'views (article number: 5) of specified page
	'''
	if request.method == 'GET':
		request_dic = {'page': pn}
		page_template = template.loader.get_template('blog-page.html')
		page_context = {'request_dic': request_dic}
		return HttpResponse(page_template.render(page_context))



def single_article(request, id):
	'''
	render the single article
	'''
	if request.method == 'GET':
		request_dic = {'article_id': id}
		article_template = template.loader.get_template('blog-article.html')
		article_context = {'request_dic': request_dic}
		return HttpResponse(article_template.render(article_context))


@csrf_exempt
@api_view(['GET'])
def article_list(request):
	"""
	list all articles
	"""
	if request.method == 'GET':
		article_all = Article.objects.all()
		artc_all_serializer = ArticleSerializer(article_all, many=True)
#		return JsonResponse(artc_all_serializer.data, safe=False)
		return Response(artc_all_serializer.data)



@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
	"""
	show or modify the detail of specified article, or delete the article
	"""
	try:
		article_one = Article.objects.get(pk=pk)
	except Article.DoesNotExist:
#		return HttpResponse(status=404)
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		artc_serializer = ArticleSerializer(article_one)
#		return JsonResponse(artc_serializer.data)
		return Response(artc_serializer.data)

	elif request.method == 'PUT':
		jsondata = JSONParser().parse(request)
		artc_serializer = ArticleSerializer(article_one, data=jsondata)
		if artc_serializer.is_valid():
			artc_serializer.save()
#			return JsonResponse(artc_serializer.data)
			return Response(artc_serializer.data)
#		return JsonResponse(artc_serializer.errors, status=400)
		return Response(artc_serializer.errors, status=HTTP_400_BAD_REQUEST)

	elif request.method == 'DELETE':
		article_one.delete()
#		return HttpResponse(status=204)
		return Response(status=HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET'])
def article_by_page(request, pg):
	"""
	show articles by page, default 5 articles every page
	"""

	# get all articles and count, and calculate the page number
	PAGE_SIZE = 5
	article_all = Article.objects.all()
	article_count = article_all.count()
	total_page_num = int(article_count/PAGE_SIZE) + 1 if article_count%PAGE_SIZE != 0 else int(article_count/PAGE_SIZE)

	# page number not correct
	if int(pg) not in range(1, total_page_num+1):
		return Response(status=status.HTTP_404_NOT_FOUND)

	# article's reverse order, for the retrive of latest article
	article_all_reverse = article_all[::-1]
	
	if request.method == 'GET':
		article_pg = article_all_reverse[(int(pg)-1)*5:((int(pg)-1)*5+5)]
		article_pg_serializer = ArticleSerializer(article_pg, many=True)
		return Response({
			'total_page': total_page_num,
			'article_data': article_pg_serializer.data
		})

	
	



		







from rest_framework import serializers

from Jared.models import Article

 

class ArticleSerializer(serializers.Serializer):

	article_id = serializers.IntegerField(read_only=True)

	title = serializers.CharField(required=True, allow_blank=False, max_length=256)

	content = serializers.CharField(required=True, allow_blank=True, max_length=102400)

	author = serializers.CharField(required=True, allow_blank=True, max_length=64)

	tag = serializers.SerializerMethodField()


	class Meta:
		model = Article


	def get_tag(self, obj):
		return obj.tag.values()


	def create(self, validate_data):

		return Article.objects.create(**validate_data)


	def update(self, instance, validate_data):

		instance.title = validate_data.get('title', instance.title)

		instance.content = validate_data.get('content', instance.content)

		instance.save()

		return instance





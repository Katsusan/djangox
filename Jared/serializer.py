from rest_framework import serializers

from Jared.models import Article

 

#from pygments.lexers import get_all_lexers

#from pygments.styles import get_all_styles

 

#LEXERS = [item for item in get_all_lexers() if item[1]]

#LANGUAGE_CHIOCES = sorted([(item[1][0], item[0]) for item in LEXERS])

#STYLES_CHOICE = sorted((item, item) for item in get_all_styles())

 

class ArticleSerializer(serializers.Serializer):

	article_id = serializers.IntegerField(read_only=True)

	title = serializers.CharField(required=True, allow_blank=False, max_length=256)

	content = serializers.CharField(required=True, allow_blank=True, max_length=102400)

#	code = serializers.CharField(style={'base_template': 'textarea.html'})

#	linenos = serializers.BooleanField(required=False)

#	language = serializers.ChoiceField(choices=LANGUAGE_CHIOCES, default='python')

#	style = serializers.ChoiceField(choices=STYLES_CHOICE, default='friendly')

 

	def create(self, validate_data):

		return Article.objects.create(**validate_data)

 

	def update(self, instance, validate_data):

		instance.title = validate_data.get('title', instance.title)

#		instance.code = validate_data.get('code', instance.code )

		instance.content = validate_data.get('content', instance.content)

#		instance.linenos = validate_data.get('linenos', instance.linenos)

#		instance.language = validate_data.get('language', instance.language)

#		instance.style = validate_data.get('style', instance.style)

 

		instance.save()

			return instance





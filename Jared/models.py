from django.db import models
from django.forms import ModelForm

# Create your models here.

class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	author = models.ForeignKey("User", to_field='username', on_delete=models.CASCADE)
	title = models.CharField(max_length=256)
	content = models.TextField("body of article", max_length=102400)
	created_time = models.DateTimeField("the create time of article", auto_now_add=True)
	modified_time = models.DateTimeField("the article's last modified time", auto_now=True)
	created_date = models.DateField(auto_now_add=True)
	tag = models.ManyToManyField('Tag', null=True, blank=True)
	comment = models.ForeignKey("Comment", to_field='comment_content', on_delete=models.CASCADE, null=True, blank=True)
	access_times = models.IntegerField(default=1, editable=False)

	def __str__(self):
		return u'%s' %(self.title)

class Comment(models.Model):
	comment_id = models.AutoField(primary_key=True)
	comment_time = models.DateTimeField("commit time of comment", auto_now_add=True)
	comment_content = models.CharField(max_length=255, unique=True,null=True, blank=True)
	commit_nickname = models.CharField(max_length=64)
	commit_email = models.EmailField()

	def __str__(self):
		return u'%s' %(self.comment_content)

class Tag(models.Model):
	tagname = models.CharField(max_length=256)

	def __str__(self):
		return u'%s' %(self.tagname)

	
class User(models.Model):
	uid = models.AutoField(primary_key=True)
	username = models.CharField(max_length=64, unique=True)
#	photo = models.ImageField()
	isactive = models.BooleanField(default=True)
	email = models.EmailField()
	join_time = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return u'%s' %(self.username)


class ArticleForm(ModelForm):
	class Meta:
		model = Article
		fields = ['title', 'author', 'content', 'tag']

	

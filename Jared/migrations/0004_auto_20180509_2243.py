# Generated by Django 2.0.3 on 2018-05-09 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Jared', '0003_article_access_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Jared.Comment', to_field='comment_content'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, to='Jared.Tag'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_content',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]

# -*- coding: utf-8 -*-

from django.db import models
from datetime import datetime

# Create your models here.

class Article(models.Model):
    class Meta():
        db_table = 'article'
    article_title = models.CharField(max_length = 200, verbose_name='Заголовок')
    article_text = models.TextField(max_length=10000, verbose_name='Текст статьи')
    article_date = models.DateTimeField(verbose_name='Дата создания')
    article_likes = models.IntegerField(default=0)
    article_first_chr = lambda self: self.article_title.split()[0][0]
    article_first_chr.short_description = 'А-Я'

class Comments(models.Model):
    class Meta():
        db_table = 'article_comments'
    comments_text = models.TextField(verbose_name='Текст комментария')
    comments_article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.SET_NULL)
    comments_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
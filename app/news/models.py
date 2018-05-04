# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):

    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Артикль'
        verbose_name_plural = u'Артикли'
        ordering = ('pub_date', )

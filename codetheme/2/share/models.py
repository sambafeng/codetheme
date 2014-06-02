#coding=utf-8
from django.db import models


class Code(models.Model):
    name = models.CharField(max_length=100)
    user = models.IntegerField()
    add_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
            return self.name

    class Meta:
        db_table = 'codes'

        

class Theme(models.Model):
    TYPE = (
        (0, u'未进行'),
        (1, u'进行中'),
        (2, u'已完成'),
    )
    title = models.CharField(max_length=100)
    user = models.IntegerField()
    type = models.ForeignKey(Code, null=True)
    tag = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=1000, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    add_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    status = models.IntegerField(default=0, choices=TYPE)
    schedule = models.IntegerField(default=0)   # 进度
    def __unicode__(self):
            return self.title

    class Meta:
        db_table = 'theme'

    

class Tag(models.Model):
    name = models.CharField(max_length=100)
    user = models.IntegerField()
    add_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
            return self.name

    class Meta:
        db_table = 'tags'

class Share(models.Model):
    title = models.CharField(max_length=100)
    user = models.IntegerField()
    type = models.ForeignKey(Code,null=True)
    desc = models.CharField(max_length=500,null=True)
    url = models.URLField()
    tag = models.CharField(max_length=100,null=True)
    author = models.CharField(max_length=50,null=True)
    add_date = models.DateTimeField(auto_now=True,auto_now_add=True)

    def __unicode__(self):
            return self.title

    class Meta:
        db_table = 'share'


class Node(models.Model):
    obj = models.ForeignKey(Theme)                  # 编程主题id
    title = models.CharField(max_length=100)
    url = models.URLField(null=True)                # 外战锚点链接
    deep = models.IntegerField()                    # 当前节点的深度
    parent_id = models.IntegerField()               # 父ID
    sequence = models.IntegerField(default=1)       # 排序(数值愈大越靠前)
    add_date = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
            return self.title

    class Meta:
        db_table = 'node'
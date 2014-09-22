#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from myblog.models import *

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)



class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author', 'publish_time', )
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-caption',)
    filter_horizontal = ('tags',)
    search_fields = ('caption',)
    # raw_id_fields = ('author',)  # 它是一个包含外键字段名称的元组，它包含的字段将被展现成`` 文本框`` ，而不再是`` 下拉框`` 。

class CMC_Board_Admin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('cmc_sn', 'id', 'cmc_lab_ref' ,'cmc_owner', 'update_time','cmc_note')
    list_filter = ('update_time',)
    date_hierarchy = 'update_time'
    ordering = ('cmc_sn',)
    search_fields = ('cmc_sn',)

class SFPAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('sfp_sn','id','sfp_mpn','sfp_owner','sfp_update_time')
    ordering = ('sfp_sn',)
    search_fields = ('sfp_sn',)

class SFPVendorAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('vendor','id','mpn' ,'optical_type','is_cisco_part')
    ordering = ('vendor',)
    search_fields = ('mpn',)

class LogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('log_date','log_mode','log_count' ,'log_note','log_person')
    ordering = ('-log_date',)
    search_fields = ('log_note',)


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(CMC_Board,CMC_Board_Admin)
admin.site.register(SFPVendor,SFPVendorAdmin)
admin.site.register(SFP,SFPAdmin)
admin.site.register(Record_log,LogAdmin)








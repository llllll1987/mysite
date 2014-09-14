from django.db import models

# Create your models here.


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)


class Zhiwei_CMC_Board(models.Model):
    """docstring for Boards"""
    cmc_lab_ref = models.CharField(max_length=10)
    cmc_sn = models.CharField(max_length=11)
    cmc_mac = models.CharField(max_length=15)
    cmc_owner = models.CharField(max_length=50)
    cmc_note = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.cmc_lab_ref, self.cmc_sn)


class CMC_Board(models.Model):
    """docstring for Boards"""
    cmc_sn = models.CharField(max_length=11)
    cmc_lab_ref = models.CharField(max_length=10)
    cmc_mac = models.CharField(max_length=18)
    cmc_owner = models.CharField(max_length=50)
    update_time = models.DateTimeField(auto_now=True)
    cmc_note = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.cmc_sn, self.cmc_owner) 

class SFPVendor(models.Model):
    """docstring for Author"""
    vendor = models.CharField(max_length=30)
    mpn = models.CharField(max_length=30)
    optical_type = models.CharField(max_length=30)
    is_cisco_part = models.BooleanField()

    def __unicode__(self):
        return u'%s' % (self.mpn)


class SFP(models.Model):
    """docstring for Boards"""
    sfp_sn = models.CharField(max_length=18)
    sfp_mpn = models.ForeignKey(SFPVendor)
    sfp_owner = models.ForeignKey(Author)
    sfp_update_time = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s' % (self.sfp_sn, self.sfp_owner)




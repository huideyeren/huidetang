from django.db import models
from django.contrib.auth.models import AbstractUser

from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager

from taggit.models import TaggedItemBase

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailmarkdown.edit_handlers import MarkdownPanel
from wagtailmarkdown.fields import MarkdownField

class User(AbstractUser):
    profile = MarkdownField(verbose_name=u'プロフィール')
    nickname = models.CharField(verbose_name=u'ニックネーム', max_length=25, null=True, blank=True)
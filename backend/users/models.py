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


class UserInterest(TaggedItemBase):
    content_object = ParentalKey(
        "User",
        on_delete=models.CASCADE,
        related_name="interest_items"
    )


class User(AbstractUser):
    profile = MarkdownField(verbose_name=u'プロフィール')
    nickname = models.CharField(verbose_name=u'ニックネーム', max_length=25, null=True, blank=True)
    middle_name = models.CharField(verbose_name=u'ミドルネーム', max_length=10, null=True, blank=True)
    is_surname_first = models.BooleanField(verbose_name=u'姓が先の表記', null=True, blank=True)
    use_nickname = models.BooleanField(verbose_name=u'ニックネームの使用', null=True, blank=True)
    interest = ClusterTaggableManager(
        verbose_name=u'興味を持っていること',
        through=UserInterest,
        blank=True
    )
    twitter_id = models.CharField(verbose_name=u'Twitterのアカウント', max_length=50, null=True, blank=True)
    facebook_id = models.CharField(verbose_name=u'Facebookのアカウント', max_length=50, null=True, blank=True)
    instagram_id = models.CharField(verbose_name=u'Instagramのアカウント', max_length=50, null=True, blank=True)
    github_id = models.CharField(verbose_name=u'GitHubのアカウント', max_length=50, null=True, blank=True)
    line_url = models.URLField(verbose_name=u'LINEの友だち追加リンク', max_length=255, null=True, blank=True)
    steam_id = models.CharField(verbose_name=u'Steamのアカウント', max_length=50, null=True, blank=True)
    hatena_id = models.CharField(verbose_name=u'はてなブックマークのアカウント', max_length=50, null=True, blank=True)
    qiita_id = models.CharField(verbose_name=u'Qiitaのアカウント', max_length=50, null=True, blank=True)
    note_id = models.CharField(verbose_name=u'noteのアカウント', max_length=50, null=True, blank=True)
    resume_url = models.URLField(verbose_name=u'職務経歴書のリンク', max_length=255, null=True, blank=True)
    charactor_list_url = models.URLField(verbose_name=u'キャラクターリストのURL', max_length=255, null=True, blank=True)




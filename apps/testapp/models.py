from django.db import models
from django.utils.translation import ugettext_lazy as _


class TestModel(models.Model):

    title = models.CharField(max_length=255,
                             verbose_name=_(u'title'))
    image = models.ImageField(_(u'image file'),
                              upload_to='catalog')
    enabled = models.BooleanField(verbose_name=_('enabled'),
                                  default=True)
    weight = models.PositiveIntegerField(verbose_name=_(u'weight'),
                                         null=True,
                                         blank=True)

    class Meta:

        verbose_name = _(u'test item')
        verbose_name_plural = _(u'test items')
        ordering = ['weight',]

    def __unicode__(self):
        return u'{}'.format(self.title)

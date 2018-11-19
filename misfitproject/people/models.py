from django.db import models
from django.utils.translation import ugettext as _
from django.contrib.auth.models import AbstractUser, UserManager

from django.db.models import signals

# Create your models here.



class Profile(AbstractUser):

    """Fully featured user profile"""

    organization = models.CharField(
        _('Organization Name'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('name of the responsible organization'))
    profile = models.TextField(_('Profile'), null=True, blank=True, help_text=_('introduce yourself'))
    profile_pic = models.ImageField(blank=True, null=True)
    position = models.CharField(
        _('Position Name'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('role or position of the responsible person'))
    voice = models.CharField(_('Voice'), max_length=255, blank=True, null=True, help_text=_(
        'telephone number by which individuals can speak to the responsible organization or individual'))
    address = models.CharField(
        _('Delivery Point'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('physical and email address at which the organization or individual may be contacted'))
    city = models.CharField(
        _('City'),
        max_length=255,
        blank=True,
        null=True,
        help_text=_('city of the location'))

    def __unicode__(self):
        return u"%s" % (self.username)

    def class_name(value):
        return value.__class__.__name__

    USERNAME_FIELD = 'username'


def get_anonymous_user_instance(Profile):
    return Profile(pk=-1, username='AnonymousUser')


# from django.core.urlresolvers import reverse
# from django.http import Http404
# def profile_pre_save(instance, sender, **kw):
#     import pdb; pdb.set_trace()
#     return Http404('this email is not permitted')
#
# signals.pre_save.connect(profile_pre_save, sender=Profile)
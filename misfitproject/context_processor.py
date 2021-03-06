# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.conf import settings
from django.contrib.sites.models import Site


def resource_urls(request):
    """Global values to pass to templates"""
    # site = Site.objects.get_current()
    HR = False
    MEMBER = False
    MANAGER = False
    if request.user.groups.filter(name='hr').exists():
        HR = True
    elif request.user.groups.filter(name='manager').exists():
        MANAGER = True
    else:
        MEMBER = True

    defaults = dict(
        STATIC_URL=settings.STATIC_URL,
        MEMBER=MEMBER,
        MANAGER=MANAGER,
        HR=HR,
        # REGISTRATION_OPEN=settings.REGISTRATION_OPEN,
        # SITE_NAME=site.name,
        # SITE_DOMAIN=site.domain,
        # SITEURL=settings.SITEURL,
        # THEME_ACCOUNT_CONTACT_EMAIL=settings.THEME_ACCOUNT_CONTACT_EMAIL,
        # DEBUG_STATIC=getattr(
        #     settings,
        #     "DEBUG_STATIC",
        #     False),
        # SOCIAL_BUTTONS=getattr(
        #     settings,
        #     'SOCIAL_BUTTONS',
        #     False),
        # THESAURI_FILTERS=[t['name'] for t in settings.THESAURI if t.get('filter')],
    )

    return defaults

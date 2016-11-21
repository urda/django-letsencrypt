"""
Copyright 2016 Peter Urda

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from django.contrib import admin
from django.utils.html import format_html

from .models import AcmeChallenge


class AcmeChallengeAdmin(admin.ModelAdmin):
    """Admin options for the ACME Challenge"""

    def format_acme_url(self, acme_object):
        """Format the ACME url from the ACME challenge object"""
        object_url = acme_object.get_acme_url()

        if object_url:
            return format_html(
                "<a href='{}'>ACME Challenge Link</a>",
                object_url,
            )

        return '-'
    format_acme_url.short_description = 'Link'

    fieldsets = [
        ('ACME Request', {
            'fields': [
                'challenge',
                'response',
            ],
        }),
        ('Metadata', {
            'fields': [
                'id',
                'format_acme_url',
                'created_ts',
                'updated_ts',
            ],
        }),
    ]

    date_hierarchy = 'created_ts'

    list_display = (
        'challenge',
        'format_acme_url',
    )

    list_filter = [
        'created_ts',
        'updated_ts',
    ]

    readonly_fields = [
        'id',
        'created_ts',
        'updated_ts',
        'format_acme_url',
    ]

    search_fields = [
        'challenge',
        'response',
    ]


admin.site.register(AcmeChallenge, AcmeChallengeAdmin)

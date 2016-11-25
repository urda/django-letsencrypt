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


from __future__ import unicode_literals

from django.db import migrations
from django.db.models import Count


def delete_duplicates(apps, schema_editor):
    """
    Find any AcmeChallenge duplicates and delete them

    An AcmeChallenge is considered a duplicate if more than one
    record has the same 'challenge' value as another.
    """

    AcmeChallenge = apps.get_model('letsencrypt', 'AcmeChallenge')
    _ = schema_editor

    dupes = (
        AcmeChallenge.objects
        .values('challenge')
        .annotate(Count('id'))
        .filter(id__count__gt=1)
    )

    for dupe_challenge in [item['challenge'] for item in dupes]:
        dupes_to_delete = (
            AcmeChallenge.objects.filter(challenge=dupe_challenge)[1:]
            .values_list("id", flat=True)
        )

        AcmeChallenge.objects.filter(id__in=dupes_to_delete).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('letsencrypt', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            code=delete_duplicates,
            reverse_code=migrations.RunPython.noop,
        ),
    ]

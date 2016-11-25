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

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('letsencrypt', '0002_remove_challenge_duplicates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acmechallenge',
            name='challenge',
            field=models.TextField(
                unique=True,
                help_text='The identifier for this challenge'
            ),
        ),
    ]

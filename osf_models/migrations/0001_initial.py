# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-27 14:33
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import osf_models.models.base
import osf_models.models.sanctions
import osf_models.models.user
import osf_models.models.validators
import osf_models.utils.base
import osf_models.utils.datetime_aware_jsonfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='OSFUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('fullname', models.CharField(blank=True, max_length=255)),
                ('is_registered', models.BooleanField(db_index=True, default=False)),
                ('is_claimed', models.BooleanField(db_index=True, default=False)),
                ('security_messages', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('is_invited', models.BooleanField(db_index=True, default=False)),
                ('unclaimed_records', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('contributor_added_email_records', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('verification_key', models.CharField(blank=True, max_length=255, null=True)),
                ('emails', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('email_verifications', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('mailing_lists', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('mailchimp_mailing_lists', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('osf_mailing_lists', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default=osf_models.models.user.get_default_mailing_lists)),
                ('date_registered', models.DateTimeField(db_index=True)),
                ('given_name', models.CharField(blank=True, max_length=255)),
                ('middle_names', models.CharField(blank=True, max_length=255)),
                ('family_name', models.CharField(blank=True, max_length=255)),
                ('suffix', models.CharField(blank=True, max_length=255)),
                ('jobs', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('schools', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('social', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('piwik_token', models.CharField(blank=True, max_length=255)),
                ('date_last_login', models.DateTimeField(null=True)),
                ('date_confirmed', models.DateTimeField(db_index=True, null=True)),
                ('date_disabled', models.DateTimeField(db_index=True, null=True)),
                ('comments_viewed_timestamp', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('timezone', models.CharField(default=b'Etc/UTC', max_length=255)),
                ('locale', models.CharField(default=b'en_US', max_length=255)),
                ('requested_deactivation', models.BooleanField(default=False)),
                ('notifications_configured', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AbstractNode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(db_index=True, max_length=255)),
                ('category', models.CharField(choices=[(b'', b'Uncategorized'), (b'communication', b'Communication'), (b'hypothesis', b'Hypothesis'), (b'data', b'Data'), (b'instrumentation', b'Instrumentation'), (b'methods and measures', b'Methods and Measures'), (b'analysis', b'Analysis'), (b'project', b'Project'), (b'other', b'Other'), (b'procedure', b'Procedure'), (b'software', b'Software')], default=b'Uncategorized', max_length=255)),
                ('child_node_subscriptions', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField(db_index=True, null=True)),
                ('deleted_date', models.DateTimeField(null=True)),
                ('description', models.TextField()),
                ('file_guid_to_share_uuids', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('forked_date', models.DateTimeField(db_index=True, null=True)),
                ('is_fork', models.BooleanField(db_index=True, default=False)),
                ('is_public', models.BooleanField(db_index=True, default=False)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('piwik_site_id', models.IntegerField(null=True)),
                ('public_comments', models.BooleanField(default=True)),
                ('suspended', models.BooleanField(db_index=True, default=False)),
                ('title', models.TextField(validators=[osf_models.models.validators.validate_title])),
                ('wiki_pages_current', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('wiki_pages_versions', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('wiki_private_uuids', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('is_registration', models.NullBooleanField(db_index=True, default=False)),
                ('registered_date', models.DateTimeField(db_index=True, null=True)),
                ('registered_meta', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={}, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlackListGuid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField()),
                ('date_modified', models.DateTimeField(db_index=True, null=True)),
                ('is_bookmark_collection', models.BooleanField(db_index=True, default=False)),
                ('title', models.TextField(validators=[osf_models.models.validators.validate_title])),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=False)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osf_models.AbstractNode')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DraftRegistrationApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_state', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('guid', models.CharField(default=osf_models.utils.base.get_object_id, max_length=255)),
                ('initiation_date', models.DateTimeField(null=True)),
                ('state', models.CharField(choices=[(b'unapproved', b'Unapproved'), (b'approved', b'Approved'), (b'rejected', b'Rejected'), (b'completed', b'Completed')], default=b'unapproved', max_length=255)),
                ('meta', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Embargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_state', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('guid', models.CharField(default=osf_models.utils.base.get_object_id, max_length=255)),
                ('initiation_date', models.DateTimeField(null=True)),
                ('state', models.CharField(choices=[(b'unapproved', b'Unapproved'), (b'approved', b'Approved'), (b'rejected', b'Rejected'), (b'completed', b'Completed')], default=b'unapproved', max_length=255)),
                ('notify_initiator_on_complete', models.BooleanField(default=False)),
                ('stashed_urls', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('for_existing_registration', models.BooleanField(default=False)),
                ('initiated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(osf_models.models.sanctions.PreregCallbackMixin, models.Model),
        ),
        migrations.CreateModel(
            name='EmbargoTerminationApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_state', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('guid', models.CharField(default=osf_models.utils.base.get_object_id, max_length=255)),
                ('initiation_date', models.DateTimeField(null=True)),
                ('state', models.CharField(choices=[(b'unapproved', b'Unapproved'), (b'approved', b'Approved'), (b'rejected', b'Rejected'), (b'completed', b'Completed')], default=b'unapproved', max_length=255)),
                ('notify_initiator_on_complete', models.BooleanField(default=False)),
                ('stashed_urls', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guid',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('guid', models.CharField(db_index=True, default=osf_models.models.base.generate_guid, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_url', models.URLField()),
                ('banner_name', models.CharField(max_length=255)),
                ('domains', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), db_index=True, size=None)),
                ('email_domains', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), db_index=True, size=None)),
                ('logo_name', models.CharField(max_length=255)),
                ('logout_url', models.URLField()),
                ('name', models.CharField(max_length=255)),
                ('_guid', models.OneToOneField(default=osf_models.models.base.generate_guid_instance, on_delete=django.db.models.deletion.CASCADE, related_name='referent_institution', to='osf_models.Guid')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstitutionalContributor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read', models.BooleanField(default=False)),
                ('write', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('visible', models.BooleanField(default=False)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osf_models.Institution')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MetaSchema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(db_index=True, default=osf_models.utils.base.get_object_id, max_length=255, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('schema', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('category', models.CharField(max_length=255)),
                ('schema_version', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NodeLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(db_index=True, default=osf_models.utils.base.get_object_id, max_length=255, unique=True)),
                ('date', models.DateTimeField(db_index=True, null=True)),
                ('action', models.CharField(choices=[(b'created_from', b'CREATED_FROM'), (b'project_created', b'PROJECT_CREATED'), (b'project_registered', b'PROJECT_REGISTERED'), (b'project_deleted', b'PROJECT_DELETED'), (b'node_created', b'NODE_CREATED'), (b'node_forked', b'NODE_FORKED'), (b'node_removed', b'NODE_REMOVED'), (b'pointer_created', b'POINTER_CREATED'), (b'pointer_forked', b'POINTER_FORKED'), (b'pointer_removed', b'POINTER_REMOVED'), (b'wiki_updated', b'WIKI_UPDATED'), (b'wiki_deleted', b'WIKI_DELETED'), (b'wiki_renamed', b'WIKI_RENAMED'), (b'made_wiki_public', b'MADE_WIKI_PUBLIC'), (b'made_wiki_private', b'MADE_WIKI_PRIVATE'), (b'contributor_added', b'CONTRIB_ADDED'), (b'contributor_removed', b'CONTRIB_REMOVED'), (b'contributors_reordered', b'CONTRIB_REORDERED'), (b'permissions_updated', b'PERMISSIONS_UPDATED'), (b'made_private', b'MADE_PRIVATE'), (b'made_public', b'MADE_PUBLIC'), (b'tag_added', b'TAG_ADDED'), (b'tag_removed', b'TAG_REMOVED'), (b'edit_title', b'EDITED_TITLE'), (b'edit_description', b'EDITED_DESCRIPTION'), (b'license_changed', b'CHANGED_LICENSE'), (b'updated_fields', b'UPDATED_FIELDS'), (b'addon_file_moved', b'FILE_MOVED'), (b'addon_file_copied', b'FILE_COPIED'), (b'addon_file_renamed', b'FILE_RENAMED'), (b'folder_created', b'FOLDER_CREATED'), (b'file_added', b'FILE_ADDED'), (b'file_updated', b'FILE_UPDATED'), (b'file_removed', b'FILE_REMOVED'), (b'file_restored', b'FILE_RESTORED'), (b'addon_added', b'ADDON_ADDED'), (b'addon_removed', b'ADDON_REMOVED'), (b'comment_added', b'COMMENT_ADDED'), (b'comment_removed', b'COMMENT_REMOVED'), (b'comment_updated', b'COMMENT_UPDATED'), (b'comment_restored', b'COMMENT_RESTORED'), (b'citation_added', b'CITATION_ADDED'), (b'citation_edited', b'CITATION_EDITED'), (b'citation_removed', b'CITATION_REMOVED'), (b'made_contributor_visible', b'MADE_CONTRIBUTOR_VISIBLE'), (b'made_contributor_invisible', b'MADE_CONTRIBUTOR_INVISIBLE'), (b'external_ids_added', b'EXTERNAL_IDS_ADDED'), (b'embargo_approved', b'EMBARGO_APPROVED'), (b'embargo_cancelled', b'EMBARGO_CANCELLED'), (b'embargo_completed', b'EMBARGO_COMPLETED'), (b'embargo_initiated', b'EMBARGO_INITIATED'), (b'retraction_approved', b'RETRACTION_APPROVED'), (b'retraction_cancelled', b'RETRACTION_CANCELLED'), (b'retraction_initiated', b'RETRACTION_INITIATED'), (b'registration_cancelled', b'REGISTRATION_APPROVAL_CANCELLED'), (b'registration_initiated', b'REGISTRATION_APPROVAL_INITIATED'), (b'registration_approved', b'REGISTRATION_APPROVAL_APPROVED'), (b'primary_institution_changed', b'PRIMARY_INSTITUTION_CHANGED'), (b'primary_institution_removed', b'PRIMARY_INSTITUTION_REMOVED')], db_index=True, max_length=255)),
                ('params', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('should_hide', models.BooleanField(default=False)),
                ('foreign_user', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RegistrationApproval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_state', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('guid', models.CharField(default=osf_models.utils.base.get_object_id, max_length=255)),
                ('initiation_date', models.DateTimeField(null=True)),
                ('state', models.CharField(choices=[(b'unapproved', b'Unapproved'), (b'approved', b'Approved'), (b'rejected', b'Rejected'), (b'completed', b'Completed')], default=b'unapproved', max_length=255)),
                ('notify_initiator_on_complete', models.BooleanField(default=False)),
                ('stashed_urls', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('initiated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=(osf_models.models.sanctions.PreregCallbackMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Retraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approval_state', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('end_date', models.DateTimeField(default=None, null=True)),
                ('guid', models.CharField(default=osf_models.utils.base.get_object_id, max_length=255)),
                ('initiation_date', models.DateTimeField(null=True)),
                ('state', models.CharField(choices=[(b'unapproved', b'Unapproved'), (b'approved', b'Approved'), (b'rejected', b'Rejected'), (b'completed', b'Completed')], default=b'unapproved', max_length=255)),
                ('notify_initiator_on_complete', models.BooleanField(default=False)),
                ('stashed_urls', osf_models.utils.datetime_aware_jsonfield.DateTimeAwareJSONField(default={})),
                ('justification', models.CharField(max_length=2048, null=True)),
                ('initiated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(max_length=1024)),
                ('lower', models.CharField(max_length=1024)),
                ('system', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together=set([('_id', 'system')]),
        ),
        migrations.AlterUniqueTogether(
            name='metaschema',
            unique_together=set([('name', 'schema_version', 'guid')]),
        ),
        migrations.AddField(
            model_name='institution',
            name='contributors',
            field=models.ManyToManyField(related_name='institutions', through='osf_models.InstitutionalContributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='collection',
            name='_guid',
            field=models.OneToOneField(default=osf_models.models.base.generate_guid_instance, on_delete=django.db.models.deletion.CASCADE, related_name='referent_collection', to='osf_models.Guid'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='_guid',
            field=models.OneToOneField(default=osf_models.models.base.generate_guid_instance, on_delete=django.db.models.deletion.CASCADE, related_name='referent_abstractnode', to='osf_models.Guid'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='affiliated_institutions',
            field=models.ManyToManyField(related_name='nodes', to='osf_models.Institution'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='contributors',
            field=models.ManyToManyField(related_name='nodes', through='osf_models.Contributor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='embargo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osf_models.Embargo'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='forked_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='forks', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='nodes',
            field=models.ManyToManyField(related_name='_abstractnode_nodes_+', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='parent_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='primary_institution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='primary_nodes', to='osf_models.Institution'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='registered_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registrations', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='registered_schema',
            field=models.ManyToManyField(null=True, to='osf_models.MetaSchema'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='registered_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='registration_approval',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osf_models.RegistrationApproval'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='retraction',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='osf_models.Retraction'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='root',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='absolute_parent', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='system_tags',
            field=models.ManyToManyField(related_name='tagged_by_system', to='osf_models.Tag'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='tags',
            field=models.ManyToManyField(related_name='tagged', to='osf_models.Tag'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='template_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='templated_from', to='osf_models.AbstractNode'),
        ),
        migrations.AddField(
            model_name='abstractnode',
            name='users_watching_node',
            field=models.ManyToManyField(related_name='watching', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='_affiliated_institutions',
            field=models.ManyToManyField(to='osf_models.Institution'),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='_guid',
            field=models.OneToOneField(default=osf_models.models.base.generate_guid_instance, on_delete=django.db.models.deletion.CASCADE, related_name='referent_osfuser', to='osf_models.Guid'),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='merged_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='recently_added',
            field=models.ManyToManyField(related_name='_osfuser_recently_added_+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='system_tags',
            field=models.ManyToManyField(to='osf_models.Tag'),
        ),
        migrations.AddField(
            model_name='osfuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('osf_models.abstractnode',),
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('osf_models.abstractnode',),
        ),
        migrations.AddField(
            model_name='nodelog',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='osf_models.Node'),
        ),
        migrations.AlterUniqueTogether(
            name='institutionalcontributor',
            unique_together=set([('user', 'institution')]),
        ),
        migrations.AddField(
            model_name='embargoterminationapproval',
            name='embargoed_registration',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='osf_models.Node'),
        ),
        migrations.AlterUniqueTogether(
            name='contributor',
            unique_together=set([('user', 'node')]),
        ),
        migrations.AddField(
            model_name='collection',
            name='nodes',
            field=models.ManyToManyField(related_name='children', to='osf_models.Node'),
        ),
    ]

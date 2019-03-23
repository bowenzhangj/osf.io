# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-26 15:18
from __future__ import unicode_literals
from math import ceil
import logging

from django.db import migrations, connection

logger = logging.getLogger(__name__)

increment = 500000

def remove_records_from_files(state, schema):
    FileMetadataRecord = state.get_model('osf', 'filemetadatarecord')
    FileMetadataRecord.objects.all().delete()

# Batching adapted from strategy in website/search_migration/migrate.py
def add_records_to_files_sql(state, schema):
    FileMetadataSchema = state.get_model('osf', 'filemetadataschema')
    datacite_schema_id = FileMetadataSchema.objects.filter(_id='datacite').values_list('id', flat=True)[0]
    OsfStorageFile = state.get_model('osf', 'osfstoragefile')
    max_fid = getattr(OsfStorageFile.objects.last(), 'id', 0)

    sql = """
        INSERT INTO osf_filemetadatarecord (created, modified, _id, metadata, file_id, schema_id)
        SELECT NOW(), NOW(), generate_object_id(), '{{}}', OSF_FILE.id, %d
            FROM osf_basefilenode OSF_FILE
                WHERE (OSF_FILE.type = 'osf.osfstoragefile'
                       AND OSF_FILE.provider = 'osfstorage'
                       AND OSF_FILE.id > {}
                       AND OSF_FILE.id <= {}
                );
    """ % (datacite_schema_id)

    total_pages = int(ceil(max_fid / float(increment)))
    page_start = 0
    page_end = 0
    page = 0
    while page_end <= (max_fid):
        page += 1
        page_end += increment
        if page <= total_pages:
            logger.info('Updating page {} / {}'.format(page_end / increment, total_pages))
        with connection.cursor() as cursor:
            cursor.execute(sql.format(
                page_start,
                page_end
            ))
        page_start = page_end

class Migration(migrations.Migration):

    dependencies = [
        ('osf', '0136_add_datacite_file_metadata_schema'),
    ]

    operations = [
        migrations.RunPython(add_records_to_files_sql, remove_records_from_files),
    ]
# Generated by Django 2.1.5 on 2019-01-25 23:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.PositiveSmallIntegerField(null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('created_at', models.DateTimeField(null=True)),
                ('source', models.CharField(max_length=700, null=True)),
                ('notebook', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notebook.NoteBook')),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
                'db_table': 'articles',
            },
        ),
    ]
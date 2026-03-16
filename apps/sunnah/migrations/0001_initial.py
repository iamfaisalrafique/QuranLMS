from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HadithCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('collection_id', models.IntegerField(blank=True, null=True)),
                ('english_title', models.CharField(max_length=255)),
                ('arabic_title', models.CharField(max_length=255)),
                ('short_intro', models.TextField(blank=True)),
                ('about', models.TextField(blank=True)),
                ('num_hadith', models.IntegerField(default=0)),
                ('total_hadith', models.IntegerField(default=0)),
                ('has_books', models.BooleanField(default=True)),
                ('has_chapters', models.BooleanField(default=True)),
                ('status', models.CharField(default='complete', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='HadithBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_number', models.IntegerField(db_index=True)),
                ('english_title', models.CharField(max_length=255)),
                ('arabic_title', models.CharField(max_length=255)),
                ('english_intro', models.TextField(blank=True)),
                ('arabic_intro', models.TextField(blank=True)),
                ('first_number', models.IntegerField(blank=True, null=True)),
                ('last_number', models.IntegerField(blank=True, null=True)),
                ('total_number', models.IntegerField(default=0)),
                ('status', models.CharField(default='complete', max_length=50)),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='sunnah.hadithcollection')),
            ],
            options={
                'unique_together': {('collection', 'book_number')},
            },
        ),
        migrations.CreateModel(
            name='HadithChapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_number', models.CharField(max_length=20)),
                ('english_title', models.CharField(max_length=500)),
                ('arabic_title', models.CharField(max_length=500)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chapters', to='sunnah.hadithbook')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sunnah.hadithcollection')),
            ],
        ),
        migrations.CreateModel(
            name='Hadith',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hadith_number', models.CharField(db_index=True, max_length=20)),
                ('source_id', models.IntegerField(db_index=True)),
                ('arabic_body', models.TextField()),
                ('english_body', models.TextField()),
                ('narrator', models.TextField(blank=True)),
                ('grade', models.CharField(blank=True, max_length=255)),
                ('reference', models.CharField(blank=True, max_length=255)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hadiths', to='sunnah.hadithbook')),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hadiths', to='sunnah.hadithchapter')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hadiths', to='sunnah.hadithcollection')),
            ],
            options={
                'ordering': ['collection', 'source_id'],
                'unique_together': {('collection', 'source_id')},
            },
        ),
    ]

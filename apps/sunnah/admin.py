from django.contrib import admin
from .models import HadithCollection, HadithBook, HadithChapter, Hadith

@admin.register(HadithCollection)
class HadithCollectionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'english_title', 'arabic_title', 'num_hadith')
    search_fields = ('slug', 'english_title', 'arabic_title')

@admin.register(HadithBook)
class HadithBookAdmin(admin.ModelAdmin):
    list_display = ('collection', 'book_number', 'english_title')
    list_filter = ('collection',)
    search_fields = ('english_title', 'book_number')

@admin.register(HadithChapter)
class HadithChapterAdmin(admin.ModelAdmin):
    list_display = ('book', 'chapter_number', 'english_title')
    list_filter = ('collection', 'book')
    search_fields = ('english_title', 'chapter_number')

@admin.register(Hadith)
class HadithAdmin(admin.ModelAdmin):
    list_display = ('hadith_number', 'collection', 'book', 'grade', 'source_id')
    list_filter = ('collection', 'grade')
    search_fields = ('arabic_body', 'english_body', 'hadith_number', 'source_id')

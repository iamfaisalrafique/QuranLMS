from rest_framework import serializers
from .models import HadithCollection, HadithBook, HadithChapter, Hadith

class HadithCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HadithCollection
        fields = ['slug', 'english_title', 'arabic_title', 'short_intro', 'num_hadith', 'status']

class HadithBookSerializer(serializers.ModelSerializer):
    collection_slug = serializers.ReadOnlyField(source='collection.slug')

    class Meta:
        model = HadithBook
        fields = ['book_number', 'english_title', 'arabic_title', 'total_number', 'collection_slug']

class HadithChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HadithChapter
        fields = ['chapter_number', 'english_title', 'arabic_title']

class HadithSerializer(serializers.ModelSerializer):
    book_number = serializers.ReadOnlyField(source='book.book_number')
    chapter = HadithChapterSerializer(read_only=True)
    
    class Meta:
        model = Hadith
        fields = [
            'id', 'hadith_number', 'arabic_body', 'english_body',
            'narrator', 'grade', 'reference', 'book_number', 'chapter'
        ]

class HadithSearchSerializer(serializers.ModelSerializer):
    collection_slug = serializers.ReadOnlyField(source='collection.slug')
    collection_title = serializers.ReadOnlyField(source='collection.english_title')
    book_number = serializers.ReadOnlyField(source='book.book_number')
    book_title = serializers.ReadOnlyField(source='book.english_title')

    class Meta:
        model = Hadith
        fields = [
            'id', 'hadith_number', 'english_body', 'arabic_body',
            'grade', 'collection_slug', 'collection_title',
            'book_number', 'book_title'
        ]

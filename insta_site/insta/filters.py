from django_filters import FilterSet
from insta_site.insta.models import Post


class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
            'hashtag': ['exact']
        }


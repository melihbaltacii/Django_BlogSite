from django.contrib import admin

# Register your models here.
from post.models import Posts

# Create your views here.



class PostAdmin(admin.ModelAdmin):
    list_display=["title",'publishDate']
    list_display_links=['publishDate']
    list_filter = ["publishDate"]
    search_fields=["title","content"]
    list_editable=["title"]

    class Meta:
        model=Posts

admin.site.register(Posts ,PostAdmin)
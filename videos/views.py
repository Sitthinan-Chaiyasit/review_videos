from django.shortcuts import render, get_object_or_404
from .models import Video

def home(request):
    featured = Video.objects.filter(is_featured=True)
    videos = Video.objects.all()
    categories = Video.CATEGORY_CHOICES
    
    category_filter = request.GET.get('category', '')
    if category_filter:
        videos = videos.filter(category=category_filter)
    
    context = {
        'featured': featured,
        'videos': videos,
        'categories': categories,
        'current_category': category_filter,
    }
    return render(request, 'videos/home.html', context)

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    related = Video.objects.exclude(pk=pk).filter(category=video.category)[:3]
    embed_url = None
    if video.youtube_url:
        url = video.youtube_url
        if 'watch?v=' in url:
            embed_url = url.replace('watch?v=', 'embed/')
        elif 'youtu.be/' in url:
            embed_url = url.replace('youtu.be/', 'www.youtube.com/embed/')
        else:
            embed_url = url

    return render(request, 'videos/detail.html', {
        'video': video,
        'related': related,
        'embed_url': embed_url,
    })
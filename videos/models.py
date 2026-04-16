from django.db import models

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('wedding', 'Typography Style'),
        ('event', 'Motion Graphics Style'),
        ('commercial', 'Daddy Style'),
        ('documentary', 'Candy Style'),
        ('music', 'VFX Style'),
        ('other', 'Others'),
    ]

    title = models.CharField(max_length=200, verbose_name='ชื่อวิดีโอ')
    description = models.TextField(blank=True, verbose_name='คำอธิบาย')
    category = models.CharField(
        max_length=20, 
        choices=CATEGORY_CHOICES, 
        default='other',
        verbose_name='หมวดหมู่'
    )
    thumbnail = models.ImageField(
        upload_to='thumbnails/', 
        blank=True, null=True,
        verbose_name='ภาพปก'
    )
    video_file = models.FileField(
        upload_to='videos/', 
        blank=True, null=True,
        verbose_name='ไฟล์วิดีโอ'
    )
    youtube_url = models.URLField(
        blank=True, 
        verbose_name='ลิงก์ YouTube (ถ้ามี)'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name='แนะนำ')
    order = models.IntegerField(default=0, verbose_name='ลำดับ')

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = 'วิดีโอ'
        verbose_name_plural = 'วิดีโอทั้งหมด'

    def __str__(self):
        return self.title
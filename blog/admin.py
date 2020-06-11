'''
코드에서 알 수 있듯이 앞 장에서 정의했던 Post모델을 가져오고(import) 있어요.
관리자 페이지에서 만든 모델을 보려면 
admin.site.register(Post)로 모델을 등록해야 해요.
'''
from django.contrib import admin
from .models import Post

admin.site.register(Post)
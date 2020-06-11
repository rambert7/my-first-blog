'''
from 또는 import로 시작하는 부분은 
다른 파일에 있는 것을 추가하라는 뜻
다시 말해, 매번 다른 파일에 있는 것을 복사&붙여넣기로 해야 하는 작업을 from이 대신 불러와 줌

class Post(models.Model):는 모델을 정의하는 코드
모델은 객체(object)

class는 특별한 키워드로, 객체를 정의한다는 것을 알려줍니다.
Post는 모델의 이름입니다. (특수문자와 공백 제외한다면) 다른 이름을 붙일 수도 있습니다. 
항상 클래스 이름의 첫 글자는 대문자로 써야 합니다.

models은 Post가 장고 모델임을 의미
이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 됩니다.

이제 속성을 정의하는 것에 대해서 이야기해 볼게요. 
title, text, created_date, published_date, author에 대해서 말할 거에요. 
속성을 정의하기 위해, 필드마다 어떤 종류의 데이터 타입을 가지는지를 정해야 해요. 
여기서 데이터 타입에는 텍스트, 숫자, 날짜, 사용자 같은 다른 객체 참조 등이 있습니다.

models.CharField - 글자 수가 제한된 텍스트를 정의할 때 사용합니다. 
                   글 제목같이 짧은 문자열 정보를 저장할 때 사용합니다.
models.TextField - 글자 수에 제한이 없는 긴 텍스트를 위한 속성입니다. 
                   블로그 콘텐츠를 담기 좋겠죠?
models.DateTimeField - 날짜와 시간을 의미합니다.
models.ForeignKey - 다른 모델에 대한 링크를 의미합니다

 모델의 필드와 정의하는 방법
 https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types
 
 def publish(self):는 무슨 뜻일까요? 
 이것이 바로 앞서 말했던 publish라는 메서드(method) 입니다. 
 def는 이것이 함수/메서드라는 뜻이고, publish는 메서드의 이름입니다. 
 원한다면 메서드 이름을 변경할 수도 있어요. 
 이름을 붙일 때는 공백 대신, 소문자와 언더스코어를 사용해야 합니다. 
 예를 들어, 평균 가격을 계산하는 메서드는 
 calculate_average_price라고 부를 수 있겠네요.

메서드는 자주 무언가를 되돌려주죠. (return) 
그 예로 __str__ 메서드를 봅시다. 
이 시나리오대로라면, __str__를 호출하면 
Post 모델의 제목 텍스트(string)를 얻게 될 거에요.

아직 모델에 대해서 잘 모르는 부분이 있다면, 
코치에게 자유롭게 물어보세요! 
지금 배운 내용이 너무 복잡하게 느껴질 수 있어요. 
객체와 함수를 배운 적이 없는 분들이 한꺼번에 배우게 된다면 
특히 그렇겠죠. 그래도 해 볼 만한 마법이라고 생각했으면 좋겠어요!
'''
from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
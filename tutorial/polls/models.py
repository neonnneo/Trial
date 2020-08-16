"""モデル

     * ソースコードの一番始めに記載すること
     * importより前に記載する

Todo:
   TODOリストを記載
    * TODOがあればココに書く
    * TODOがあればココに書く

"""
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)

    #question_text = 'どっちを選ぶ？'
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 日付が過去の場合のみTrueを返すこと
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    #choice_text = 'a''i'
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

"""管理者用のモジュール

     * ソースコードの一番始めに記載すること
     * importより前に記載する

History:
   更新日   更新者  更新内容
   2020/08/16   neonnneo    新規作成

"""

from django.contrib import admin
from .models import Choice, Question, Log
# ログクラスの宣言
log = Log()


class ChoiceInline(admin.TabularInline):
    """
     チュートリアルで作成したサンプルクラス

    """

    model = Choice
    extra = 0

# class ChoiceInline(admin.StackedInline):


class QuestionAdmin(admin.ModelAdmin):
    """
     チュートリアルで作成したサンプルクラス

    """

    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


log.logging('info', 'hogehoge')
admin.site.register(Question, QuestionAdmin)

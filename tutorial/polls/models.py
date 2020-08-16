"""モデル宣言用のモジュール

     * ソースコードの一番始めに記載すること
     * importより前に記載する

History:
   更新日   更新者  更新内容
   2020/08/16   neonnneo    Class Logとlogging関数を追加

"""
import datetime


from django.db import models
from django.utils import timezone

# Logging絡みのImportなど
import logging

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


class Log(models.Model):

    # class Command(BaseCommand):
    """
     ログ出力処理用クラス

    """

    # python manage.py help count_entryで表示されるメッセージ
    help = 'Display the number of blog articles'

    def logging(self, level, message):
        """ログ出力

            ログ出力時に呼び出すクラス

        Args:
            self：
            level （文字列）: ログレベル
            message （文字列）: ログ出力するメッセージ

        Note:
            1.pyファイルで最初にimport loggingする
            2.settings.pyのLOGGING設定(以下debug設定)を取得
                logger = logging.getLogger('debug')
            3.メッセージを出力する。
                logger.debug(message)

            4.エラーメッセージの場合
                self.logging('debug', 'no positions, no orders')

        """
        if level == 'debug':
            logger = logging.getLogger('debug')
            logger.debug(message)
        elif level == 'info':
            logger = logging.getLogger('info')
            logger.info(message)
        else:
            logger = logging.getLogger('error')
            logger.error(message)

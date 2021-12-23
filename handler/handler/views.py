import psycopg2
from io import BytesIO
from django.http.response import HttpResponse
from django.utils.timezone import datetime
from passlib.handlers.django import django_pbkdf2_sha256
from django.views.decorators.csrf import csrf_exempt

from base64 import b64encode as enc64 
from base64 import b64decode as dec64 
from PIL import Image

def telegramPassword(request):
    try: 
        conn = psycopg2.connect(dbname='hello_django_dev', user='hello_django', 
                        password='hello_django', host='db', port = '5432')
    except:
        return HttpResponse(False)
    
    cursor = conn.cursor()
    if request.method == "GET":
        sql = "SELECT password, id FROM userprofile_user WHERE username = '%s'" % request.GET['username']
        cursor.execute(sql)

        try: 
            password, id = cursor.fetchone()
        except:
            return HttpResponse(False)

        is_verified = django_pbkdf2_sha256.verify(request.GET['password'],password)

        if(is_verified):
            sql = """
                INSERT INTO userprofile_telegram(telegram_id, user_id)
                VALUES(%s, %s)
            """ % (request.GET['id'], id)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            return HttpResponse(True)

    return HttpResponse(False)

@csrf_exempt
def addNews(request):
        conn =  psycopg2.connect(dbname='hello_django_dev', user='hello_django', 
                    password='hello_django', host='db', port = '5432')


        cursor = conn.cursor()

        title = request.POST.get("title")
        small_text = request.POST.get("small_text")
        text = request.POST.get("text")
        date_pub = datetime.now()
        image_id = request.POST.get("image_id") + '.jpg'

        image = BytesIO(dec64(request.POST.get("image")))
        pillow = Image.open(image)
        pillow.save(f'media/{image_id}')

        image = 'default.jpg'


        header_image = 'default.jpg'
        message_count = 0
        in_header = False

        cursor.execute("SELECT user_id FROM userprofile_telegram WHERE telegram_id = %s" % request.POST.get("id"))
        
        author_id = cursor.fetchall()[0][0]

        news = (title, small_text, text, date_pub, image_id, header_image, author_id, message_count, in_header)
        sql = """
            INSERT INTO news_news(title, small_text, text, date_pub, image, header_image, author_id, message_count, in_header) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        cursor.execute(sql, news)
        conn.commit()
        return HttpResponse(True)
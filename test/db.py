import pika, sys, os
import sqlite3
import datetime
def main():
    conn = sqlite3.connect(r'./django project/db.sqlite3')
    cursor = conn.cursor()

    title = "Test"
    small_text = "Test"
    text = "Test"
    date_pub = datetime.datetime.today() 
    image = '1.jpg'
    header_image = '1.jpg'
    author_id = '1'
    message_count = 0
    in_header = 0
    news = (title, small_text, text, date_pub, image, header_image, author_id, message_count, in_header)

    sql = """
    INSERT INTO news_news(title, small_text, text, date_pub, image, header_image, author_id, message_count, in_header) 
   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
   """
    cursor.execute(sql, news)
    conn.commit()

    print(cursor.fetchall())


if __name__ == '__main__':
    main()
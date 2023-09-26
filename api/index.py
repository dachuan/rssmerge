from flask import Flask, Response
import feedparser
from feedgen.feed import FeedGenerator

app = Flask(__name__)

@app.route('/')
def merge_rss():
    # 创建一个新的RSS源
    fg = FeedGenerator()
    fg.title('合并的RSS源')
    fg.link(href='https://rssmerge-bhsnd63v9-dachuan.vercel.app/api', rel='alternate')
    fg.description('这是合并的RSS源')

    # 添加多个RSS源
    rss_urls = ['https://utgd.net/feed',  'https://blog.jimmylv.info/pages/atom.xml']
    for rss_url in rss_urls:
        feed = feedparser.parse(rss_url)
        for entry in feed.entries:
            fe = fg.add_entry()
            fe.title(entry.title)
            fe.link(href=entry.link)
            fe.description(entry.summary)

    # 生成合并后的RSS字符串
    rss_str = fg.rss_str(pretty=True)

    # 返回RSS内容
    return Response(rss_str, content_type='application/rss+xml')

#if __name__ == '__main__':
#    app.run()

from flask import Flask, Response
import feedparser
from feedgen.feed import FeedGenerator

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello"

@app.route('/feed')
def merge_rss():
    # 创建一个新的RSS源
    fg = FeedGenerator()
    fg.title('合并的RSS源')
    fg.link(href='https://rssmerge.vercel.app', rel='alternate')
    fg.description('这是合并的RSS源')

    # 添加多个RSS源
    rss_urls = [
            "https://utgd.net/feed",
            "https://rsshub.app/marginnote/tag/%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB",
            "https://blog.jimmylv.info/pages/atom.xml",
            "https://iseex.github.io/feed.xml",
            "http://www.ruanyifeng.com/blog/atom.xml",
            "http://sspai.com/feed",
            "https://www.appinn.com/feed",
            "http://research.sinica.edu.tw/feed",
            "https://yuyencia.org/feed/",
            "https://hnrss.org/newest?points=100",
            "https://inessential.com/feed.json",
            "http://free.apprcn.com/category/ios/feed/",
            "http://www.matrix67.com/blog/feed",
            "http://www.mooc.cn/feed",
            "https://type.cyhsu.xyz/feed/",
            "https://forum-zh.obsidian.md/u/boninall/activity/topics.rss",
            "https://troynikov.io/rss/",
            "https://rosemaryorchard.com/blog/feed/",
            "https://www.sapiens.org/feed/",
            "https://www.scotthyoung.com/blog/feed/",
            "https://shyrz.me/rss/",
            "https://shapeof.com/feed.json",
            "https://www.youtube.com/feeds/videos.xml?channel_id=UCC0gns4a9fhVkGkngvSumAQ",
            ]
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

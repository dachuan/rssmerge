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
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/aliyisheng?code=ee98b264d5c3272d2bf137aaefbf006a",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/piao-shi-yu",
            "https://rsshub.app/marginnote/tag/%E7%BB%8F%E9%AA%8C%E5%88%86%E4%BA%AB",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/37badb617c1845a82c3e22bc612dac55",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/LBQYJS",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/lijianhui.net",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/li-lei-34-16",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/lin-xiao-63-71",
            "https://rsshhhub-dachuan.vercel.app/bilibili/user/dynamic/37648256",
            "https://blog.jimmylv.info/pages/atom.xml",
            "https://iseex.github.io/feed.xml",
            "http://www.ruanyifeng.com/blog/atom.xml",
            "http://sspai.com/feed",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/yu-chen-tian-2",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/mo-lu-wei-ma",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/tan-jun-jiang",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/taoshu0",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/wan-dao-zhu",
            "https://rsshhhub-dachuan.vercel.app/bilibili/user/dynamic/314022607",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/mi-mi-37-98",
            "https://rsshhhub-dachuan.vercel.app/bilibili/user/dynamic/17197484?code=fd04a0261d3a5741193eca85417d624f",
            "https://www.appinn.com/feed",
            "http://research.sinica.edu.tw/feed",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/yin-you-shi-ren-ji-de",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/handanxie",
            "https://yuyencia.org/feed/",
            "https://rsshhhub-dachuan.vercel.app/bilibili/user/dynamic/228924385",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/yuzhoutianwenguan",
            "https://rsshhhub-dachuan.vercel.app/zhihu/question/432830135?code=bfe2c69accc6edf672ef0152bddef6a1",
            "https://rsshhhub-dachuan.vercel.app/zhihu/zhuanlan/c_1122815481962270720?code=abf85d1b6815fb64634bbf653971b27e",
            "https://rsshhhub-dachuan.vercel.app/zhihu/zhuanlan/digitalnomad",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/df87c128d6f437eea9e6e97bba2e7496",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/zfish",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/dhunterb",
            "https://hnrss.org/newest?points=100",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/haibaraemily",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/xueweihan",
            "https://inessential.com/feed.json",
            "http://free.apprcn.com/category/ios/feed/",
            "https://rsshhhub-dachuan.vercel.app/bilibili/user/dynamic/432408734",
            "http://www.matrix67.com/blog/feed",
            "http://www.mooc.cn/feed",
            "https://type.cyhsu.xyz/feed/",
            "https://rsshub-9g2bv8piab12b614-1258242446.ap-shanghai.app.tcloudbase.com/bilibili/user/dynamic/677015432?code=1dd8eb1cc47d3eadc1a003a36663e271",
            "https://forum-zh.obsidian.md/u/boninall/activity/topics.rss",
            "https://troynikov.io/rss/",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/phodal",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/man-burton",
            "https://rosemaryorchard.com/blog/feed/",
            "https://www.sapiens.org/feed/",
            "https://www.scotthyoung.com/blog/feed/",
            "https://shyrz.me/rss/",
            "https://shapeof.com/feed.json",
            "https://rsshhhub-dachuan.vercel.app/zhihu/people/activities/garrett-wyatt",
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

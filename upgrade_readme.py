import feedparser

khyojun_blog_rss_url="https://v2.velog.io/rss/nandong1104"
rss_feed=feedparser.parse(khyojun_blog_rss_url)


MAX_POST_NUM = 10

latest_blog_post_list = ""


for idx, feed in enumerate(rss_feed['entries']):
    if idx> MAX_POST_NUM:
        break
    feed_date = feed['published_parsed']
    latest_blog_post_list +=f"<ul><li>[{feed_date.tm_year}/{feed_date.tm_mon}/{feed_date.tm_mday} - {feed['title']}]({feed['link']}) </ul><br>\n"

markdown_text = """
# ✋ HELLO ✋ 

### 📧 Contact Email : nandong5923@naver.com
### 🔍 Study & Daily Blog : https://velog.io/@nandong1104
[![github stats](https://github-readme-stats.vercel.app/api?username=khyojun&show_icons=true&hide_border=False)](https://velog.io/@nandong1104)
[![Velog's GitHub stats](https://velog-readme-stats.vercel.app/api?name=velopert)](https://github.com/eungyeole/velog-readme-stats)


"""

readme_text=f"{markdown_text}{latest_blog_post_list}"

with open("README.md", "w", encoding='utf-8') as f:
    f.write(readme_text)


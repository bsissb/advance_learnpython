# coding:utf-8
import urllib, re

#remod = re.compile(ur'<div class="info "><a href="/video/(?P<av>.+?)/" target="_blank"><div class="title">(?P<title>.+?)</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>(?P<click>.+?)</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>(?P<review>.+?)</span><a href="//space.bilibili.com/\d*" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>(?P<upname>.+?)</span></a></div><div class="pts" title="[\u4e00-\u9fa5]+"><div>(?P<grade>.+?)</div>[\u4e00-\u9fa5]+</div></div>')
remod = re.compile(r'\t<tr>\n\t\t<td nowrap>(?P<class>.+?)</td>\n\t\t<td nowrap><h3><a href="(?P<url>.+?)" target="_blank">(?P<title>.+?)</a></h3></td>\n\t\t<td nowrap>(?P<click>.+?)</td>\n\t\t<td nowrap>(?P<datetime>.+?)</td>\n\t\t<td nowrap><a href="(?P<reviewurl>.+?)" target="_blank">发表评论</a></td>\n\t</tr>')

bilibiliranking = urllib.urlopen(r"http://news.ifeng.com/hotnews/").read()

resultiter = remod.finditer(bilibiliranking)

rankinglist = []
for m in resultiter:
    rankinglist.append(m.groupdict())

print rankinglist[0]["title"].decode('utf-8').encode('utf-8')   #终于学会了如何显示中文……
'''
<div class="info "><a href="/video/av9135074/" target="_blank"><div class="title">【贝尔】荒野求生系列（720P超清）（国语版全网最齐）更新至57集</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>27.0万</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>1.0万</span><a href="//space.bilibili.com/43837937" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>A6驾照</span></a></div><div class="pts" title="综合评分"><div>1179503</div>综合评分</div></div>
<div class="info "><a href="/video/av9147506/" target="_blank"><div class="title">爱情公寓op动漫版</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>18.8万</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>841</span><a href="//space.bilibili.com/1939319" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>科学超电磁炮F</span></a></div><div class="pts" title="综合评分"><div>416569</div>综合评分</div></div>
<div class="info "><a href="/video/(?P<av>.+?)/" target="_blank"><div class="title">(?P<title>.+?)</div></a><div class="detail"><span class="data-box play"><i class="b-icon b-icon-v-play"></i>(?P<click>.+?)</span><span class="data-box dm"><i class="b-icon b-icon-v-dm"></i>(?P<review>.+?)</span><a href="//space.bilibili.com/\d*" target="_blank"><span class="data-box author"><i class="b-icon b-icon-v-author"></i>(?P<upname>.+?)</span></a></div><div class="pts" title="综合评分"><div>(?P<grade>.+?)</div>综合评分</div></div>
抓取大失败，似乎b站不能这样简单抓取（动态网页？不懂
'''

'''
<tr>\n\t\t<td nowrap="">(?P<class>.+?)</td>
\t\t<td nowrap=""><h3><a href="(?P<url>.+?)" target="_blank">(?P<title>.+?</a></h3></td>
\t\t<td nowrap="">(?P<click>.+?)</td>
\t\t<td nowrap="">(?P<datetime>.+?)</td>
\t\t<td nowrap=""><a href="(?P<review_url>.+?)" target="_blank">发表评论</a></td>
\t</tr>
'''

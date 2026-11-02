---
title: 연대표
part: 4
order: 1
authors: [편찬위원회]
tags: [연대표]
---

# 연대표

이우교육공동체 20년의 주요 사건을 연·월(·일) 단위로 정리했습니다. 각 사건 링크는 관련 본문(Part 1/2)으로 연결됩니다.

<div class="ew-timeline" markdown>
{% for year, rows in timeline | groupby("year") %}
## {{ year }}년 { #y{{ year }} }
{% for row in rows %}
### {% if row.month %}{{ row.month }}월{% if row.day %} {{ row.day }}일{% endif %}{% else %}{{ row.year }}년 중{% endif %} { #{{ row.anchor }} }

{{ row.event }}
{% if row.related_essays -%}
관련 글:
{% for essay in row.related_essays %}- [{{ essay }}]({{ essay }})
{% endfor %}
{%- endif %}
{% endfor %}
{% endfor %}
</div>

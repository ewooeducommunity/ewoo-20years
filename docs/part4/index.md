---
title: 연대표
part: 4
order: 1
authors: [편찬위원회]
tags: [연대표]
---

# 연대표

{% for row in timeline %}
## <span id="{{ row.anchor }}">{{ row.year }}년{% if row.month %} {{ row.month }}월{% endif %}</span> — {{ row.event }}
{% if row.related_essays -%}
관련 글:
{% for essay in row.related_essays %}- [{{ essay }}]({{ essay }})
{% endfor %}
{%- endif %}
{% endfor %}

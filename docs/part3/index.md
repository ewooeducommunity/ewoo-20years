---
title: 역대 임원진
part: 3
order: 1
authors: [편찬위원회]
tags: [임원진, 색인]
---

# 역대 임원진

| 재임 | 직책 | 성명 |
| --- | --- | --- |
{% for row in executives -%}
| {{ row.period }} | {{ row.role }} | <span id="{{ row.anchor }}">{{ row.name }}</span> |
{% endfor %}

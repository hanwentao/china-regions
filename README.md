# 中国行政区划数据

本项目将民政部公布的中国行政区划数据结构化，可作为地点控件的参考数据。

## 数据来源

原始数据来自于[2020年5月中华人民共和国县以上行政区划代码](http://www.mca.gov.cn/article/sj/xzqh/2020/2020/2020072805001.html)。获取方法：

    curl -s http://www.mca.gov.cn/article/sj/xzqh/2020/2020/2020072805001.html | html2text --ignore-tables >data/places.txt

这里用到了 [html2text](http://alir3z4.github.io/html2text/) 工具。或者，也可以用浏览器访问[该网页](http://www.mca.gov.cn/article/sj/xzqh/2020/2020/2020072805001.html)，然后把文字内容复制粘贴到 `data/places.txt` 文件中。

## 数据文件

* `data/regions.json`：JSON 格式的中国县以上行政区划数据，本身是一个数组，元素为省级行政区划，元素字段包括
  + `code`：行政区划的 6 位数字代码
  + `name`：行政区划的名称
  + `subregions`（可选）：下级行政区划数据，格式同上
* `data/locations.csv`：CSV 格式的中国县以上行政区划数据，包含三个字段
  + `code`：行政区划的 6 位数字代码
  + `name`：行政区划的名称
  + `full_name`：行政区划的全称，一般包含省、地、县三部分
* `data/locations.txt`：纯文本格式，每行包括一条中国县以上行政区划的全称，包括县以上的下级行政区划的行政区划不列出。

## 处理脚本

* `generate_regions.py`：从 `data/places.txt` 产生 `data/regions.json` 的 Python 脚本
* `parse_places.py`：从 `data/places.txt` 产生 `data/locations.csv` 的 Python 脚本
* `dump_locations.py`：从 `data/regions.json` 产生 `data/locations.txt` 的 Python 脚本

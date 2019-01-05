#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 16:42
# @Author  : Qinyong
# @Site    :
# @File    : urldata.py

import bs4
import requests
import re
import openpyxl


def open_url(url):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"}
	res = requests.get(url, headers=headers)
	return res


def find_data(res):
	data = []
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	content = soup.find(id="Cnt-Main-Article-QQ")
	print(content)
	target = content.find_all("p", style="TEXT-INDENT: 2em")
	target = iter(target)
	for each in target:
		print(each)
		if each.text.isnumeric():
			data.append([
				re.search(r'\[(.+)\]', next(target).text).group(1),
				re.search(r'\d.*', next(target).text).group(),
				re.search(r'\d.*', next(target).text).group(),
				re.search(r'\d.*', next(target).text).group()])
	return data


def to_excl(data):
	wb = openpyxl.Workbook()
	wb.guess_types = True
	ws = wb.active
	ws.append(['城市', '平均房价', '工资', '房价工资比'])
	for each in data:
		print(each)
		ws.append(each)
	wb.save("qqqqq.xlsx")


def main():
	url = "https://news.house.qq.com/a/20170702/003985.htm"
	res = open_url(url)
	data = find_data(res)
	to_excl(data)


if __name__ == "__main__":
	main()

# coding:utf-8
# 3-2 如何实现可迭代对象和迭代器对象（2）

import requests


def getWeather(city):
	r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
	data = r.json()['data']['forecast'][0]
	return '%s:%s,%s' % (city, data['low'], data['high'])


# print(getWeather('北京'))
# print(getWeather('长春'))

from collections import Iterable, Iterator


# print(Iterator.__abstractmethods__)
# print(Iterable.__abstractmethods__)

class WeatherIterator(Iterator):
	'''
	迭代器对象
	'''
	def __init__(self, cities):
		self.cities = cities  # 城市列表
		self.index = 0

	def __next__(self):
		if self.index == len(self.cities):
			raise StopIteration
		city = self.cities[self.index]
		self.index += 1
		return self.getWeather(city)

	def getWeather(self, city):
		r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=' + city)
		data = r.json()['data']['forecast'][0]
		return '%s:%s,%s' % (city, data['low'], data['high'])

class WeatherIterable(Iterable):
	def __init__(self,cities):
		self.cities=cities
	def __iter__(self):
		return WeatherIterator(self.cities)


for x in  WeatherIterable(['北京','上海','广州','长春']):
	print(x)
'''从 Github 上分别拉取五门热门语言的 star 数前三十的项目. 以 svg 图片格式展示出来.

'''
import requests
from pygal import Bar
from pygal import Config

languages = ['Java', 'Python', 'C', 'Ruby', 'JavaScript', 'PHP']

def add_data_to_bar(language, chart):
	'''get data from github and add it to chart
	'''
	''' language: special language to search
		chart : pygal.Bar object
	'''
	names = []
	stars = []
	url ='https://api.github.com/search/repositories?q=language:' + language +'&sort=stars'

	response_dict = requests.get(url).json()
	items_list = response_dict['items']

	for item in items_list:
		names.append(item['name'])
		stars.append(item['stargazers_count'])
		
	chart.add(language, stars)
	
	
def init_bar_graph():
	config = Config()
	config.x_label_rotation = 45
	config.show_legend = True
	config.title = 'Most-Starred Top-5 Programming Languages\'s Projects on Github'
	config.y_title = 'Stars'
	chart = Bar(config)
	
	return chart

#Entrypoint
if __name__ == '__main__':
	chart = init_bar_graph()
	for language in languages:
		add_data_to_bar(language, chart)

	chart.render_to_file('repos_star.svg')






try:
	from setuptools	import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description':'ex46'
	'author':'zhou'
	'url':'URL to get it at'
	'download_url':'Where to download it'
	'author_email':'mmix1009@163.com'
	'version':'0.1',
	'install_requires':['nose']	
	'packages':['skeleton'],
	'scripts':[],
	'name':'projectname'
}

setup(**config)
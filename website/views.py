from django.shortcuts import render
import requests
import json


def index(request):

	headers = {
		'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
		'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	}

	# get random recipe
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

	querystring = { "number": "6"} # number of random recipes

	response = requests.request("GET", url, headers=headers, params=querystring)
	gallery = json.loads(response.text)


	information_response = requests.request("GET", url, headers=headers)
	information = json.loads(information_response.content)

	image_list = []
	id_list = []
	for recipe in gallery['recipes']:
		images = recipe['image']
		image_list.append(images)
		recipe_id = recipe['id']
		id_list.append(recipe_id)


	return render(request, 'index.html', {'gallery': gallery['recipes'], 'images': image_list, 'recipe_id': id_list})


def gallery(request, food):
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
	querystring = {"query": food,
				   "number": "12",
				   "offset": "0",
				   "type": "main course"}
	headers = {
		'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
		'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	}
	response = requests.request("GET", url, headers=headers, params=querystring)
	recipes = json.loads(response.content)


	#grab id of recipes
	images = []
	row = [0,1]
	menu_id = []
	for item in recipes['results']:
		id = item['id']
		menu_id.append(id)
		image_url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
		image_response = requests.request("GET", image_url, headers=headers, params=querystring)
		image = json.loads(image_response.content)
		images.append(image['image'])

	return render(request, 'gallery.html', {'images':images, 'row':row, 'menu_id': menu_id})

def blog(request):
	return render(request, 'blog.html', {})

def recipe(request):
	if request.method == 'POST':
		recipe_search = request.POST.get('recipe').upper()

		# search box

		url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/search"
		querystring = {"query": recipe_search,
					   "number": "1",
					   "offset": "0",
					   "type": "main course"}
		headers = {
			'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
			'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
		}
		response = requests.request("GET", url, headers=headers, params=querystring)
		search = json.loads(response.content)


		# get recipe information
		for item in search['results']:
			recipe_id = item['id']

		url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{recipe_id}/information"

		information_response = requests.request("GET", url, headers=headers)
		information = json.loads(information_response.content)


	return render(request, 'recipe.html', {'recipe': recipe_search, 'search':search['results'], 'information':information})

def search(request):

	return render(request, 'search.html', {})

def random(request):
	return render(request, 'random.html', {})

def random_recipe(request):
	# get recipe information

	headers = {
		'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
		'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	}
	# get random recipe
	url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

	querystring = { "number": "1"} # number of random recipes

	response = requests.request("GET", url, headers=headers, params=querystring)
	random = json.loads(response.text)


	information_response = requests.request("GET", url, headers=headers)
	information = json.loads(information_response.content)
	# print(information)
	#
	return render(request, 'random-recipe.html', {'random':random['recipes']})

def menu(request):
	return render(request, 'menu.html', {})

def meats(request, id):
	url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"

	headers = {
		'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
		'x-rapidapi-key': "ef40eaf520msh733eda9215e1f99p16edb1jsn67d51e5b20f8"
	}
	response = requests.request("GET", url, headers=headers)
	recipes = json.loads(response.content)
	print(recipes['title'])

	return render(request, 'meats.html', {'recipes':recipes})


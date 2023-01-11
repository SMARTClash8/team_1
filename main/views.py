from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm
from .models import Links
from .test import save_photo
from utils.module_model import model_loader, image_classify, get_photo_path
from .main_path import PATH_FOLDER_MODEL, PATH_FOLDER_PROJECT
from .detete_all_files import delete_images
model_path = (PATH_FOLDER_MODEL + "model_from_mentor.h5", 
			  PATH_FOLDER_MODEL + "weights_from_mentor.h5")
model = model_loader(model_path)

def index(request):
	string = ''
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		delete_images('./media/images')
		if form.is_valid():
			x = form.save()
			full_name = PATH_FOLDER_PROJECT + "/media/images/" + str(request.FILES['link'])
			result = image_classify(full_name, 'si_rescale', model)
			# print(round(result[0][2]*100, 2))
			string = "This is the " + result[0][1] + " with chance " + str(round(result[0][2]*100, 2)) + "%"
	else:
		form = UserForm()
	return render(request, 'html/index.html', {'form': form, 'result': string})

def success(request):
	return HttpResponse('successfully uploaded')

	# news = Links.objects.all()
	# if request.method == "POST":
	# 	form = UserForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# print(f"\n\n {news[13]} \n\n")
	# save_photo(news[21])


	# form = UserForm()
	# data = {
	# 	'form': form,
	# 	'news': news
	# }
	# return render(request, 'html/index.html', data)

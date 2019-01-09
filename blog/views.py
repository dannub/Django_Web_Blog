from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def  index (request):
    post= Post.objects.all()
    categories = Post.objects.values('category').distinct()
    context ={
        "Judul" : "Home Blog",
        "Content":"Ini adalah halaman blog",
        'Categories':categories,
        "Posts":post,
    }
    return render(request,"blog/index.html",context)

def  delete (request,delete_id):
    Post.objects.filter(id = delete_id).delete()
    return redirect("blog:index") 

def  update (request,update_id):
    post_update = Post.objects.get(id=update_id)
    category='jurnal'
    if post_update.category == 'Jurnal':
        category='Jurnal'
    elif post_update.category == 'Gosip':
        category='Gosip'
    elif post_update.category == 'Berita':
        category='Berita'
    print(category)
    data={
        'judul':post_update.judul,
        'body':post_update.body,
        'category':category,
    }
    post_form = PostForm(request.POST or None, initial=data,instance=post_update)
    
    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

            return redirect('blog:index')
    context ={
        "Judul" : "Update Blog",
        "post_form" : post_form,
    }

    return render(request,"blog/create.html",context)

def  categoryPost (request,categoryInput):
    post= Post.objects.filter(category=categoryInput)
    categories = Post.objects.values('category').distinct()
    print(categories)
    context ={
        "Judul" : "Home Blog",
        "Content":"Ini adalah halaman blog :",
        'Categories':categories,
        "Posts":post,
    }
    return render(request,"blog/category.html",context)



def  detailPost (request,slugInput):
    post= Post.objects.get(slug=slugInput)
    categories = Post.objects.values('category').distinct()
    context ={
        "Judul" : "Home Blog",
        "Content":"Ini adalah delail blog :",
        'Categories':categories,
        "Posts":post,
    }
    return render(request,"blog/detail.html",context)

def create(request):
    post_form = PostForm(request.POST or None)

    if request.method == 'POST':
        if post_form.is_valid():
            post_form.save()

            return redirect('blog:index')
    context ={
        "Judul" : "Input Blog",
        "post_form" : post_form,
    }

    return render(request,"blog/create.html",context)
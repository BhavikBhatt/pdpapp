from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from pdp_app.models import Post, Comment, State
from pdp_app import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import get_list_or_404, get_object_or_404
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'pdp_app/index.html')
    
def register(request):

    registered = False

    if request.method == 'POST':

        user_form = forms.UserForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = forms.UserForm()

    return render(request,'pdp_app/registration.html',
                          {'user_form':user_form, 'registered':registered})


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'post_list'   # your own name for the list as a template variable
    template_name = 'pdp_app/qa.html'  # Specify your own template name/location
    
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'   # your own name for the list as a template variable
    template_name = 'pdp_app/post_detail.html'  # Specify your own template name/location

@login_required
def add_post(request):
    
    if request.method == 'POST':
        post_form = forms.PostForm(data=request.POST)

        if post_form.is_valid():
            
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('pdp_app:posts'))
        else: 
            print(post_form.errors)
    else:
        post_form = forms.PostForm()
    
    return render(request,'pdp_app/add_post.html',
                          {'post_form':post_form })

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        comment_form = forms.CommentForm(data=request.POST)

        if comment_form.is_valid():
            
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('pdp_app:posts'))
        else: 
            print(comment_form.errors)
    else:
        comment_form = forms.CommentForm()

    return render(request,'pdp_app/add_comment.html',
                          {'comment_form':comment_form, 'post':post})

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('pdp_app:posts')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.author == request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(reverse('pdp_app:posts'))

def state(request, state_name):
    state = get_object_or_404(State, name=state_name)

    return render(request,'pdp_app/state-detail.html',
                          {'state':state})

from django import forms

from pagedown.widgets import PagedownWidget

from .models import Post, Comment


class PostForm(forms.ModelForm):
	"""docstring for PostForm"""
	text = forms.CharField(widget=PagedownWidget)


	class Meta:
		model = Post
		fields = ('title', 'text',)



class CommentForm(forms.ModelForm):
	"""docstring for CommentForm"""
	

	class Meta:
		model = Comment
		fields = ('author', 'text',)
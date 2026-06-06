from allauth.account.forms import SignupForm
from django import forms
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import redirect
from .models import CustomUser

class CustomSignupForm(SignupForm):
    birthday = forms.DateField()
    
    def clean_username(self):
        """Validate username BEFORE saving"""
        username = self.cleaned_data.get('username')
        if username:
            # Convert to lowercase for validation
            username_lower = username.lower()
            
            # Check if username already exists (case-insensitive)
            if CustomUser.objects.filter(username__iexact=username_lower).exists():
                raise forms.ValidationError('This username is already taken.')
            
            # Store the lowercase version
            self.cleaned_data['username'] = username_lower
        
        return username
    
    def clean_email(self):
        """Convert email to lowercase"""
        email = self.cleaned_data.get('email')
        if email:
            email = email.lower()
            self.cleaned_data['email'] = email
        return email
    
    def save(self, request):
        """Save the user with lowercase username and email"""
        try:
            # The username is already lowercased from clean_username
            user = super().save(request)
            
            # Add birthday
            user.birthday = self.cleaned_data.get('birthday')
            
            # Save the additional fields
            user.save()
            
            return user
            
        except IntegrityError as e:
            # Handle any unexpected integrity errors
            from django.contrib import messages
            from django.shortcuts import redirect
            
            if 'username' in str(e):
                messages.error(request, 'This username is already taken. Please choose another one.')
            else:
                messages.error(request, 'An error occurred during registration. Please try again.')
            
            # Redirect back to signup page
            return redirect('account_signup')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'username', 'name', 'bio', 'website']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input-field','placeholder': 'Username'}),
            'name': forms.TextInput(attrs={'class': 'input-field','placeholder': 'Name'}),
            'bio': forms.Textarea(attrs={'class': 'input-field resize-none','rows':2, 'placeholder': 'Bio', 'maxlength': '250'}),
        }
    
    def clean_username(self):
        """Ensure username is unique when editing profile"""
        username = self.cleaned_data.get('username')
        if username:
            username = username.lower()
            
            # Get the current user being edited
            instance = getattr(self, 'instance', None)
            
            # Check if another user has this username
            if CustomUser.objects.filter(username=username).exclude(pk=instance.pk if instance else None).exists():
                raise forms.ValidationError('This username is already taken.')
        
        return username

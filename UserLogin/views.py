from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from UserLogin.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 



# Crearemos la funcion, para loguear a un usuario.

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('user')
            password = form.cleaned_data.get('password')

            user = authenticate(username=user, passw=password)

            if user is not None:
                login(request, user)

                return render(request, 'Principal/index.html', {'message': f'Bienvenido {user}'})
            
            else:
                return render(request, 'Principal/index.html', {'message':'Error, algún dato ingresado ha sido incorrecto.'})
            
        else:
                return render(request, 'Principal/index.html', {'message':'Error, algún dato ingresado ha sido incorrecto.'})
        
    form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form':form})

# Crearemos la funcion, registrar a un usuario.

def register(request):
     
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, 'registration/login.html', {'message':'Usuario realizado con éxito. '}) 

    else:
        form = UserRegisterForm()

    return render(request, 'registration/register.html', {'form':form})
       

@login_required
def logout_view(request):
    logout(request)
    return redirect('UserLogin/login')



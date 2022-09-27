from flask import render_template, redirect, session, request, flash
from flask_app import app
from datetime import date

#Importación del modelo
from flask_app.models.users import User
from flask_app.models.citas import Cita


@app.route('/new/add')
def new_add():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    return render_template('new_add.html', user=user, hoy = date.today())

@app.route('/create/new', methods=['POST']) 
def create_new():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    if not Cita.valida_cita(request.form): #llamo a la funcion de cita y envio formulario
        return redirect ('/new/add')           
#verificar
    Cita.save(request.form)     
    return redirect ('/dashboard')

@app.route('/edit/cita/<int:id>') 
def edit_cita (id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario = {
        'id': session['user_id']
    }

    user = User.get_by_id(formulario) #Instancia del usuario que inicio sesión

    form_cita = {"id": id}

    cita = Cita.get_by_id(form_cita)

    return render_template('edit_cita.html', user=user, cita=cita, hoy = date.today())
#verificar

@app.route ('/update/cita', methods=['POST'])
def update_cita():
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')
    if not Cita.valida_cita (request.form):
        return redirect ('/edit/cita/'+request.form['id'])

    Cita.update(request.form)
    return redirect ('/dashboard') 

@app.route('/delete/cita/<int:id>')
def delete_cita(id):
    if 'user_id' not in session: #Comprobamos que el usuario haya iniciado sesiónh
        return redirect('/')

    formulario_cita = {"id": id}
    Cita.delete(formulario_cita)

    return redirect ('/dashboard')





    












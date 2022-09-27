from flask_app.config.mysqlconnection import  connectToMySQL

class Cita:

    def __init__(self, data):
        self.id = data['id']
        self.task = data['task']
        self.date = data['date']
        self.status = data['status']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

        #LEFT JOIN
        self.first_name = data['first_name']

    @staticmethod
    def valida_cita(formulario):
        es_valido = True

        if len(formulario['task']) < 3:
            flash('tarea debe tener al menos 3 caracteres', 'citas')
            es_valido = False

        
        if len(formulario['status']) =="":
            flash('colocar status', 'citas')
            es_valido = False
        
        if formulario['date'] == "":
            flash('Ingrese una fecha', 'citas')
            
            es_valido = False

        return es_valido


    @classmethod
    #funcion de guardar 
    def save(cls, formulario):
        query = "INSERT INTO citas  (task, date,  status, user_id) VALUES (%(task)s, %(date)s, %(status)s, %(user_id)s) "
        result = connectToMySQL('citas1').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls, formulario):
        query = "SELECT citas.*, first_name  FROM citas LEFT JOIN users ON users.id = citas.user_id WHERE (citas.status='Hecho' OR citas.status='Pendiente')AND citas.user_id = %(id)s"        
        results = connectToMySQL('citas1').query_db(query, formulario) #Lista de diccionarios )
        citas = []
        for cita in results:            
            citas.append(cls(cita))
        return citas


    @classmethod
    def fecha_not(cls, formulario):
        query = "SELECT * FROM citas  LEFT JOIN users ON users.id = citas.user_id WHERE current_date () >= citas.date and citas.status= 'Perdida' AND citas.user_id = %(id)s"        
        results = connectToMySQL('citas1').query_db(query, formulario) 
        fecha_citas = []
        for citas in results:            
            fecha_citas.append(cls(citas))
        return fecha_citas

    @classmethod
    def get_by_id(cls, formulario): 
        query = "SELECT citas.*, first_name  FROM citas LEFT JOIN users ON users.id = citas.user_id WHERE citas.id = %(id)s"
        result = connectToMySQL('citas1').query_db(query, formulario) #Lista de diccionarios
        citas = cls(result[0])
        return citas

    @classmethod
    def update(cls, formulario):
        query = "UPDATE citas SET task=%(task)s, date=%(date)s, status=%(status)s WHERE id = %(id)s"
        result = connectToMySQL('citas1').query_db(query, formulario)
        return result

    @classmethod
    def delete(cls, formulario): 
        query = "DELETE FROM citas WHERE id = %(id)s"
        result = connectToMySQL('citas1').query_db(query, formulario)
        return result 


    
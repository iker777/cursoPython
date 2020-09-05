class Employee:  # Es una clase para crear el eMail a partir del nombre y el apellido
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property  # Puedes llamar a la función como si fuese un atributo
    def email(self):  # Función para conseguir todo el email del empleado
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):  # Función para conseguir todo el nombre del empleado
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):  # El atributo name es el atributo que estamos tratando de insertar como atributo
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

if __name__ == '__main__':    
    emp_1 = Employee('John', 'Smith')
    emp_1.fullname = 'Gary Cooper'  

    print(emp_1.first)  # > Jim
    print(emp_1.email)  # LLAMAS A LA FUNCIÓN IGUAL QUE A UN MÉTODO > Jim.Smith@email.com / El email cambia porque con el nuevo método coge los atributos actuales
    print(emp_1.fullname) # LLAMAS AL MÉTODO IGUAL QUE A UN ATRIBUTO> Jim Smith  / El fullname también cambia por lo mismo 
   

    del emp_1.fullname  # Borra los atributos guardados dentro del método
    print(emp_1.first, emp_1.last)
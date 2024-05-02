
# Herencias - Ejercicio 2
# Ejercicio de herencia y uso de super:
# Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.
# Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.


class Person: 
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_attributes(self):
        print(f'The persons name is {self.name} and is {self.age}')

class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade
    def print_grade(self):
        print(f'{self.name} is on {self.grade} grade')


student1 = Student("Lebron",33,"7th")

student1.print_grade()

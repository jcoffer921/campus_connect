# student.py
# Defines the Student class for Campus Connect

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.connections = []

    def __str__(self):
        return f'{self.name} {self.major}'

    def add_connection(self, connection):
        # Storing the object to be able to traverse through connections
        self.connections.append(connection)
        connection.connections.append(self)

    def remove_connection(self, connection):
        # Using connection object again because its more flexible
        self.connections.remove(connection)
        connection.connections.remove(self)

    def show_connections(self):
        '''
        Prints all the connections the student has connected to
        '''
        print(f"Connections for {self.name}:")
        for connection in self.connections:
            print(f" - {connection.name}")



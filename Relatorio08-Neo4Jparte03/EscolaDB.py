from db.database import Graph


class EscolaDB(object):
    def __init__(self):
        self.db = Graph(uri='bolt://3.208.94.175:7687',
                        user='neo4j', password='photographs-dent-laundries')

    def create(self, person):
        return self.db.execute_query('CREATE (n:Person {name:$name, age:$age, area:$area}) return n',
                                     {'name': person['name'], 'age': person['age'], 'area': person['area']})

    def create_grade(self, grade):
        return self.db.execute_query('CREATE (n:Grade {assunto:$assunto, horario:$horario}) return n',
                                     {'assunto': grade['assunto'], 'horario': grade['horario']})

    def read_by_name(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) RETURN n',
                                     {'name': person['name']})

    def read_all_nodes(self):
        return self.db.execute_query('MATCH (n) RETURN n')

    def update_age(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) SET n.age = $age RETURN n',
                                     {'name': person['name'], 'age': person['age']})

    def delete(self, person):
        return self.db.execute_query('MATCH (n:Person {name:$name}) DELETE n',
                                     {'name': person['name']})

    def delete_all_nodes(self):
        return self.db.execute_query('MATCH (n) DETACH DELETE n')

    def create_relation(self, person, grade, year):
        return self.db.execute_query(
            'MATCH (n:Person {name:$name}), (g:Grade {assunto:$assunto}) CREATE (n)-[r:LECIONA{year: $year}]->(g) RETURN n, r, g',
            {'name': person['name'], 'grade': grade['assunto'], 'year': year})

    def read_relation(self, person, grade):
        return self.db.execute_query('MATCH (n:Person {name:$name})-[r]->(g:grade {assunto:$assunto}) RETURN n, r, g',
                                     {'name': person['name'], 'assunto': grade['assunto']})

from cassandra.cluster import Cluster

class Test_DB:
    def setup_class(cls):
        cluster = Cluster()
        global session
        session = cluster.connect('test_python')

    def test_1_insert_data(self):
        session.execute("INSERT INTO employee_by_id (id,name,position) VALUES (1,'KUKU1', 'Automation eng.');")
        session.execute("INSERT INTO employee_by_id (id,name,position) VALUES (2,'KUKU2', 'CTO');")
        session.execute("INSERT INTO employee_by_id (id,name,position) VALUES (3,'KUKU3', 'SCRUM MASTER');")
        session.execute("INSERT INTO employee_by_id (id,name,position) VALUES (4,'KUKU4', 'QA');")
        session.execute("INSERT INTO employee_by_id (id,name,position) VALUES (5,'KUKU5', 'BOSS');")
        data = session.execute("SELECT * FROM employee_by_id")
        print("")

        for item in data:
            print("ID: " + str(item.id) + " Name: " +item.name + " Position: " + item.position)


    def teardown_class(self):
        session.shutdown()
from neo4j import GraphDatabase

def run_query_and_print_results(query, session):
    records = session.run(query)
    for data in records:
        print(data)

# Connect to the Neo4j database
driver = GraphDatabase.driver(uri="bolt://localhost:7687", auth=("neo4j", "12345678"))
session = driver.session()

# Define queries
query1 = "MATCH (N:Movie) RETURN N.title"
query2 = "MATCH (N:Movie)-[:ACTED_IN]-(P:Person) RETURN N.title, P.name"

run_query_and_print_results(query1, session)
run_query_and_print_results(query2, session)

# Close the session and the driver
session.close()
driver.close()

from fastapi import FastAPI
from database import Neo4jConnection

app = FastAPI(title="API con Neo4j")

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "fenomenologia2024"  # ✅ contraseña correcta

conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

@app.get("/")
def home():
    return {"mensaje": "Servidor FastAPI conectado a Neo4j"}

@app.get("/nodos")
def listar_nodos():
    query = "MATCH (n) RETURN n LIMIT 10"
    result = conn.query(query)
    return {"nodos": result}

@app.get("/crear")
def crear_nodo(nombre: str):
    query = "CREATE (n:Prueba {nombre: $nombre}) RETURN n"
    result = conn.query(query, {"nombre": nombre})
    return {"resultado": result}


from pymongo import MongoClient
from bson import ObjectId

# Conexão com o MongoDB via DESKTOP DOCKER
client = MongoClient("mongodb://root:root@localhost:27017/?authSource=admin")
db = client["testandocruddolucas"]
col = db["usuarios_do_banheiro_da_univassouras"]

# CREATE
def create_user( nome, email, idade):
    user = {"nome": nome, "email": email, "idade": idade}
    res = col.insert_one(user)
    print(f"[CREATE] Usuário do banheiro da Univassouras cadastrado com sucesso! ID: {res.inserted_id}")

# READ
def read_users():
    print("[READ] Listando usuários do banheiro cadastrados...")
    for user in col.find():
        print(user)

# UPDATE
def update_user(user_id, new_data):
    res = col.update_one({"_id": ObjectId(user_id)}, {"$set": new_data})
    print(f"[UPDATE] Usuários modificados: {res.modified_count}")

# DELETE
def delete_user(user_id):
    res = col.delete_one({"_id": ObjectId(user_id)})
    print(f"[DELETE] Usuários removidos!: {res.deleted_count} (é perigoso não poder usar um banheiro...)")

# TESTANDO A CRUD
if __name__ == "__main__":
    res = col.insert_one({"nome": "Lucas", "email": "lucas@example.com", "Idade": 27})
    user_id = res.inserted_id
    print(f"Usuário criado com id {user_id}")

    read_users()

    update_user(str(user_id), {"age": 23})

    delete_user(str(user_id))

    read_users()

    input("Pressione ENTER para sair...")

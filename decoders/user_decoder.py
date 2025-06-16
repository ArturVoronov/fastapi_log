def decode_todo(doc) -> dict:
        return {
            'id':doc.id,
            'username': doc.username,
            'email': doc.email,
            'password':doc.password,
            'is_staff': doc.is_staff,
            'is_active':doc.is_active

              }
def decode_todos(docs) -> list:
        return [
             decode_todo(doc) for doc in docs
         ]

def decode_todo_product(doc) -> dict:
        return {
            'id':doc.id,
            'name': doc.name,
            'category': doc.category,
            'description':doc.description,
            'price': doc.price
              }
def decode_todos_product(docs) -> list:
        return [
             decode_todo_product(doc) for doc in docs
         ]
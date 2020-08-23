import uvicorn

from ariadne import QueryType, gql, make_executable_schema, MutationType
from ariadne.asgi import GraphQL

type_defs = gql("""
  type Query {
    user: User
    users: [User]
  }
  
  type Mutation {
    createUser(name: String, email: String): User
  }

  type User {
    id: ID!
    name: String
    email: String!
  }
""")

query = QueryType()
mutation = MutationType()
users = [{"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
         {"id": 2, "name": "Alan Turing", "email": "alan@example.com"}]

@mutation.field("createUser")
def resolver_createUser(_, info, name, email):
    newdict = {"id": users[-1]["id"], "name": name, "email":email }
    users.append(newdict)
    print(users)
    return newdict

@query.field("user")
def resolve_user(_, info):
    print("hi")
    return users[0]


@query.field("users")
def resolve_users(_, info):
    return users


schema = make_executable_schema(type_defs, [query, mutation])
app = GraphQL(schema, debug=True)


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=5001)

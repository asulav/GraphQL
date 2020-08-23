import uvicorn

from ariadne import QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = gql("""
  type Query {
    user: User
    users: [User]
  }
  type User {
    id: ID!
    name: String
    email: String!
  }
""")

query = QueryType()


@query.field("user")
def resolve_user(_, info):
    return users[0]


@query.field("users")
def resolve_users(_, info):
    return users


schema = make_executable_schema(type_defs, query)
app = GraphQL(schema, debug=True)

users = [
    {"id": 1, "name": "Ada Lovelace", "email": "ada@example.com"},
    {"id": 2, "name": "Alan Turing", "email": "alan@example.com"},
]


if __name__ == "__main__":
    uvicorn.run(application, host="0.0.0.0", port=5001)

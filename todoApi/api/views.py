from rest_framework.response import Response

def getRoutes(response):
    routes = [
        {
            "endpoint":"/items",
            "method":"GET",
            "body":None,
            "description":"return array of items"
        },
        {
            "endpoint":"/item/id",
            "method":"GET",
            "body":None,
            "description":"return an item"
        },
        {
            "endpoint":"/item/create",
            "method":"POST",
            "body":{'body':""},
            "description":"create an item"
        },
        {
            "endpoint":"/item/create",
            "method":"POST",
            "body":{'body':""},
            "description":"create an item"
        },
        {
            "endpoint":"/item/id/update",
            "method":"PUT",
            "body":{'body':""},
            "description":"update an item"
        },
        {
            "endpoint":"/item/id/delete",
            "method":"DELETE",
            "body":{'body':""},
            "description":"delete an item"
        },
    ]
    return Response(routes)
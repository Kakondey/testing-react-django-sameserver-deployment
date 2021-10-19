from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.conf import settings
# This will return a list of books


@api_view(["GET"])
def book(request):
    books = ["Pro Python", "Fluent Python",
             "Speaking javascript", "The Go programming language"]
    return Response(status=status.HTTP_200_OK, data={"data": books})


def index(request):
    dir = settings.BASE_DIR
    # import pdb
    # pdb.set_trace()
    return render(request, "build/index.html")

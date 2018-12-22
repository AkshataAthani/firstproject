from django.http import HttpResponse

def getwordcount(request):
   fulltext= request.GET['fulltext']
   fulltextsplit =fulltext.split()
   fulltextcount = len(fulltextsplit)
   return fulltextcount

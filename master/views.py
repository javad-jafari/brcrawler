from django.shortcuts import render
from master.models import  Cluster, ClusterTen, ClusterSixty



def cluster_view(req):
    clusters = Cluster.objects.all()[0:57]
    return render(req, "index_one.html", {"clusters":clusters})



def cluster_view_ten(req):
    clusters = ClusterTen.objects.all()[0:57]
    return render(req, "index_ten.html", {"clusters":clusters})



def cluster_view_sixty(req):
    clusters = ClusterSixty.objects.all()[0:57]
    return render(req, "index_sixty.html", {"clusters":clusters})
from django.db import models




class Cluster(models.Model):

    name = models.CharField(max_length=256)
    propagate_date = models.CharField(max_length=256)
    last_value = models.CharField(max_length=256)
    change = models.CharField(max_length=256)
    precent = models.CharField(max_length=256)
    max_value = models.CharField(max_length=256)
    min_value = models.CharField(max_length=256)


    def __repr__(self) -> str:
        return "<Cluster '{}' '{}'>".format( self.id, self.name )


    def __str__(self) -> str:
        return self.name
    


class ClusterTen(models.Model):

    name = models.CharField(max_length=256)
    propagate_date = models.CharField(max_length=256)
    last_value = models.CharField(max_length=256)
    change = models.CharField(max_length=256)
    precent = models.CharField(max_length=256)
    max_value = models.CharField(max_length=256)
    min_value = models.CharField(max_length=256)


    def __repr__(self) -> str:
        return "<Cluster '{}' '{}'>".format( self.id, self.name )

    def __str__(self) -> str:
        return self.name

class ClusterSixty(models.Model):

    name = models.CharField(max_length=256)
    propagate_date = models.CharField(max_length=256)
    last_value = models.CharField(max_length=256)
    change = models.CharField(max_length=256)
    precent = models.CharField(max_length=256)
    max_value = models.CharField(max_length=256)
    min_value = models.CharField(max_length=256)


    def __repr__(self) -> str:
        return "<Cluster '{}' '{}'>".format( self.id, self.name )
    
    
    def __str__(self) -> str:
        return self.name
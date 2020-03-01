from apps.comments import models as comments_models



def getComments(id_homeless: int):
    comments = comments_models.Comment.objects.filter(homeless__id = id_homeless)
    return comments
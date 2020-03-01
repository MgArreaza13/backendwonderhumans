from apps.donations import models as donations_models 


def getDonations(id_homeless: int):
    donations = donations_models.Donation.objects.filter(event__homeless__id = id_homeless)
    return donations


def getEvents(id_homeless: int):
    events = donations_models.Event.objects.filter(homeless__id = id_homeless)
    return events
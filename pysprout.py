import requests

class LearnSproutClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def list_organizations(self):
        url = "https://v1.api.learnsprout.com/org"
        payload = {"apikey": self.api_key}
        response = requests.get(url, params=payload)
        return response.json()

    def get_schools(self, org_id):
        url="https://v1.api.learnsprout.com/org/%s/school"%org_id
        payload = {"apikey": self.api_key}
        response = requests.get(url, params=payload)
        return response.json()

    def get_teachers(self, org_id, teacher):
        url = "https://v1.api.learnsprout.com/org/%s/teacher"%org_id
        payload = {"apikey": self.api_key}
        response = requests.get(url, params=payload)
        return response.json()

    def get_students(self, org_id, student):
        url = "https://v1.api.learnsprout.com/org/%s/student" % org_id
        payload = {"apikey": self.api_key}
        response = requests.get(url, params=payload)
        return response.json()

def test_sprout():
    lsc = LearnSproutClient("fcb8534c-e4ee-4e02-8b22-9328db1dac18")
    orgs =  lsc.list_organizations()
    print "Number of orgs: %d"%len(orgs)
    print "org 1 name, id: %s %s"%(orgs[0]['name'], orgs[0]['id'])

    schools = lsc.get_schools(orgs[0]['id'])
    print schools
    school1 = schools['data'][0]['name']
    print school1
    teachers = lsc.get_teachers(teachers[0]['id'])


if __name__ == "__main__":
    test_sprout()
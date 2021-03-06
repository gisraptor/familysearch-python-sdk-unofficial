# Python imports

# Magic

class Person:
    def __init__(self):
        pass
        
    def create_person(self, data):
        pass # Working on it!
        #url = self.tree_base + 'persons'
        #response = self._request(url, data)    
        
    def parents(self, pid):
        url = self.tree_base + pid + "/parents"
        response = self._request(url)
        return response
    
    def spouses(self, pid):
        url = self.tree_base + pid + "/spouses"
        response = self._request(url)
        return response
    
    def children(self, pid):
        url = self.tree_base + pid + "/children"
        response = self._request(url)
        return response
    
    def memories_query(self, pid):
        url = self.tree_base + 'persons/' + pid + '/memories'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_portrait(self, pid):
        url = tree_base + "persons/" + pid + 'portrait'
        response = self._request(url)
        response = self._fs2py(response)
        return response
        
    def person_portraits(self, pid):
        url = tree_base + "persons/" + pid + 'portraits'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def spouse_relationships(self, pid):
        url = tree_base + "persons/" + pid + '/spouse-relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def child_relationships(self, pid):
        url = tree_base + "persons/" + pid + 'child-relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def parent_relationships(self, pid):
        url = tree_base + "persons/" + pid + 'parent_relationships'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def persons_with_relationships(self):
        url = tree_base + "persons-with-relationships.json?person=" + pid
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_conclusion(self, pic, cid):
        pass # TODO
    
    def person_merge(self, pid, dpid):
        pass # TODO
    
    def person_change_summary(self, pid):
        url = tree_base + "persons/" + pid + '/change-summary'
        response = self._request(url)
        response = self._fs2py(response)
        return response
    
    def person_not_a_match(self, pid, dpid):
        pass # TODO
    
    def person_restore(self, pid):
        pass # TODO
    
    def preferred_spouse_relationship(self, uid, pid):
        pass # TODO
    
    def preferred_parent_relationship(self, uid, pid):
        pass # TODO
    
    
# FamilySearch imports

from . import FamilySearch
FamilySearch.__bases__ += (Person,)
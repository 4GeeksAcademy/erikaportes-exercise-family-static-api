last_name = "Jackson"

members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22]},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3]},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1]}
]


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if not member.get("first_name") or not member["first_name"].strip():
            raise Exception("First name is required")
        
        if not isinstance(member.get("age"), int) or member["age"] <= 0:
            raise Exception("Age must be a positive integer")

        new_member = {
            "id": self._generate_id(),
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member.get("lucky_numbers", [])
        }

        self._members.append(new_member)
        return new_member

    def delete_member(self, member_id):
        for index, member in enumerate(self._members):
            if member["id"] == member_id:
                del self._members[index]
                return True
        return False

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        return None

    def get_all_members(self):
        return list(self._members)
    
family = FamilyStructure(last_name) 
for m in members:      
    family.add_member(m)    
    print(family.get_all_members())


# """
# Update this file to implement the following already declared methods:
# - add_member: Should add a member to the self._members list
# - delete_member: Should delete a member from the self._members list
# - get_member: Should return a member from the self._members list
# """

# class FamilyStructure:
#     def __init__(self, last_name):
#         self.last_name = last_name
#         self._next_id = 1
#         self._members = [
#             {
#                 "id": self._generate_id(),
#                 "first_name": "John",
#                 "last_name": last_name,
#                 "age": 33,
#                 "lucky_numbers": [7, 13, 22]
#             }
#         ]

#     # This method generates a unique incremental ID
#     def _generate_id(self):
#         generated_id = self._next_id
#         self._next_id += 1
#         return generated_id

#     def add_member(self, member):
#         ## You have to implement this method
#         ## Append the member to the list of _members
#         pass

#     def delete_member(self, id):
#         ## You have to implement this method
#         ## Loop the list and delete the member with the given id
#         pass

#     def get_member(self, id):
#         ## You have to implement this method
#         ## Loop all the members and return the one with the given id
#         pass

#     # This method is done, it returns a list with all the family members
#     def get_all_members(self):
#         return self._members

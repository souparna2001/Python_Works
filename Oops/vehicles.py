class Parent:

    def properties(self):
        self.vehicles=["splender","cdd848"]
        return self.vehicles

class Child(Parent):

    def properties(self):
        self.context=super().properties() 
        self.context.append("pulsar")
        return self.context


new=Child() 
print(new.properties())

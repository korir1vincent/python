callable(3)
class network_providers:
    def __init__(self,Name,Year_founded,No_of_users):
        self.Name= Name
        self.Year_founded= Year_founded
        self.No_of_users= No_of_users

    def display(self):
        print(f"{self.Name} was founded in the year {self.Year_founded} and has {self.No_of_users} users")

network_providers= network_providers('Safaricom','1992','12,132,234')
network_providers.display()

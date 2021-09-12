
from ..models import Consumer, Package, Package_Type,  Provider, User_Profile, User

class Context_jugu():
    def __init__(self,given_model=None, page_name='dashboard.html') -> None:

        self.model = None
        self.page_name = page_name
        
        if(given_model):
            self.model = given_model
        else:
            if(page_name=='consumers'):
                self.model = Consumer

    def get_context(self):
        return self.model.objects.all().order_by('-provided_at')
        return self.model.objects.filter(priority=1).order_by('-provided_at')[:5]

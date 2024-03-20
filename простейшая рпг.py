class AbstactAccount:

    def __init__(self,**kwargs) -> None:
        self.name = kwargs['nikname']
        self.gender = kwargs['gender']
        
    def __str__(self) -> str:
        return str(self.__dict__)
    
    class plaerAccount(AbstactAccount):
    def __init__(self, **kwargs) -> None:
        self.balance = kwargs['balance']
        self.playerFunction = kwargs['playerFunction']
        super().__init__(**kwargs)

    class adminAccount(AbstactAccount):
    def __init__(self, **kwargs) -> None:
self.bonuses = kwargs['adminFunction']
        super().__init__(**kwargs)

        class ClassPlaer:
                def __init__(
        self,
        health:int,
        mana:int,
        damage:int,
        stamina:int,
        user:plaerAccount,
    ) -> None:
        self.health = health
        self.mana = mana
        self.damage = damage
        self.stamina = stamina
        self.plaer = plaer
        self.weapon = weapon
        self.is_busy = False
        
        def __str__(self) -> str:
            return str(self.__dict__)
    
        def __repr__(self) -> str:
            return str(self.__dict__)

        class ClassPlayerList:
    def __init__(
        self,
        class_list,
        user_list,
        ) -> None:
        self.classPlayer_list = classPlayer_list
        self.user_list = user_list
        self.plaer_list = [car.plaer for car in class_list]

    def __str__(self) -> str:
        return str(self.__dict__)




    from models import ClassPlayerList,plaerAccount,ClassPlaer


    class Menu:
        player = playerAccount(
        nikname='Gora',
        gender='male',
        balance = '0')

    cps = ClassPlayerList(
        classPlayer_list
        
        
        

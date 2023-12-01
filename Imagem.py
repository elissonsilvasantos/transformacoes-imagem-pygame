
class Imagem:
    
    def __init__(self, obj, pos_x=0, pos_y=0, largura=10, altura=10, angulo=0):
        self._obj = obj # objeto de imagem do pygame
        
        self._pos_x = pos_x
        self._pos_y = pos_y

        self._largura = largura
        self._altura = altura

        self._angulo = angulo

    # métodos de acesso ao objeto de imagem do pygame
    @property
    def obj(self):
        return self._obj
    
    @obj.setter
    def obj(self, obj):
        self._obj = obj
    
    # métodos de acesso à posição x
    @property
    def pos_x(self):
        return self._pos_x
    
    @pos_x.setter
    def pos_x(self, pos_x):
        self._pos_x = pos_x

    # métodos de acesso à posição y
    @property
    def pos_y(self):
        return self._pos_y
    
    @pos_y.setter
    def pos_y(self, pos_y):
        self._pos_y = pos_y

    # métodos de acesso à largura
    @property
    def largura(self):
        return self._largura
    
    @largura.setter
    def largura(self, largura):
        self._largura = largura

    # métodos de acesso à altura
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, altura):
        self._altura = altura
    
    # métodos de acesso ao ângulo
    @property
    def angulo(self):
        return self._angulo
    
    @angulo.setter
    def angulo(self, angulo):
        self._angulo = angulo

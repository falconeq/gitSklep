from django.db import models  # Moduł do tworzenia modeli baz danych
from django.contrib.auth.models import User  # Model użytkownika do uwierzytelniania

# Model klienta
class Customer(models.Model):  # Reprezentuje klienta
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)  # Relacja 1:1 z User
    name = models.CharField(max_length=100, null=True)  # Imię klienta
    email = models.EmailField(max_length=200)  # E-mail klienta

    def __str__(self):  
        return self.name + ", email: " + str(self.email)  # Reprezentacja obiektu jako imię

# Model produktu
class Product(models.Model):  # Reprezentuje produkt
    name = models.CharField(max_length=200)  # Nazwa produktu
    price = models.FloatField()  # Cena produktu
    digital = models.BooleanField(default=False, null=True, blank=True)  # Cyfrowy produkt (True/False)
    image = models.ImageField(null=True, blank=True)  # Opcjonalny obrazek produktu

    def __str__(self):  
        return self.name + ", Cena: " + str(self.price)  # Reprezentacja obiektu jako nazwa

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

# Model zamówienia
class Order(models.Model):  # Reprezentuje zamówienie
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)  # Powiązanie z klientem
    order_date = models.DateTimeField(auto_now_add=True)  # Data złożenia zamówienia
    completed = models.BooleanField(default=False)  # Status zamówienia (ukończone/niedokończone)
    transaction_id = models.CharField(max_length=100, null=True)  # ID transakcji

    def __str__(self):  
        return str(self.id)  # Reprezentacja obiektu jako ID
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum ([item.get_total for item in orderitems ])
        return total
    
    @property
    def get_cart_items(self):
        oderitems = self.orderitem_set.all()
        total = sum ([ item.quantity for item in oderitems ])
        return total

# Model Zamawianego Produktu
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
# Model Adresu Dostawy
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    zipcode = models.CharField(max_length=10, null=False)
    country = models.CharField(max_length=50, null=False)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.address
    
# Po utworzeniu modelów, w pliku admin.py dodajemy do widoku admina nowo powstane tabele (Na stronie admin)
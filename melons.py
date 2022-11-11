"""Classes for melon orders."""
class AbstractMelonOrder:
    """holds common vars"""
    def __init__(self, qty, species,country_code ):  # initialixing an order type domestic or international and adding comon atributes 
        self.species=species # we are saying that species are chanchabel you can assighn any name  
        self.qty=qty
        self.order_type=None # this is a fanctioon which one you can reuse in different orders like Domestic or International
        self.tax=None # tax is also changable it depence which order you are creating Domestic or International. It is much easy to reuse
        self.country_code = country_code
      
        


# class DomesticMelonOrder: 
class DomesticMelonOrder(AbstractMelonOrder): 
    """A melon order within the USA."""

    def __init__(self, species, qty):               #order2=DomesticMelonOrder("yw", 4) 
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self):                                        
        """Calculate price, including tax."""

        base_price = 5 *1.5                                             
        total = (1 + self.tax) * self.qty * base_price  #total=(1+.08) * (4*5)= 21.6
        #    order3 =(1+0.08)*6*5= 32.4 

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder:
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17
        self.flat_fee= 3

    def get_total(self):
        """Calculate price, including tax."""

        base_price = (5*1.5)
    
                # total = (1 + self.tax) * self.qty * base_price
        #order3 =(1+0.17)*6*5= 35.1 
        if self.qty<10:
            total=((1 + self.tax) * self.qty * base_price)+3
            return total
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
   

# class AbstractMelonOrder(InternationalMelonOrder):
#     """holds common vars"""
#         self.species=None
        





#abstract....wont have its own instance...its a superclass...itsnon-functioning
#we only instantize subclasses of it
#seems like its a class that gets subclasses to do things via its own methods
#like both classes can borrown from this and its their tether almost?
#seems like its a class that you can use the othersmethods for and its own.

#look iup dependency injection....one way to wrie up all different objects in application 
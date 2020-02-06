"""Classes for melon orders."""



class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, country_code, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code
        self.order_type = order_type
        self.tax = tax


    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        super().__init__(species, qty, 'US', 'domestic', .08)
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.shipped = False
        # self.order_type = "domestic"
        # self.tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code) :
        super().__init__(species, qty, country_code, 'international', .15)
        """Initialize melon order attributes."""

        # self.species = species
        # self.qty = qty
        # self.country_code = country_code
        # # self.shipped = False
        # self.order_type = "international"
        # self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

from django.db import models
from .helpers import AbstractModel
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Category(AbstractModel):
    """_summary_

    Args:
        AbstractModel (Category): this model is used for list of category exists in product

    Returns:
        _type_: model object : category name of category in product 
    """
    category_id = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100, verbose_name="category_name")

    def __str__(self) -> str:
        return self.name


class Product(AbstractModel):
    """_summary_

    Args:
        AbstractModel (Product): this model is used for what are the possible fields avilable in product model

    Returns:
        _type_: model object: list of fields avilable in product model return all field except id 
    """
    name         = models.CharField(max_length=75, verbose_name="product_name")
    product_sku  = models.CharField(max_length=50, verbose_name="product_sku")
    # price        = models.FloatField()
    weight       = models.FloatField()
    cart_description = models.CharField(max_length=250, verbose_name="cart_description")
    short_description  = models.CharField(max_length=500, verbose_name="short_description")
    long_description =  models.TextField(verbose_name=_("description"), help_text=_("Not Required"), blank=True)
    category_id    = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.FloatField()
    slug = models.SlugField(max_length=255)
    
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )

    def __str__(self) -> str:
        return self.name
    

class ProductImage(AbstractModel):
    """_summary_

    Args:
        AbstractModel (ProductImage): one product can have multiple images 
    """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.FileField(blank=True)


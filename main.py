from sqlalchemy import create_engine,Column,String,Text,DateTime,Integer
from sqlalchemy.orm import declarative_base,sessionmaker
from datetime import datetime

# base
Base = declarative_base()
engine =create_engine("sqlite:///debts.db")
Session=sessionmaker(bind=engine)

class Debts(Base):
    __tablename__ = "debts"

    id= Column(Integer(),primary_key=True)
    customer_name= Column(String(),nullable=True)
    customer_email = Column(String(20),nullable=True)
    items_taken = Column(Text(),nullable=True)
    quantity_of_items=Column(Integer(),nullable=True)
    price_per_item = Column(Integer(),default=0.0,nullable=True)
    total_price_to_pay = Column(Integer(),nullable=True)
    price_paid = Column(Integer(),nullable=True)
    balance_to_pay =Column(Integer(),nullable=True)
    created_at = Column(DateTime(),default=datetime.utcnow)
    #  date_created= Column(DateTime(),default=datetime.utcnow)

Base.metadata.create_all(bind=engine) 
debts_session=Session()  

# delete prior data if their is
debts_session.query(Debts).delete()
debts_session.commit()

debts_list=[
    {
      "customer_name":"Isaac juma",
      "customer_email":"juma@gmai.com",
      "items_taken":"4 inch nails",
      "quantity_of_items":5,
      "price_per_item":200,
      "price_paid":500,
      "created_at":datetime.utcnow(),
    },
     {
        "customer_name": "Mary Wambui",
        "customer_email": "mary.wambui@example.com",
        "items_taken": "Wooden planks",
        "quantity_of_items": 10,
        "price_per_item": 350,
        "price_paid": 2000,
        "created_at": datetime.utcnow()
    },
    {
        "customer_name": "John Doe",
        "customer_email": "john.doe@example.com",
        "items_taken": "Paint buckets",
        "quantity_of_items": 3,
        "price_per_item": 1200,
        "price_paid": 3000,
        "created_at": datetime.utcnow()
    },
    {
        "customer_name": "Jane Smith",
        "customer_email": "jane.smith@example.com",
        "items_taken": "Screwdrivers",
        "quantity_of_items": 8,
        "price_per_item": 150,
        "price_paid": 800,
        "created_at": datetime.utcnow()
    },
    {
        "customer_name": "Robert Johnson",
        "customer_email": "robert.j@example.com",
        "items_taken": "Hammer sets",
        "quantity_of_items": 2,
        "price_per_item": 800,
        "price_paid": 1500,
        "created_at": datetime.utcnow()
    }
]
for debt_data in debts_list:
    total = debt_data['quantity_of_items']* debt_data['price_per_item']
    balance=total-debt_data['price_paid']

    debt = Debts(
       customer_name=debt_data["customer_name"],
        customer_email=debt_data["customer_email"],
        items_taken=debt_data["items_taken"],
        quantity_of_items=debt_data["quantity_of_items"],
        price_per_item=debt_data["price_per_item"],
        total_price_to_pay=total,
        price_paid=debt_data["price_paid"],
        balance_to_pay=balance,
        created_at=debt_data["created_at"]  
    )
    debts_session.add(debt)
debts_session.commit()   

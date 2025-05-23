from main import Debts,debts_session,engine

debts=debts_session.query(Debts).all()


print("--------------customersnames----------")
for debt in debts:
  
    print(debt.customer_name)

#filtering
Isaac=debts_session.query(Debts).filter(Debts.customer_name=='Isaac Juma')
print(Isaac)


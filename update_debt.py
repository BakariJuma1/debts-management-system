
from main import Debts,debts_session,engine


customer_to_update=debts_session.query(Debts).filter(Debts.customer_name =='Mary Wambui').first()

if customer_to_update:
          customer_to_update.items_taken = "3ply"
          debts_session.commit()
          print(f" {customer_to_update.customer_name} updated successfully")
else:
        print('update failed')          


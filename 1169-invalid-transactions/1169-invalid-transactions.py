class Solution:
    
    """
    In order to solve this problem, we need to define a helper function to handle current transaction with 
    previous transaction.
    """
    
    
    def is_invalid(self, transaction, previous_transactions):
        
        name, time, amount, city = transaction.split(",")
        
        
        # Check if amount is greater than $1000
        if int(amount) > 1000:
            return True
        
        for prev_transaction in previous_transactions:
            prev_name, prev_time, pre_amount, prev_city = prev_transaction.split(",")
            
            if prev_name == name and prev_city != city and abs(int(time) - int(prev_time)) <= 60:
                return True
            
        return False
    
    
    
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        invalid = []
        processed = []
        
        for transaction in transactions:
            if self.is_invalid(transaction, transactions):
                invalid.append(transaction)
            
            else:
                processed.append(transaction)
                
        return invalid
        
        
        
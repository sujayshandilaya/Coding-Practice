SELECT account_id, sum(case when transaction_type='Deposit' then amount else -1*amount end) as final_balance
FROM transactions group by 1;
Solution 1: Select N, 
case 
when cnt= 1 then 'Leaf'
when cnt=2 and P is null then 'Root' 
else 'Inner' 
end
from (
Select N, P, Count(*) cnt from (Select BST1.N, BST1.P from BST BST1 left join BST BST2 on BST1.N = BST2.P)tbl1 group by 1,2) tbl2 order by 1

Solution 2: 

select N, 
case when P is null then 'Root' 
when N IN (SELECT DISTINCT P FROM  BST) then 'Inner'
else 'Leaf'
end as NodeType 
from BST 
order by N

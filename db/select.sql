select prod.name , cat.name 
from product prod
left join productscategorii prodcat on prod.id = prodcat.products_id
inner join categorii cat on cat.id = prodcat.category_id
order by prod.name
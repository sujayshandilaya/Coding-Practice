class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        op=[]
        products.sort()
        for i in range(1,len(word)+1):
            prefix=word[:i]
            temp=[]
            for product in products:
                if product.startswith(prefix):
                    temp.append(product)
                    if len(temp)==3:
                        op.append(temp)
                        break
            else:
                op.append(temp)
        return op
########################################
class Solution:
    def suggestedProducts(self, products: List[str], word: str) -> List[List[str]]:
        op=[]
        products.sort()
        for i,c in enumerate(word):
            products=[product for product in products if i < len(product) and product[i]==c]
            op.append(products[:3])
        return op

class Cypher:
    def __init__(self,code:str) -> None:
        self.code = code
    
    def convert(self)-> str:
        code = self.cypherize(self.code)
        return code
    
    @classmethod
    def cypherize(cls,code:str) ->str:
        cypher = ""
        for char in code:
            if char.isalpha():
                if char.islower():
                    part = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
                else:
                    part = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            else:
                if char.isdigit():
                    if char=='9':
                        part='0'
                    else:
                        part=str(int(char)+1)
                else:
                    part = char
        
            if char.islower():
                part = part.upper()
            else:
                part = part.lower()
            cypher += part
        return cypher

def convert_to_cypher():
    print("\n\n-- CONVERT TO CYPHER --")
    code = input("Enter the string to convert to cypher : ")
    cypher1 = Cypher(code)
    cypher = cypher1.convert()
    print(f"\nThe corresponding cypher for {code} is : {cypher}")

convert_to_cypher()




        
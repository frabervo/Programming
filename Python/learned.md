# Enumerate(iterable, start=0)
This is a function built into Python. 
- iterable: must be a sequence: Like a list, tuple or string
- start: is the start of the enumeration
- return value: the function returns a tuple of (index, value).

example:
```
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
list(enumerate(seasons))
>>> output: [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
```
```
words= "Manger"
for index, iterator in enumerate (words,start=0):
  print("iterator: "+ iterator + " und index: " +str(index) )
>>> output: iterator: M und index: 0
        iterator: a und index: 1
        iterator: n und index: 2
        iterator: g und index: 3
        iterator: e und index: 4	
        iterator: r und index: 5
```

# Function definition with paramter-type
It is possible to specify in the definition which data type the parameters have as well as the return value:  

example:
```
def twoSum(self, nums: List[int], target: int) -> List[int]:
```

# String-Methoden
```
word = "string"
```
- `word.lower()` write everything in small letters
- `word.upper()` Capitalise all
- `word.title()` first letter upper case and the rest lower case
- `word.isupper()` True, when everything is capitalised
- `word.islower()` True, when everything is written in lower case
- `word.capitalize()` True, when the first letter is upper case and the rest lower case

# Regex-Methode (re) 
This method is used to compare string with a rational expression. The use of this method requires the library "re".  
Uni-code( string) as well as bytes can be compared.
In a regex, special characters are not interpreted. That is, "\n" is interpreted as a string with "\" and "n" . 

Rules when comparing: 

- Let A and B be two rational expressions. A and B can be concatenated to create a new expression AB. In that case qp matches AB if q matches A and p matches B too. 
- | and ( are special characters

|**Opérateurs**|**Description**|**Exemples**|
| :-: | :-: | :-: |
|||**Expression régulière**|**Chaînes décrites**|**Chaînes non décrites**|
|*expr1 expr2*|Concatenation operator of two expressions (implicit).|ab|« ab »|« a », « b », empty string|
|.|One character and one only|.|« a », « b », etc.|empty string, « ab »|
|*expr*?|This quantifier matches what precedes it, present **zero or once**. If multiple matches exist in a text, it first finds those placed at the head of the text and then returns the longest possible length from that initial position.|a?|empty string, « a »|« aa », « b »|
|*expr*+|This quantifier matches what precedes it, repeated **once or more**. If multiple matches exist in a text, it first finds those placed at the head of the text and then returns the longest possible length from that initial position.|a+|« a », « aa », « aaaaa », etc.|empty string, « b », « aaab »|
|*expr*\*|This quantifier matches what precedes it, repeated **zero or multiple times**. If multiple matches exist in a text, it first finds those placed at the head of the text and then returns the longest possible length from that initial position.|a\*|empty string, « a », « aaa », etc.|« b », « aaab »|
|*expr1*\|*expr2*|It is the operator of choice between several alternatives, i.e. the set union. It can be combined as many times as necessary for each of the possible alternatives. It matches **one of the expressions placed before or after the operator**. These expressions may be empty, so (x|) is equivalent to x?|a|b|« a », « b »|empty string, « ab », « c »|
|[*liste*]|One of the characters in square brackets ("character class")|[aeiou]|« a », « e », « i », etc.|empty string, « b », « ae »|
|[^*liste*]|A character not in square brackets ("character class")|[^aeiou]|« b », etc.|empty string, « a », « bc »|

The method can be read here:  <https://docs.python.org/fr/3/library/re.html> 
About Wikipedia you can learn more about the history of the method: <https://de.wikipedia.org/wiki/Regul%C3%A4rer_Ausdruck> 

Example: The match() function here returns the first word
```
import re
result= re.match(r"(?P<First>\w+)", "Ami Python ici")
print(result.group('First'))
```
Example 2: The findall() function here searches for all words that start with an uppercase letter and then lowercase letters.
```
import re
word= re.findall(r"[A-Z].[a-z]+", " j'apprends Python maintenant a Emerson.")
print(word)
```

# Learn about the mysql.connector library

- ### Querying data with mysql.connector 
<https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html> 

1. establish connection and store the connection object in a variable.
2. call the cursor() method from the connection object and store the result in a new variable. 

## What is cursor()?

<https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor.html> 

The MYSQLCursor class is a class that can be used to execute SQL statement. Cursor objects interact with the MySQL server through a MySQL Connection object.
```
import mysql.connector
cnx = mysql.connector.connect(database='world')
cursor = cnx.cursor()
```
[^note]:
  *The package mysql.connector must be installed first: ```python3 -m pip install mysql-connector```*


### Methoden der Klasse MYSQLCursor
- ```result\_args = cursor.callproc(proc\_name, args=())```: Calls a stored procedure. 

The args parameter sequence must contain an entry for each argument the procedure expects. callproc()returns a modified copy of the input sequence.

Example: 
in Myslql:
```
CREATE PROCEDURE multiply(IN pFac1 INT, IN pFac2 INT, OUT pProd INT)
BEGIN
  SET pProd := pFac1 \* pFac2;
END;
````
Python code
```
args = (5, 6, 0) # 0 is to hold value of the OUT parameter pProd
cursor.callproc('multiply', args)

>>> Output: ('5', '6', 30L)
```
- ```cursor.close()``` Used when done with the class. 
- ```iterator = cursor.execute(operation, params=None, multi=True)```

This command executes the operation ( statement or command) in the database. Parameters can be passed. If the parameter "multi" is set to "True", multiple queries can be executed.

example: 
```
insert\_stmt = ("INSERT INTO employees (emp\_no, first\_name, last\_name, hire\_date) ", "VALUES (%s, %s, %s, %s)")
data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
cursor.execute(insert\_stmt, data)
select\_stmt = "SELECT \* FROM employees WHERE emp\_no = %(emp\_no)s"
cursor.execute(select\_stmt, { 'emp\_no': 2 })
```

**Mit „multi“ auf True**
```
operation = 'SELECT 1; INSERT INTO t1 VALUES (); SELECT 2'
for result in cursor.execute(operation, multi=True):
  if result.with\_rows:
    print("Rows produced by statement '{}':".format(result.statement))
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(result.statement, result.rowcount))
```

# The function zip 
```
strs= ["flower","flow","flight"]
for c in zip(\*strs):
  print(c)

>>>Output:  ('f', 'f', 'f')
            ('l', 'l', 'l')
            ('o', 'o', 'i')
            ('w', 'w', 'g')
```
# The Function sort()
```
strs= ["flower","flow","flight"]
strs.sort()
print(strs)
>>> output: ['flight', 'flow', 'flower']
```

Here the function sort() compares the elements with each other. it results that the first element is very different from the last element.


user = {'name': 'vipul',
'height': '5.6',
'shoe size': '8',
'hair': 'black',
'eyes': 'brown',
'favorite movies': ['Rambo','Creed','love']}

mattan = {'name': 'Mattan',
          'height': 70,
          'shoe size': 10.5,
          'hair': 'Brown',
          'eyes': 'Brown',
          'favorite movies': ['Pulp Fiction',
                              'Magnolia',
                              'The Royal Tenenbaums']}

chris =  {'name': 'Chris',
          'height': 72,
          'shoe size': 11,
          'hair': 'Blonde',
          'eyes': 'Blue',
          'favorite movies': ['Shawshank Redemption',
                              'Lord of the Rings']}

lisa =   {'name': 'Lisa',
          'height': 64,78:
          'shoe size': 6.5,
          'hair': 'Black',
          'eyes': 'Brown',
          'favorite movies': ['Crazy Rich Asians',
                              'Avengers',
                              'Lord of the Rings']}
data=[user, mattan,chris,lisa]

bunty =   {'name': 'bunty',
          'height': 64,
          'shoe size': 6.5,
          'hair': 'Black',
          'eyes': 'Brown',
          'favorite movies': ['Crazy Rich Asians',
                              'Avengers',
                              'Lord of the Rings']}
data.append(bunty)
print (data)

#for name in (data):
#    print(f"""{name['name']}'s shoe size is {name['shoe size']} & other details are as below
#    Height is {name['height']}
#    Hair is {name['hair']}
#    Eye color is {name['eyes']}
#    Fav movies is {'.'.join(name['favorite movies'])}""")

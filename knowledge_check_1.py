print('hello world!')
values = [1, 2, 3, 4]
print (values[0])
dictionary = {
    "dog": "Corgi",
    "cat" : "Calico",
}
print(dictionary["dog"])
mealtimes = ("10:00AM", "1:00PM", "5:00PM", "9:00PM")
print(mealtimes[0])

pets = [
    {
    "species" : "Dog",
    "type" : "Corgi",
    "mealtimes" : ("10:00AM", "1:00PM", "5:00PM", "9:00PM"),
    "Friendly before meal?" : True},
    {
    "species" : "Cat",
    "type" : "Calico"
    "mealtimes" : ("8:00AM", "11:00AM", "4:00PM", "8:00PM"),
    "Friendly before meal?" : False
    }
]
print(pets[0])
print(pets["species"])
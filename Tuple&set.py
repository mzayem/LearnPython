mytuple = ("apple", "banana", "cherry")
print(mytuple)
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict["color"] = "red"
thisdict.update({"color": "white"})
thisdict["ket"] = "maroon"
thisdict.popitem()
# thisdict.pop("ket")
# del thisdict("ket")
print(thisdict)
'''
**Q: What are `__len__`, `__getitem__`, and `__contains__` in Python?**

`__len__` object ki length return karta hai aur `len()` ke saath use hota hai.

`__getitem__` indexing ya key-based access support karta hai, jaise `obj[0]`.

`__contains__` membership checking implement karta hai, jaise `value in obj`.

In special methods ki madad se hum custom objects ko built-in Python collections jaisa behavior de sakte hain.
'''

class Playlist:
    def __init__(self, playlist):
        self.playlist = playlist

    def __len__(self):
        return len(self.playlist)

    def __getitem__(self, index):
        return self.playlist[index]

    def __contains__(self, value):
        return value in self.playlist


playlist = Playlist(["Dil Dil Pakistan", "Afreen", "Pasoori"])
print(len(playlist))                 # 3
print(playlist[0])                   # Dil Dil Pakistan
print("Pasoori" in playlist)         # True
print("Shape of You" in playlist)    # False
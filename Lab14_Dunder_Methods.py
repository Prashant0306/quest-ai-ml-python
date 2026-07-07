# ============================================
# Lab 4: Dunder (Magic) Methods
# ============================================
# "Dunder" = Double UNDERscore, e.g. __init__, __str__.
# These let YOUR objects work with built-in syntax (+, ==, len(), print()...).

class Money:
    def __init__(self, amount, currency="INR"):
        self.amount = amount
        self.currency = currency

    # ---- __str__ : what print() / str() shows (human-friendly) ----
    def __str__(self):
        return f"{self.amount} {self.currency}"

    # ---- __repr__ : the "developer" representation (debugging, REPL) ----
    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    # ---- __add__ : enables the + operator ----
    def __add__(self, other):
        if self.currency != other.currency:
            raise ValueError("Currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    # ---- __eq__ : enables == comparison ----
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    # ---- __lt__ : enables < (and lets sorted() work) ----
    def __lt__(self, other):
        return self.amount < other.amount


wallet = [Money(10),Money(20),Money(30)]

print(wallet)


# wallet = Money(100) + Money(50)        # uses __add__
# print("total:", wallet)                # uses __str__  -> "150 INR"
# print("repr :", repr(wallet))          # uses __repr__ -> Money(150, 'INR')
# print("equal?", Money(50) == Money(50))            # __eq__ -> True
# print("sorted:", sorted([Money(30), Money(10), Money(20)]))   # __lt__


# # ---- A container-like object ----
# class Playlist:
#     def __init__(self):
#         self.songs = []

#     def add(self, song):
#         self.songs.append(song)

#     def __len__(self):                 # enables len(playlist)
#         return len(self.songs)

#     def __getitem__(self, index):      # enables playlist[0] AND for-loops
#         return self.songs[index]

#     def __contains__(self, song):      # enables 'song in playlist'
#         return song in self.songs


# pl = Playlist()
# pl.add("Song A")
# pl.add("Song B")
# print("length:", len(pl))              # __len__   -> 2
# print("first :", pl[0])                # __getitem__ -> "Song A"
# print("has B?", "Song B" in pl)        # __contains__ -> True
# for song in pl:                        # works because of __getitem__
#     print("playing:", song)


# ---- TRY THIS (uncomment to explore) ----
# Add __mul__ to Money so 'Money(50) * 3' works:
# def __mul__(self, factor):
#     return Money(self.amount * factor, self.currency)

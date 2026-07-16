library_data = {
    "M1" : ["ABC","XYZ"],
    "M2" : ["Irodov", "black_book"],   
    "M3" : ["ABC", "Bhagvat_gita"], 
    "M4" : [],
    "M5" : ["ABC", "black_book"],
    "M6" : []
}
 

total_members = len(library_data)
total_book = 0
zero_borroweers = 0


# for avg and zero borrowers
for members in library_data:
    book_borrowed = library_data[members]
    num_books = len(book_borrowed)
    total_book += num_books

    if num_books == 0:
        zero_borroweers += 1

Avg_books = total_book/total_members


# Making a list of all books 
all_books =[]
for members in library_data:
    book_borrowed = library_data[members]
    for book in book_borrowed:
        all_books.append(book)


# making a dict for book and there score
book_score = {}
for book in all_books:
    if book in book_score:
     book_score[book] += 1
    else:
        book_score[book] = 1


# for highest and lowest book borrowed
highest_score= -1
H_B_B =""

lowest_score = 100
L_B_B =""


for book in book_score:
    score = book_score[book]
    
    if score > highest_score:
        highest_score = score
        H_B_B = book
        
    if score < lowest_score:
        lowest_score = score
        L_B_B = book

# --- FINAL OUTPUT ---
print("--- Library Report ---")
print(f"Average books borrowed: {Avg_books}")
print(f"Members with zero borrowing: {zero_borroweers}")
print(f"Most borrowed book: '{H_B_B}' (Borrowed {highest_score} times)")
print(f"Least borrowed book: '{L_B_B}' (Borrowed {lowest_score} times)")
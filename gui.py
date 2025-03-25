import tkinter as tk
from recommender import recommend_manga

def get_recommendations():
    manga_name = entry.get()
    results = recommend_manga(manga_name)
    output.delete(1.0, tk.END)
    for manga in results:
        output.insert(tk.END, manga + '\n')

# GUI setup
root = tk.Tk()
root.title("Manga Recommender")

tk.Label(root, text="Enter a manga title you like:").pack()

entry = tk.Entry(root, width=50)
entry.pack()

tk.Button(root, text="Recommend", command=get_recommendations).pack()

output = tk.Text(root, height=10, width=50)
output.pack()

root.mainloop()

import requests
import json
import tkinter as tk
from tkinter import messagebox

def get_github_data():
    username = entry.get().strip()
    if not username:
        messagebox.showwarning("Ошибка", "Введите имя пользователя GitHub")
        return

    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        user_data = response.json()

        filtered_data = {
            'company': user_data.get('company'),
            'created_at': user_data.get('created_at'),
            'email': user_data.get('email'),
            'id': user_data.get('id'),
            'name': user_data.get('name'),
            'url': user_data.get('url')
        }

        with open(f"github_{username}.json", "w", encoding="utf-8") as f:
            json.dump(filtered_data, f, indent=2, ensure_ascii=False)

        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, json.dumps(filtered_data, indent=2, ensure_ascii=False))

        messagebox.showinfo("Успех", f"Данные сохранены в файл: github_{username}.json")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Ошибка", f"Не удалось получить данные: {str(e)}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Произошла ошибка: {str(e)}")


root = tk.Tk()
root.title("GitHub Data Fetcher")
root.geometry("500x400")

tk.Label(root, text="Введите имя пользователя GitHub:").pack(pady=10)
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
entry.insert(0, "kubernetes")  

tk.Button(root, text="Получить данные", command=get_github_data, bg="lightblue").pack(pady=10)

tk.Label(root, text="Результат:").pack(pady=5)
result_text = tk.Text(root, height=15, width=60)
result_text.pack(pady=10)

root.mainloop()
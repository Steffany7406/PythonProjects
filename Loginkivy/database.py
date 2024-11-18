import datetime

class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    email, password, name, created = line.strip().split(",")
                    self.users[email] = (password, name, created)
        except FileNotFoundError:
            print(f"O arquivo {self.filename} não foi encontrado. Um novo será criado ao adicionar usuários.")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")

    @staticmethod
    def get_date():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def get_user(self, email):
        return self.users.get(email, -1)

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), self.get_date())
            self.save()
            return 1
        else:
            print("Email já existe")
            return -1

    def validate(self, email, password):
        user = self.get_user(email)
        if user != -1:
            return user[0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w", encoding="utf-8") as fd:
            for user in self.users:
                fd.write(f"{user},{self.users[user][0]},{self.users[user][1]},{self.users[user][2]}\n")

# Exemplo de uso
if __name__ == "__main__":
    db = DataBase("users.txt")
    db.add_user("test@example.com", "password123", "Test User")
    print(db.validate("test@example.com", "password123"))  # Deve retornar True
class Email:
    def __init__(self, sender, receiver, content, is_send=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = is_send

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

line = input()

while line != "Stop":
    sender, receiver, content = line.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

send_emails = list(map(lambda x: int(x), input().split(", ")))
for index in send_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())
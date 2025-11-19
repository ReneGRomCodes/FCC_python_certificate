import datetime


class Email:

    def __init__(self, sender: User, receiver: User, subject: str, body: str):
        self.sender: User = sender
        self.receiver: User = receiver
        self.subject: str = subject
        self.body: str = body
        self.timestamp: datetime.datetime = datetime.datetime.now()
        self.read: bool = False

    def mark_as_read(self) -> None:
        self.read = True

    def display_full_email(self) -> None:
        self.mark_as_read()
        print('\n--- Email ---')
        print(f'From: {self.sender.name}')
        print(f'To: {self.receiver.name}')
        print(f'Subject: {self.subject}')
        print(f"Received: {self.timestamp.strftime('%Y-%m-%d %H:%M')}")
        print(f'Body: {self.body}')
        print('------------\n')

    def __str__(self) -> str:
        status: str = 'Read' if self.read else 'Unread'
        return f"[{status}] From: {self.sender.name} | Subject: {self.subject} | Time: {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class Inbox:
    def __init__(self):
        self.emails: list[Email] = []

    def receive_email(self, email) -> None:
        self.emails.append(email)

    def list_emails(self) -> None:
        if not self.emails:
            print('Your inbox is empty.\n')
            return

        print('\nYour Emails:')
        for i, email in enumerate(self.emails, start=1):
            print(f'{i}. {email}')


    def read_email(self, index: int) -> None:
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index: int = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        self.emails[actual_index].display_full_email()

    def delete_email(self, index: int) -> None:
        if not self.emails:
            print('Inbox is empty.\n')
            return

        actual_index: int = index - 1
        if actual_index < 0 or actual_index >= len(self.emails):
            print('Invalid email number.\n')
            return

        del self.emails[actual_index]
        print('Email deleted.\n')


class User:
    def __init__(self, name: str):
        self.name: str = name
        self.inbox: Inbox = Inbox()

    def send_email(self, receiver: User, subject: str, body: str) -> None:
        email: Email = Email(sender=self, receiver=receiver, subject=subject, body=body)
        receiver.inbox.receive_email(email)
        print(f'Email sent from {self.name} to {receiver.name}!\n')

    def check_inbox(self) -> None:
        print(f"\n{self.name}'s Inbox:")
        self.inbox.list_emails()

    def read_email(self, index: int) -> None:
        self.inbox.read_email(index)

    def delete_email(self, index: int) -> None:
        self.inbox.delete_email(index)


def main():
    tory: User = User('Tory')
    ramy: User = User('Ramy')

    tory.send_email(ramy, "Hello", "Hi Ramy, just saying hello!")
    ramy.send_email(tory, "Re: Hello", "Hi Tory, hope you are fine.")

    ramy.check_inbox()
    ramy.read_email(1)
    ramy.delete_email(1)
    ramy.check_inbox()


if __name__ == '__main__':
    main()

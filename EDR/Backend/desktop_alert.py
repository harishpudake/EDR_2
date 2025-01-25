from plyer import notification

class DesktopAlert():

    def __init__(self, title, msg):
        self.title =  title
        self.msg = msg

    def show_alert(self):
        notification.notify(
            title=self.title,
            message=self.msg,
        )

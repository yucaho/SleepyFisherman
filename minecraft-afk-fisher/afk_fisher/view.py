class ConsoleView:
    """Console messages for status and user feedback."""

    @staticmethod
    def show_message(message: str) -> None:
        print(message)

    def show_startup(self) -> None:
        self.show_message("Oh yeah, let's do this!")

    def show_start(self) -> None:
        self.show_message("Enjoy fishing!")

    def show_stop(self) -> None:
        self.show_message("Catch anything good?")

    def show_bite(self) -> None:
        self.show_message("Oh! It's a bite!")

    def show_recast(self) -> None:
        self.show_message("SaulGOD used SUPER ROD!")

    def show_exit(self) -> None:
        self.show_message("See you space cowboy...")
